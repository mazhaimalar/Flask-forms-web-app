#!c:\gayathri\forms\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'utmp==0.4','console_scripts','utmp'
__requires__ = 'utmp==0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('utmp==0.4', 'console_scripts', 'utmp')()
    )
