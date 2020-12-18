#!/usr/bin/python/
print("content-type: text/html"\n)

import cgi
import subprocess as sp

y=cgi.FieldStorage()
osname=y.getvalue("x")

print(osname)
cmd="sudo docker run -i -t --name {0} ubuntu".format(osname)

output=sp.getstatusoutput(cmd)


status=output[0]
out=output[1]

if status==0 :
 print("ur { } has been launched".format(osname))
else :
 print("ther is an error {}".format(out))
