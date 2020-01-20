import os
import tempfile


def get_temp():
    temp_file = tempfile.mkdtemp()
    print(temp_file)
    return temp_file


def return_path(filename, dir):
    path = os.path.join("{0}{1}.csv".format(dir, filename))
    return path
