from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanException


class LoopToolsConan(ConanFile):
    name = "LoopTools"
    version = "2.15"
    license = "LGPL-3.0-only"
    author = "Alexander Voigt"
    url = "http://www.feynarts.de/looptools/"
    description = "Package for the evaluation of scalar and tensor one-loop integrals"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
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

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("COPYING", src=self._source_subfolder, dst="licenses", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ooptools"]