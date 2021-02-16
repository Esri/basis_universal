from conans import ConanFile


class BasisUniversalConan(ConanFile):
    name = "basis_universal"
    version = "0.1"
    url = "https://devtopia.esri.com/3rdparty/basis_universal/tree/runtimecore"
    license = "esri"
    description = "Basis Universal for Scene Layer Library."

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/basis_universal/"

        # headers
        self.copy("*.h*", src=base + "encoder", dst=relative + "encoder")
        self.copy("*.h*", src=base + "transcoder", dst=relative + "transcoder")
 
        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
