Email=input("Enter your email... ")
k=0
j=0
if len(Email)>=6:
    if Email[0].isalpha():
        if ("@" in Email)and (Email.count("@")==1):
            if(Email[-4]==".")^(Email[-3]=="."):
                for i in Email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha:
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_"or i=="."or i=="@":
                        continue 
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong email 5")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")

else:
    print("Wrong email 1")