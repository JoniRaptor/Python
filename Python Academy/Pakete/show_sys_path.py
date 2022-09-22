"""Show sys.path"""

import pprint
import sys

def show_sys_path(x=[]):
    """Show sys.path"""
    pprint.pprint(sys.path)
    return 42
    a = 100  # pylint: disable=unreachable, unused-variable

if __name__ == '__main__':
    show_sys_path()
