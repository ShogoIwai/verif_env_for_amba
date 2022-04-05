import sys
import misc

def setenv_cadence():
    dict_ary = misc.csv2dict_from_home()

    cds_floating_license = dict_ary['cds_floating_license']
    eda_path = dict_ary['eda_path']
    tool_path = dict_ary['tool_path']

    # xcelium_home = f'{eda_path}/Cadence/Xcelium/XCELIUM20.09.007'
    xcelium_home = f'{tool_path}/cadence/xcelium/XCELIUM21.09.007'

    misc.add_license(f'{cds_floating_license}')

    misc.add_path(f'{xcelium_home}/bin')
    misc.add_path(f'{xcelium_home}/tools/bin')

    misc.add_lib(f'{xcelium_home}/tools/lib')
    misc.add_lib(f'{xcelium_home}/tools/lib/64bit')
    misc.add_lib(f'{xcelium_home}/tools/inca/lib')
    misc.add_lib(f'{xcelium_home}/tools/tbsc/lib/gnu')
    misc.add_lib(f'{xcelium_home}/tools/systemc/gcc/install/lib')

    misc.add_env('CDS_INST_DIR', f'{xcelium_home}')
    misc.add_env('NCSC_CDS_ROOT', f'{xcelium_home}')
    misc.add_env('CDS_LIC_QUEUE_POLL', '1')

if __name__ == '__main__':
    setenv_cadence()
    misc.exec_argv(sys.argv[1:])
