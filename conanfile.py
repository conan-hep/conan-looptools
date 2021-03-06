import os
from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanException
from conans.model.version import Version
from conans.tools import SystemPackageTool

# python 2 / 3 StringIO import
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class LoopToolsConan(ConanFile):
    name = "LoopTools"
    version = "2.15"
    license = "LGPL-3.0-only"
    author = "Alexander Voigt"
    url = "http://www.feynarts.de/looptools/"
    description = "Package for the evaluation of scalar and tensor one-loop integrals"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"fPIC": [True, False]}
    exports = ["LICENSE"]
    default_options = ("fPIC=True")
    generators = ["cmake", "make", "pkg_config"]
    _source_subfolder = "LoopTools-{}".format(version)

    def _have_fortran_compiler(self):
        return tools.which("gfortran") != None or tools.which("ifort") != None

    def _have_c_compiler(self):
        return tools.which("gcc") != None or tools.which("clang") != None

    def source(self):
        src_file = "http://www.feynarts.de/looptools/LoopTools-{}.tar.gz".format(self.version)

        try:
            tools.get(src_file)
        except ConanException:
            raise ConanException("Could not download source code {}".format(src_file))

    def build(self):
        with tools.chdir(self._source_subfolder):
            autotools = AutoToolsBuildEnvironment(self)
            env_build_vars = { 'CC': 'gcc'} # clang gives relocation errors
            if self.options.fPIC:
                env_build_vars['FFLAGS'] = '-fPIC'
                env_build_vars['CFLAGS'] = '-fPIC'
                env_build_vars['CXXFLAGS'] = '-fPIC'
            autotools.configure(vars=env_build_vars, build=False, host=False)
            autotools.make()

    def system_requirements(self):
        installer = SystemPackageTool()

        if not (self._have_fortran_compiler() and self._have_c_compiler()):
            if tools.os_info.is_linux:
                if tools.os_info.with_pacman or tools.os_info.with_yum or tools.os_info.with_zypper:
                    installer.install("gcc")
                    installer.install("gcc-fortran")
                else:
                    installer.install("gcc")
                    installer.install("gfortran")
                    versionfloat = Version(self.settings.compiler.version.value)
                    if self.settings.compiler == "gcc":
                        if versionfloat < "5.0":
                            installer.install("libgfortran-{}-dev".format(versionfloat))
                        else:
                            installer.install("libgfortran-{}-dev".format(int(versionfloat)))

        if tools.os_info.is_macos and Version(self.settings.compiler.version.value) > "7.3":
            try:
                installer.install("gcc")
            except Exception:
                self.output.warn("brew install gcc failed. Tying to fix it with 'brew link'")
                self.run("brew link --overwrite gcc")

    def package(self):
        for header in ["looptools.h", "clooptools.h"]:
            self.copy(header, dst="include",
                      src="{}{}build".format(self._source_subfolder, os.sep),
                      keep_path=False, symlinks=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("COPYING", src=self._source_subfolder, dst="licenses", keep_path=False)

    def _get_lib_path(self, libname):
        out = StringIO()
        try:
            self.run("gfortran --print-file-name {}".format(libname), output=out)
        except Exception as error:
            raise ConanException("Failed to run command: {}. Output: {}".format(error, out.getvalue()))
        path = os.path.normpath(out.getvalue().strip())
        return os.path.dirname(path) if os.path.exists(path) else None

    def _make_unique(self, seq):
        ''' Modified version of Dave Kirby solution '''
        seen = set()
        return [x for x in seq if x not in seen and not seen.add(x)]


    def package_info(self):
        self.cpp_info.libs = ["ooptools", "gfortran", "quadmath"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("m")
        self.cpp_info.libdirs = ["lib"]

        # explicit paths to libraries on MacOS
        if self.settings.os == "Macos":
            # add path of libgfortran
            path = self._get_lib_path('libgfortran.dylib')
            if path: self.cpp_info.libdirs.append(path)

            # add path of libquadmath
            path = self._get_lib_path('libquadmath.dylib')
            if path: self.cpp_info.libdirs.append(path)

            # add libgcc and its path, if available
            path = self._get_lib_path('libgcc.a')
            if path:
                self.cpp_info.libdirs.append(path)
                self.cpp_info.libs.append('gcc')

        self.cpp_info.libdirs = self._make_unique(self.cpp_info.libdirs)
