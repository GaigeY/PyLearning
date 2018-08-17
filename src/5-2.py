import sys
print "Argument count:"+str(len(sys.argv))

for i in range(0,len(sys.argv)):
    print ""+ str(i+1)+": "+ sys.argv[i]