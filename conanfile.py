import os
from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanException
from conans.model.version import Version
from conans.tools import SystemPackageTool


class LoopToolsConan(ConanFile):
    name = "LoopTools"
    version = "2.15"
    license = "LGPL-3.0-only"
    author = "Alexander Voigt"
    url = "http://www.feynarts.de/looptools/"
    description = "Package for the evaluation of scalar and tensor one-loop integrals"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    exports = ["LICENSE", "FindLoopTools.cmake"]
    default_options = ("shared=False", "fPIC=True")
    generators = ["cmake", "make", "pkg_config"]
    _source_subfolder = "LoopTools-{}".format(version)

    def source(self):
        src_file = "http://www.feynarts.de/looptools/LoopTools-{}.tar.gz".format(self.version)

        try:
            tools.get(src_file)
        except ConanException:
            raise ConanException("Could not download source code {}".format(src_file))

    def build(self):
        with tools.chdir(self._source_subfolder):
            autotools = AutoToolsBuildEnvironment(self)
            env_build_vars = autotools.vars
            env_build_vars['CC'] = 'gcc' # clang gives relocation errors
            autotools.configure(vars=env_build_vars)
            autotools.make()

    def system_requirements(self):
        installer = SystemPackageTool()

        if tools.os_info.is_linux:
            if tools.os_info.with_pacman or tools.os_info.with_yum:
                installer.install("gcc-fortran")
            else:
                installer.install("gfortran")
                versionfloat = Version(self.settings.compiler.version.value)
                if self.settings.compiler == "gcc":
                    if versionfloat < "5.0":
                        installer.install("libgfortran-{}-dev".format(versionfloat))
                    else:
                        installer.install("libgfortran-{}-dev".format(int(versionfloat)))

        if tools.os_info.is_macos and Version(self.settings.compiler.version.value) > "7.3":
            try:
                installer.install("gcc", update=True, force=True)
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
        self.copy('FindLoopTools.cmake', '.', '.')

    def package_info(self):
        self.cpp_info.libs = ["ooptools"]
