import os

from conans import ConanFile, CMake, tools


class LooptoolsTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ["cmake", "make", "pkg_config"]

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%stest_looptools_f" % os.sep)
            self.run(".%stest_looptools_c" % os.sep)
