from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/meet/Desktop/pythoncodes') if isfile(join('/home/meet/Desktop/pythoncodes', f))]
print(files_list);
