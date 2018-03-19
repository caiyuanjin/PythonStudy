import copy;
import socket;
# see the source file of this module
print copy.__file__;
f = open(r'/home/caijin/test.txt');
print f.read(7); ## Welcome
f.close();

f = open(r'/home/caijin/test.txt');
print f.read(); ## print the whole content in file

s = socket.socket();
host = socket.gethostname();
port = 1234;
s.connect((host, port));
print s.recv(1024);

