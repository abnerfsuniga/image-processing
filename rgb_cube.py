class RGB_Cube(object):
    _rmin = 0
    _rmax = 255
    _gmin = 0
    _gmax = 255
    _bmin = 0
    _bmax = 255

    def __init__(self, img):
        self._img = img
        self.resize()


    def resize(self):
        self._bmin = self._img[:,:,0].min()
        self._bmax = self._img[:,:,0].max()
        self._gmin = self._img[:,:,1].min()
        self._gmax = self._img[:,:,1].max()
        self._rmin = self._img[:,:,2].min()
        self._rmax = self._img[:,:,2].max()

    # Test funciton
    def print(self):
        print(self._bmin)
        print(self._bmax)
        print(self._gmin)
        print(self._gmax)
        print(self._rmin)
        print(self._rmax)