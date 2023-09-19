import sys, os
INTERP = os.path.expanduser("~/env/bin/python3")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from am_logger_back.wsgi import application