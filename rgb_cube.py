import numpy as np

class RGB_Cube(object):

    def __init__(self, b_list, g_list, r_list):
        self.b_list = np.unique(b_list)
        self.g_list = np.unique(g_list)
        self.r_list = np.unique(r_list)
        self.find_size()
        self.largest_side = max(self.bsize, self.gsize, self.rsize) 

    def find_size(self):
        self.bsize = abs(max(self.b_list) - min(self.b_list))
        self.gsize = abs(max(self.g_list) - min(self.g_list))
        self.rsize = abs(max(self.r_list) - min(self.r_list))

    def select_representative(self):
        self.rep_color = [int(np.mean(self.b_list)), int(np.mean(self.g_list)), int(np.mean(self.r_list))]

    # Test method
    def print(self):
        print(self.rep_color)

    