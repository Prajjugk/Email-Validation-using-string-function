Email=input("Enter the email\n") #User inputs the email
k=0
j=0
d=0
if (len(Email)>=6):# checks the length 
    if Email[0].isalpha(): # Email first letter should be alphabet
        if ("@"in Email) and (Email.count("@")==1): #checks whether @ is present and also checks the number of @ in the Email
            if (Email[-4]==".") ^ (Email[-3]=="."): # Email should contain "." at the end , for gmail.com the position should be -4 and -3 for .in
                for i in Email:
                    if(i==i.isspace()):# checks whether there is any space
                        k=1
                    elif i.isalpha(): # checks eery characr=ters are alphabets
                        if i==i.upper():# checks whether any upper case letter
                            j=1
                    elif i.isdigit(): #checks whether any digits are present
                            continue
                    elif i=="_" or i=="." or i=="@": #checks whether they contain only these 3 characters
                            continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("Rigth email")
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
    else:
        print("Wrong email 2")
else:
     print("Wrong email 1")




