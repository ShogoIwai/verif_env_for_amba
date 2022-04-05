import sys
import misc

def setenv_synopsys():
    dict_ary = misc.csv2dict_from_home()

    snp_floating_license = dict_ary['snp_floating_license']
    snp_floating_license_ext = dict_ary['snp_floating_license_ext']
    eda_path = dict_ary['eda_path']
    tool_path = dict_ary['tool_path']

    vcs_home = f'{eda_path}/Synopsys/vcs/R-2020.12-SP2'

    misc.add_license(f'{snp_floating_license_ext}')

    misc.add_path(f'{vcs_home}/bin')

    misc.add_lib(f'{vcs_home}/linux64/packages/IEEE/lib')
    misc.add_lib(f'{vcs_home}/linux64/packages/synopsys/lib')

    misc.add_env('VCS_HOME', f'{vcs_home}')
    misc.add_env('SNPSLMD_LICENSE_FILE', f'{snp_floating_license}')

if __name__ == '__main__':
    setenv_synopsys()
    misc.exec_argv(sys.argv[1:])
