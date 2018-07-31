
name=raw_input("enter a string ")
x=len(name)
for i in range(0,x):
    if name[i]==" ":
        print " ",

    else:
        w = ord(name[i])
        y = 110 - w
        z = (y * 2) - 1
        w = ord(name[i]) + z
        print chr(w),









