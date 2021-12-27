import socket,os,platform
print(socket.gethostname())
print(os.uname().nodename)
print(platform.uname()[1])