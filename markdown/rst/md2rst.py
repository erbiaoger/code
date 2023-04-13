import os

cwd = os.getcwd()
com = os.path.join(cwd, 'Computer')
tech = os.path.join(cwd, 'technology')
ba_con = os.path.join(cwd, 'BasicConfiguration')

file_com = [file for file in com if os.path.isfile(os.path.join(com, file))]
file_tech = [file for file in tech if os.path.isfile(os.path.join(tech, file))]
file_ba_con = [file for file in ba_con if os.path.isfile(os.path.join(ba_con, file))]

import glob

md_files = glob.glob(os.path.join(com, '*.md'))
for file in  md_files:
    name, _ = file.split('.')
    print(name)
    os.system('pandoc -s '+file+' -o '+name+'.rst')
