from conans import ConanFile, CMake
import shutil

class Md5aladinConan(ConanFile):
    name = "md5Aladdin"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        shutil.copytree(".", "md5Aladdin")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="md5Aladdin")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="md5Aladdin")
        self.copy("*md5aladin.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["md5Aladdin"]
