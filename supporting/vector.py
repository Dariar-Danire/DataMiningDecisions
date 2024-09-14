# Класс Vector для задачи №11

class Vector(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print('{%.2f;   %.2f;   %.2f}' % (self.x, self.y, self.z))