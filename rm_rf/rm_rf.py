import os
import shutil
import errno


def rm_rf(path):
    if not os.path.exists(path):
        return
    # We catch File not Found, just in case of a race condition
    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        else:
            shutil.rmtree(path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise (e)  # In case something strange happens
