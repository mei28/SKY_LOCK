import time 
import sys
import sg5010

s = sg5010.Sg5010(4,100)
time.sleep(0.5)
opened = sys.argv[1]

print(opened)
if(opened==1 or opened=='1'):
    print("Opening ...")
    s.setdirection(-10,-10)
elif(opened==0 or opened=='0'):
    print("Closing ...")
    s.setdirection(100,10)
else:
    print("Error")

time.sleep(0.5)
print("Good Bye")
