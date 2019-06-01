class RGB_Cube(object):

    def __init__(self, b_list, g_list, r_list):
        self.b_list = b_list
        self.g_list = g_list
        self.r_list = r_list
        self._bmin = b_list.min()
        self._bmax = b_list.max()
        self._gmin = g_list.min()
        self._gmax = g_list.max()
        self._rmin = r_list.min()
        self._rmax = r_list.max()
        self.find_size()

    def find_size(self):
        self._bsize = abs(self._bmax - self._bmin)
        self._gsize = abs(self._gmax - self._gmin)
        self._rsize = abs(self._rmax - self._rmin)

    # Test method
    def print(self):
        print(self._bmin)
        print(self._bmax)
        print(self._gmin)
        print(self._gmax)
        print(self._rmin)
        print(self._rmax)
        print(self._bsize)
        print(self._gsize)
        print(self._rsize)

    