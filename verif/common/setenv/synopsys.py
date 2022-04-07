import sys
import misc

def setenv_synopsys():
    dict_ary = misc.csv2dict_from_home()

    snp_floating_license = dict_ary['snp_floating_license']
    snp_floating_license_ext = dict_ary['snp_floating_license_ext']
    eda_path = dict_ary['eda_path']
    tool_path = dict_ary['tool_path']

    vcs_home = f'{eda_path}/Synopsys/vcs/R-2020.12-SP2'
    vcs_uvm_home = f'{vcs_home}/etc/uvm-1.1'
    verdi_home = f'{eda_path}/Synopsys/verdi/Q-2020.03-SP1-1'
    spyglass_home = f'{eda_path}/Synopsys/SpyGlass/SpyGlass_S-2021.09/SPYGLASS_HOME'
    dc_home = f'{eda_path}/Synopsys/DesignCompiler/S-2021.06-SP2'

    misc.add_license(f'{snp_floating_license_ext}')

    misc.add_path(f'{vcs_home}/bin')
    misc.add_path(f'{verdi_home}/bin')
    misc.add_path(f'{spyglass_home}/bin')
    misc.add_path(f'{dc_home}/amd64/syn/bin')

    misc.add_lib(f'{vcs_home}/linux64/packages/IEEE/lib')
    misc.add_lib(f'{vcs_home}/linux64/packages/synopsys/lib')
    misc.add_lib(f'{verdi_home}/share/PLI/IUS/LINUX64')
    misc.add_lib(f'{verdi_home}/share/PLI/IUS/LINUX64/boot')
    misc.add_lib(f'{verdi_home}/share/PLI/VCS/LINUX64')

    misc.add_env('SNPSLMD_LICENSE_FILE', f'{snp_floating_license}')
    misc.add_env('SPS_LICENSE_FILE', f'{snp_floating_license}')
    misc.add_env('VCS_LICENSE_WAIT', '1')
    misc.add_env('VCS_HOME', f'{vcs_home}')
    # misc.add_env('VCS_UVM_HOME', f'{vcs_uvm_home}')
    misc.add_env('VERDI_HOME', f'{verdi_home}')
    misc.add_env('SPYGLASS_HOME', f'{spyglass_home}')

if __name__ == '__main__':
    setenv_synopsys()
    misc.exec_argv(sys.argv[1:])
