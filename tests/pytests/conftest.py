import numpy as np

class SimpleSpice():
    def scs2e(self, *args):
        return 0.1
    def bods2c(self, x):
        return -12345
    def frmnam(self, id):
        return 'Test_Frame'
    def gdpool(self, key, x, length):
        return np.ones(length)
    def gipool(self, key, x, length):
        return np.arange(length)
    def bodvrd(self, key, x, length):
        return (3, np.ones(length,))
    def spkpos(self, *args):
        return (np.ones(3), None)
    def spkezr(self, *args):
        return (np.ones(6), None)
    def furnsh(self, *args):
        return
    def unload(self, *args):
        return
    def pxform(self, *args):
        return np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    def m2q(self, *args):
        return np.asarray([1,2,3,4])
    def bodn2c(self, *args):
        return "SPACE"
    def sct2e(self, *args):
        return 0.1
    def cidfrm(self, *args):
        return (2000, "Test_Body_Frame", True)

def get_mockkernels(self, *args):
    return "some_metakernel"
