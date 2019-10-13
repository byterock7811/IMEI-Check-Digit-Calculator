##Python 3

def luhn(imei):
    count=0
    for term in range(14):
        if term%2!=0:
            digit=int(imei[term])
            doubled=digit*2
            print(doubled)
            if len(str(doubled))==2:
                strdoubled=str(doubled)
                count=count+(int(strdoubled[0]))+(int(strdoubled[1]))
            else:
               count=count+doubled
        else:
            count=count+int(imei[term])
            print(count)
    strcount=str(count)
    last=strcount[-1]
    checkdigit=10-int(last)
    return checkdigit

another="y"
while another=="y" or another=="Y":
    imei=str(input("Please input IMEI number \n"))
    if len(imei)!=14 and len(imei)!=15:
        print("Please input IMEI of length 14 to calculate checkdigit or an IMEI of length 15 to check checkdigit")
    else:
        checkdigit=luhn(imei)
        if len(imei)==14:
            if checkdigit==10:
                print("The checkdigit is 0")
            else:
                print("The checkdigit is " + str(checkdigit))
        else:
            if checkdigit==10:
                if imei[-1]=="0":
                    print("Checkdigit is correct")
                else:
                    print("Checkdigit is incorrect! Checkdigit should be 0")
            elif checkdigit==int(imei[-1]):
                print("Checkdigit is correct")
            else:
                print("Checkdigit is incorrect! Checkdigit should be " + str(checkdigit))
        another=str(input("Would you like to test another Y/N \n"))
            
