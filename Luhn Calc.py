import sys
imei=str(sys.argv[1])
count=0
for i in range(14):
    if i%2!=0:
        digit=int(imei[i])
        doubled=digit*2
        if len(str(doubled))==2:
            strdoubled=str(doubled)
            count=count+(int(strdoubled[0]))+(int(strdoubled[1]))
        else:
           count=count+digit
    else:
        count=count+int(imei[i])

strcount=str(count)
last=strcount[-1]
if last=="0":
    print("The checkdigit is 0")
else:
    checkdigit=10-int(last)
    print("The checkdigit is " + str(checkdigit))

