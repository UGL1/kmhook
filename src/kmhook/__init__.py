import sys

if sys.platform == 'win32':
    from ._kmhook_win import *
else:
    print('kmHook is not supported on this platform.')
    from ._kmhook_other import *
