import os
import sys
import csv
import re

def csv2dict(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        dict_ary = {rows[0]:rows[1] for rows in reader}

    return dict_ary

def csv2dict_from_file():
    csvfile = os.path.dirname(__file__) + '/setenv.csv'
    return csv2dict(csvfile)

def csv2dict_from_home():
    csvfile = os.environ['HOME'] + '/setenv.csv'
    return csv2dict(csvfile)

def add_env(var_name, add_path):
    if (os.environ.get(var_name)):
        current_path = os.environ[var_name]
        update_path = add_path + ':' + current_path
        os.environ[var_name] = update_path
    else:
        os.environ[var_name] = add_path

def add_license(add_path):
    add_env('LM_LICENSE_FILE', add_path)

def add_path(add_path):
    add_env('PATH', add_path)

def add_lib(add_path):
    add_env('LD_LIBRARY_PATH', add_path)

def exec_argv(argv):
    str_list = argv
    m = re.search('\.py$', str_list[0])
    if (m):
        pyscr = str_list[0]
        if (not os.path.isfile(pyscr)):
            path_arry = os.environ['PATH'].split(':')
            for path in path_arry:
                fpath = path + '/' + pyscr
                if (os.path.isfile(fpath)):
                    pyscr = fpath
                    break
        str_list[0] = 'python ' + pyscr
    maped_list = map(str, str_list)
    argstr = ' '.join(maped_list)
    print(argstr)
    os.system(argstr)
