


class North():
    """Read heading position related to north"""

    file_name = '/sys/bus/iio/devices/iio:device4/in_rot_from_north_magnetic_tilt_comp_raw'

    def __init__(self, file_name = None):
        if file_name != None:
            self.file_name = file_name

    def read(self):
        f = open(self.file_name, 'r')
        h = f.readline()
        f.close()
        h = str(h)
        h = h[0:-1]
        return int(h) / 100000

    
class Incl():
    """Read incl sensors"""

    def read(self):
        x = self.read_file('/sys/bus/iio/devices/iio:device7/in_incli_x_raw')
        y = self.read_file('/sys/bus/iio/devices/iio:device7/in_incli_y_raw')
        z = self.read_file('/sys/bus/iio/devices/iio:device7/in_incli_z_raw')
        return [ self.get_incl_value(x), self.get_incl_value(y), self.get_incl_value(z) ]

    def read_file(self, file_name):
        f = open(file_name, 'r')
        v = f.readline()
        f.close()
        v = str(v)
        v = v[0:-1]
        return v
    
    def get_incl_value(self, value):
        v = int(value)
        return v / 100000

    def check_y(self, value):
        if value > -6 and value - 6:
            return True
        return False

    def get_orientation(self):
        values = self.read()
        if self.check_y(values[1]):
            if values[1] > 0:
                return 'normal'
            else:
                return 'inverted'
        return 'portrait'