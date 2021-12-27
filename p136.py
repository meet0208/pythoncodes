import os
print([f for f in os.listdir('/home/meet/Desktop') if os.path.isfile(os.path.join('/home/meet/Desktop', f))])