import os
import re

from wac2wav import wac2wav


class WacConverter:
    def __init__(self, root="", dest="", files=[]):
        self.rootDir = root
        self.destDir = dest
        self.files = files

    def files_to_wav(self, qt_console=None):
        regex = re.compile(r"^" + self.rootDir + "(.*)\.wac$")
        for fn in self.files:
            new = regex.sub(self.destDir + "\\1.wav", fn)
            dirname = os.path.dirname(new)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            if qt_console:
                qt_console.append("Converting {0} in {1}".format(fn, new))
            wac2wav(fn, new)


# if __name__ == '__main__':
#     wc = WacConverter(
#         "/home/vin/Doctorat/data/acoustic/field/wac",
#         "/home/vin/Doctorat/data/acoustic/field/wav", [
#             "/home/vin/Doctorat/data/acoustic/field/wac/2015/Igloolik24/IGLOOLIK24_20150615_170000.wac"
#         ])
#     wc.files_to_wav()
