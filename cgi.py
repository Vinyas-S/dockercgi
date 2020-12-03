#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess as sub
import cgi

dont = ["do not","don't","dont","nothing"]

y = cgi.FieldStorage()
p = y.getvalue("x").lower()

if any(ele in p for ele in dont) :
print("Please don't play with me")

elif not(any(ele in p for ele in dont)) and (("calendar" in p)):
print(sub.getstatusoutput("cal")[1])

elif not(any(ele in p for ele in dont)) and (("date" in p) or ("time" in p)):
print(sub.getstatusoutput("date")[1])

elif (p==""):
print("Sorry... But I haven't received any input from you!!!")

elif ("hello" in p) or ("hi" in p) or ("hey" in p):
print("Hello, I hope it's goning great")

elif ("thank" in p):
print("It's my pleasure")

else:
print("Sorry...Try it again....")
