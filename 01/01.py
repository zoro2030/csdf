import re
def matchre(data,*args):
    for regstr in args:
        matchObj = re.search( regstr+'.*', data, re.M|re.I)
        if matchObj:
            print (matchObj.group(0).lstrip().rstrip())
        else:
            print ("No ",regstr,"found")
        

filename= input("Enter path for email header file\n");
fo = open("01.txt") #fo=filehandle
data=fo.read()
matchre(data,"MIME-version","Date:","Subject:","Message-ID:","From:","To:")
fo.close()
