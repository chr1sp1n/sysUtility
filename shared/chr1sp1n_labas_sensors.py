from pathlib import PurePath, Path

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

    def __init__(self):
        try:
            self.file_path = None
            for d in range(1, 9):
                dir_name = Path('/sys/bus/iio/devices/iio:device' + str(d))
                if dir_name.is_dir():
                    for f in "xyz":
                        file_name = Path( str(dir_name) + '/in_incli_' + f +'_raw' )
                        if file_name.is_file():
                            dir_ok = True
                        else:
                            dir_ok = False
                            break
                    if dir_ok:
                        self.file_path = dir_name
                        break
            if self.file_path == None:
                raise ValueError("[ERRO] Can't find sensor file.")
        except:
            print ("[ERRO] Can't find sensor file.")
            exit(1)
        

    def read(self):
        x = Path(self.file_path, 'in_incli_x_raw').read_text()
        y = Path(self.file_path, 'in_incli_y_raw').read_text()
        z = Path(self.file_path, 'in_incli_z_raw').read_text()
        return [ self.get_incl_value(x), self.get_incl_value(y), self.get_incl_value(z) ]
    
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