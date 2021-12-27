import glob
file_list = glob.glob('*.*')
print(file_list)
print(glob.glob('*.py'))
print(glob.glob('./p[0-9]*.*'))