import platform as python_platform

from pysyte import imports
from pysyte import oss
from pysyte.bash import cmnds

_platform_name = python_platform.system().lower()
platform = imports.load_module(oss, _platform_name)


def _bash(command):
    if not command:
        return None
    status, output = cmnds.getstatusoutput(command)
    if status:
        raise ValueError(output)
    return output


def get_clipboard_data():
    return _bash(platform.bash_paste)
