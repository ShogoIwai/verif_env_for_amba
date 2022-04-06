import sys
import misc
import cadence
import synopsys

if __name__ == '__main__':
    cadence.setenv_cadence()
    synopsys.setenv_synopsys()
    misc.exec_argv(sys.argv[1:])
