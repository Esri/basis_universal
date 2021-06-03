from conans import ConanFile


class BasisUniversalConan(ConanFile):
    name = "basis_universal"
    version = "v1.15"
    url = "https://devtopia.esri.com/3rdparty/basis_universal/tree/runtimecore"
    license = "https://github.com/Esri/basis_universal/blob/master/LICENSE"
    description = "Basis Universal for Scene Layer Library."

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/basis_universal/"

        # headers
        self.copy("*.h*", src=base, dst=relative)
        self.copy("*.h*", src=base + "transcoder", dst=relative + "transcoder")
 
        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
