def search_details_staff(trans_ch):
    if trans_ch==1:
            f=open("air_staff.txt","r")
    elif trans_ch==2:
            f=open("water_staff.txt","r")
    elif trans_ch==3:
            f=open("rail_staff.txt","r")
            a=input("Enter name:")
            c=1
            while True:
                try:
                    name=f.readline()
                    if name.rstrip()=="Name : "+a:
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        print(f.readline())
                        break
                except:
                    print("Not found")
                    break
                    f.close()

def search_details_client(trans_ch):
    if trans_ch==1:
                f=open("air_client.txt","r")
    if trans_ch==2:
                f=open("water_client.txt","r")
    if trans_ch==3:
                f=open("rail_client.txt","r")
                a=input("Enter name:")
                c=1
    while True:
        try:
            name=f.readline()
            if name.rstrip()=="Name : "+a:
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                print(f.readline())
                break
        except:
                print("Not found")
                break
        f.close()



def write_details_staff(trans_ch):
    name=input("ENTER YOUR NAME: ")
    adhaar=int(input("ENTER YOUR ADHAAR NUMBER: "))
    address=str(input("ENTER YOUR PERMANENT ADDRESS: "))
    city=str(input("ENTER NAME OF YOUR CITY: "))
    state=str(input("ENTER NAME OF YOUR STATE: "))
    contact=int(input("ENTER YOUR CONTACT NUMBER: "))
    dob=input("ENTER YOUR DOB IN DD/MM/YYYY: ")
    doj=input("ENTER YOUR DOJ IN DD/MM/YYYY: ")
    qual=input("ENTER YOUR QUALIFICATIONS: ")
    post=input("ENTER YOUR POST: ")
    shift=input("ENTER YOUR SHIFT ROAT: ")
    print("")
    if trans_ch == 1:
        f=open("air_staff.txt",'w') 
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("DOJ : "+doj+"\n")
        f.write("qualifications : "+qual+"\n")
        f.write("post : "+post+"\n")
        f.write("shift : "+shift+"\n")
        f.close()

    elif trans_ch == 2:
        f=open("water_staff.txt",'w')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("DOJ : "+doj+"\n")
        f.write("qualifications : "+qual+"\n")
        f.write("post : "+post+"\n")
        f.write("shift : "+shift+"\n")
        f.close()
    elif trans_ch == 3:
        f=open("rail_staff.txt",'w')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("DOJ : "+doj+"\n")
        f.write("qualifications : "+qual+"\n")
        f.write("post : "+post+"\n")
        f.write("shift : "+shift+"\n")
        f.close()


def write_details_client(trans_ch):
    name=str(input("ENTER YOUR NAME : "))
    adhaar=int(input("ENTER YOUR ADHAAR NUMBER : "))
    address=str(input("ENTER YOUR PERMANENT ADDRESS : "))
    city=str(input("ENTER NAME OF YOUR CITY : "))
    state=str(input("ENTER NAME OF YOUR STATE : "))
    contact=int(input("ENTER YOUR CONTACT NUMBER : "))
    dob=input("ENTER YOUR DOB  IN DD/MM/YYYY : ")
    tra_from=str(input("ENTER NAME OF CITY YOU ARE TRAVELLING FROM : "))
    tra_to=str(input("ENTER NAME OF CITY YOU ARE TRAVELLING TO : "))
    booking_date=input("ENTER YOUR BOOKING DATE IN FORMATE OF 'DD/MM/YY' : ")
    print("")
    if trans_ch == 1:
        f=open("air_client.txt",'w')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("travelling from : "+tra_from+"\n")
        f.write("travellin to : "+tra_to+"\n")
        f.write("booking date : "+booking_date+"\n")
        f.close()
    elif trans_ch == 2:
        f=open("water_client.txt",'w')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("travelling from : "+tra_from+"\n")
        f.write("travellin to : "+tra_to+"\n")
        f.write("booking date : "+booking_date+"\n")
        f.close()
    elif trans_ch == 3:
        f=open("rail_client.txt",'w')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("travelling from : "+tra_from+"\n")
        f.write("travellin to : "+tra_to+"\n")
        f.write("booking date : "+booking_date+"\n")
        f.close()


def read_details_staff(trans_ch):
    if trans_ch == 1:
            f=open("air_staff.txt",'r')
            print(f.read())
    elif trans_ch==2:
            f=open("water_staff.txt","r")
            print(f.read())
    elif trans_ch==3:
            f=open("rail_staff.txt","r")


def read_details_client(trans_ch):
    if trans_ch==1:
            f=open("air_client.txt","r")
            print(f.read())
    elif trans_ch==2:
            f=open("water_client.txt","r")
            print(f.read())
    elif trans_ch==3:
            f=open("rail_client.txt","r")
            print(f.read())


def append_details_staff(trans_ch):
    name=input("ENTER YOUR NAME: ")
    adhaar=int(input("ENTER YOUR ADHAAR NUMBER: "))
    address=str(input("ENTER YOUR PERMANENT ADDRESS: "))
    city=str(input("ENTER NAME OF YOUR CITY: "))
    state=str(input("ENTER NAME OF YOUR STATE: "))
    contact=int(input("ENTER YOUR CONTACT NUMBER: "))
    dob=input("ENTER YOUR DOB IN DD/MM/YYYY: ")
    doj=input("ENTER YOUR DOJ IN DD/MM/YYYY: ")
    qual=input("ENTER YOUR QUALIFICATIONS: ")
    post=input("ENTER YOUR POST: ")
    shift=input("ENTER YOUR SHIFT ROAT: ")
    print("")
    if trans_ch == 1:
        f=open("air_staff.txt",'a')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("DOJ : "+doj+"\n")
        f.write("qualifications : "+qual+"\n")
        f.write("post : "+post+"\n")
        f.write("shift : "+shift+"\n")
        f.close()
    elif trans_ch == 2:
        f=open("water_staff.txt",'a')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("DOJ : "+doj+"\n")
        f.write("qualifications : "+qual+"\n")
        f.write("post : "+post+"\n")
        f.write("shift : "+shift+"\n")
        f.close()
    elif trans_ch == 3:
        f=open("rail_staff.txt",'a')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("DOJ : "+doj+"\n")
        f.write("qualifications : "+qual+"\n")
        f.write("post : "+post+"\n")
        f.write("shift : "+shift+"\n")
        f.close()


def append_details_client(trans_ch):
    name=str(input("ENTER YOUR NAME : "))
    adhaar=int(input("ENTER YOUR ADHAAR NUMBER : "))
    address=str(input("ENTER YOUR PERMANENT ADDRESS : "))
    city=str(input("ENTER NAME OF YOUR CITY : "))
    state=str(input("ENTER NAME OF YOUR STATE : "))
    contact=int(input("ENTER YOUR CONTACT NUMBER : "))
    dob=input("ENTER YOUR DOB  IN DD/MM/YYYY : ")
    tra_from=str(input("ENTER NAME OF CITY YOU ARE TRAVELLING FROM : "))
    tra_to=str(input("ENTER NAME OF CITY YOU ARE TRAVELLING TO : "))
    booking_date=input("ENTER YOUR BOOKING DATE IN FORMATE OF 'DD/MM/YY' : ")
    print("")
    if trans_ch == 1:
        f=open("air_client.txt",'a')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("travelling from : "+tra_from+"\n")
        f.write("travellin to : "+tra_to+"\n")
        f.write("booking date : "+booking_date+"\n")
        f.close()
    elif trans_ch == 2:
        f=open("water_client.txt",'a')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("travelling from : "+tra_from+"\n")
        f.write("travellin to : "+tra_to+"\n")
        f.write("booking date : "+booking_date+"\n")
        f.close()
    elif trans_ch == 3:
        f=open("rail_client.txt",'a')
        f.write("Name : "+name+"\n")
        f.write("adhaar : "+str(adhaar)+"\n")
        f.write("address : "+address+"\n")
        f.write("city : "+city+"\n")
        f.write("state : "+state+"\n")
        f.write("contact : "+str(contact)+"\n")
        f.write("DOB : "+dob+"\n")
        f.write("travelling from : "+tra_from+"\n")
        f.write("travellin to : "+tra_to+"\n")
        f.write("booking date : "+booking_date+"\n")
        f.close()


def copy_details(trans_ch, ch):
    if ch == 1:
        if trans_ch == 1:
                f=open("air_staff.txt",'r')
                temp=f.read()
                f.close()
                f=open("air_staff_copy.txt",'w')
                f.write(temp)
                f.close()
                f=open("air_staff_copy.txt",'r')
                print(f.read())
                f.close()
        elif trans_ch ==2:
                f=open("water_staff.txt",'r')
                temp=f.read()
                f.close()
                f=open("water_staff_copy.txt",'w')
                f.write(temp)
                f.close()
                f=open("water_staff_copy,txt",'r')
                print(f.read())
                f.close()
        elif trans_ch ==3:
                f=open("rail_staff.txt",'r')
                temp=f.read()
                f.close()
                f=open("rail_staff_copy,txt",'w')
                f.write(temp)
                f.close()
                f=open("rail_staff_copy.txt",'r')
                print(f.read())
                f.close()
    elif ch == 2:
        if trans_ch == 1:
                f=open("air_client.txt",'r')
                temp=f.read()
                f.close()
                f=open("air_client_copy.txt",'w')
                f.write(temp)
                f.close()
                f=open("air_client_copy.txt",'r')
                print(f.read())
                f.close()
        elif trans_ch ==2:
                f=open("water_client.txt",'r')
                temp=f.read()
                f.close()
                f=open("water_client_copy.txt",'w')
                f.write(temp)
                f.close()
                f=open("water_client_copy,txt",'r')
                print(f.read())
                f.close()
        elif trans_ch ==3:
                f=open("rail_client.txt",'r')
                temp=f.read()
                f.close()
                f=open("rail_client_copy,txt",'w')
                f.write(temp)
                f.close()
                f=open("rail_client_copy.txt",'r')
                print(f.read())
                f.close()


def delete_details(trans_ch, ch):
    if ch == 1:
        if trans_ch == 1:
            f=open("air_staff.txt",'w')
            f.close()
        elif trans_ch ==2:
            f=open("water_staff.txt","w")
            f.close()
        elif trans_ch ==3:
            f=open("rail_staff.txt","w")
            f.close()
    elif ch==2:
        if trans_ch ==1:
            f=open("air_client.txt","w")
            f.close()
        elif trans_ch ==2:
            f=open("water_client.txt","w")
            f.close()
        elif trans_ch ==3:
            f=open("rail_client.txt","w")
            f.close()




def password_admin(ps):
    admin = 'admin'
    if ps == admin:
        return 1
    else:
        return  0


def password_staff(ps):
    staff = 'staff'
    if ps == staff:
        return 1
    else:
        return  0

print()
print()
print("\t\t\tWELCOME  TO  GEETRATANAK TRAVELS")

print("\t\t\t        TOUR & TRAVELLERS")
print()
print()
ch=(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPRESS ENTER KEY_"))
while(True):
    print()
    print()
    print("1. AIRWAYS")
    print("2. WATERWAYS") 
    print("3. RAILWAYS")
    print("0. EXIT")
    trans_ch=int(input("ENTER YOUR CHOICE: "))
    print("\n")
    if trans_ch==1:
        while(True):
            print()
            print()
            print("1. ADMIN")
            print("2. USER")
            print("0. EXIT")
            air_ch=int(input("ENTER YOUR CHOICE: "))
            print("\n")
            if air_ch==1:
                ps = input("Enter the password : ")
                res = password_admin(ps)
                if res == 0:
                    exit("Invalid Password")
                while(True):
                    print()
                    print()
                    print("1. STAFF DETAILS")
                    print("2. CLIENT DETAILS")
                    print("0. EXIT")
                    air_admin=int(input("ENTER YOUR CHOICE: "))
                    print("\n")
                    if air_admin==1:
                        while(True):
                            print()
                            print()
                            print("STAFF DETAILS")
                            print("1. WRITE SOME DETAILS")
                            print("2. READ COMPLETE DETAILS")
                            print("3. COPY DETAILS")
                            print("4. SEARCH DETAILS")
                            print("5. DELETE DETAILS")
                            print("0. EXIT")
                            air_admin_staff=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if air_admin_staff == 1:
                                write_details_staff(trans_ch)
                            elif air_admin_staff == 2:
                                read_details_staff(trans_ch)
                            elif air_admin_staff == 3:
                                copy_details(trans_ch, air_ch)
                            elif air_admin_staff == 4:
                                search_details_staff(trans_ch)
                            elif air_admin_staff == 5:
                                delete_details(trans_ch, air_ch)
                            else:
                                break
                    elif air_admin==2:
                        while(True):
                            print()
                            print()
                            print("CLIENT DETAILS")
                            print("1. WRITE SOME DETAILS")
                            print("2. READ COMPLETE DETAILS")
                            print("3. COPY DETAILS")
                            print("4. SEARCH DETAILS")
                            print("5. DELETE DETAILS")
                            print("0. EXIT")
                            air_admin_client=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if air_admin_client == 1:
                                write_details_client(trans_ch)
                            elif air_admin_client == 2:
                                read_details_client(trans_ch)
                            elif air_admin_client == 3:
                                copy_details(trans_ch, air_ch)
                            elif air_admin_client == 4:
                                search_details_client(trans_ch)
                            elif air_admin_client == 5:
                                delete_details(trans_ch, air_ch)
                            else:
                                break
                    else:
                        break
            elif air_ch==2:
                while(True):
                    print()
                    print()
                    print("1. STAFF ")
                    print("2. CLIENTS")
                    print("0. EXIT")
                    air_user=int(input("ENTER YOUR CHOICE: "))
                    print("\n")
                    if air_user==1:
                        ps = input("Enter the password : ")
                        res = password_staff(ps)
                        if res == 0:
                            exit("Invalid Password")
                        while(True):
                            print()
                            print()
                            print("STAFF ")
                            print("press 1 to enter personal details")
                            print("0. EXIT")
                            air_user_staff= int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if air_user_staff == 1:
                                append_details_staff(trans_ch)
                            else:
                                break
                    elif air_user==2:
                        while(True):
                            print()
                            print()
                            print("USER ")
                            print("press 1 to start booking")
                            print("0. EXIT")
                            air_user_client=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if air_user_client == 1:
                                append_details_client(trans_ch)
                            else:
                                break
                    else:
                        break
            else:
                break
    elif trans_ch==2:
        while(True):
            print()
            print()
            print("1. ADMIN")
            print("2. USER")
            print("0. EXIT")
            water_ch=int(input("ENTER YOUR CHOICE: "))
            print("\n")
            if water_ch==1:
                ps = input("Enter the password : ")
                res = password_admin(ps)
                if res == 0:
                    exit("Invalid Password")
                while(True):
                    print()
                    print()
                    print("1. STAFF DETAILS")
                    print("2. CLIENT DETAILS")
                    print("0. EXIT")
                    water_admin=int(input("ENTER YOUR CHOICE: "))
                    print("\n")
                    if water_admin==1:
                        while(True):
                            print()
                            print()
                            print("STAFF DETAILS")
                            print("1. WRITE SOME DETAILS")
                            print("2. READ COMPLETE DETAILS")
                            print("3. COPY DETAILS")
                            print("4. SEARCH DETAILS")
                            print("5. DELETE DETAILS")
                            print("0. EXIT")
                            water_admin_staff=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if water_admin_staff == 1:
                                write_details_staff(trans_ch)
                            elif water_admin_staff == 2:
                                read_details_staff(trans_ch)
                            elif water_admin_staff == 3:
                                copy_details(trans_ch, water_ch)
                            elif water_admin_staff == 4:
                                search_details_staff(trans_ch)
                            elif water_admin_staff == 5:
                                delete_details(trans_ch, water_ch)
                            else:
                                break
                    elif water_admin==2:
                        while(True):
                            print()
                            print()
                            print("CLIENT DETAILS")
                            print("1. WRITE SOME DETAILS")
                            print("2. READ COMPLETE DETAILS")
                            print("3. COPY DETAILS")
                            print("4. SEARCH DETAILS")
                            print("5. DELETE DETAILS")
                            print("0. EXIT")
                            water_admin_client=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if water_admin_client == 1:
                                write_details_client(trans_ch)
                            elif water_admin_client == 2:
                                read_details_client(trans_ch)
                            elif water_admin_client == 3:
                                copy_details(trans_ch, water_ch)
                            elif water_admin_client == 4:
                                search_details_client(trans_ch)
                            elif water_admin_client == 5:
                                delete_details(trans_ch, water_ch)
                            else:
                                break
                        else:
                            break
            elif water_ch==2:
                while(True):
                    print()
                    print()
                    print("1. STAFF ")
                    print("2. CLIENTS")
                    print("0. EXIT")
                    water_user=int(input("ENTER YOUR CHOICE: "))
                    print("\n")
                    if water_user==1:
                        ps = input("Enter the password : ")
                        res = password_staff(ps)
                        if res == 0:
                            exit("Invalid Password")
                        while(True):
                            print()
                            print()
                            print("STAFF ")
                            print("press 1 to enter personal details")
                            print("0. EXIT")
                            water_user_staff=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if water_user_staff == 1:
                                append_details_staff(trans_ch)
                            else:
                                break
                    elif water_user==2:
                        while(True):
                            print()
                            print()
                            print("USER ")
                            print("press 1 to start booking")
                            print("0. EXIT")
                            water_user_client=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if water_user_client == 1:
                                append_details_client(trans_ch)
                            else:
                                break
                    else:
                        break
            else:
                break
    elif trans_ch==3:
        while(True):
            print()
            print()
            print("1. ADMIN")
            print("2. USER")
            print("0. EXIT")
            rail_ch=int(input("ENTER YOUR CHOICE: "))
            print("\n")
            if rail_ch==1:
                ps = input("Enter the password : ")
                res = password_admin(ps)
                if res == 0:
                    exit("Invalid Password")
                while(True):
                    print()
                    print()
                    print("1. STAFF DETAILS")
                    print("2. CLIENT DETAILS")
                    print("0. EXIT")
                    rail_admin=int(input("ENTER YOUR CHOICE: "))
                    print("\n")
                    if rail_admin==1:
                        while(True):
                            print()
                            print()
                            print("STAFF DETAILS")
                            print("1. WRITE SOME DETAILS")
                            print("2. READ COMPLETE DETAILS")
                            print("3. COPY DETAILS")
                            print("4. SEARCH DETAILS")
                            print("5. DELETE DETAILS")
                            print("0. EXIT")
                            rail_admin_staff=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if rail_admin_staff == 1:
                                write_details_staff(trans_ch)
                            elif rail_admin_staff == 2:
                                read_details_staff(trans_ch)
                            elif rail_admin_staff == 3:
                                copy_details(trans_ch, rail_ch)
                            elif rail_admin_staff == 4:
                                search_details_staff(trans_ch)
                            elif water_admin_staff == 5:
                                delete_details(trans_ch, rail_ch)
                            else:
                                break
                    elif rail_admin==2:
                        while(True):
                            print()
                            print()
                            print("CLIENT DETAILS")
                            print("1. WRITE SOME DETAILS")
                            print("2. READ COMPLETE DETAILS")
                            print("3. COPY DETAILS")
                            print("4. SEARCH DETAILS")
                            print("5. DELETE DETAILS")
                            print("0. EXIT")
                            rail_admin_client=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if rail_admin_client == 1:
                                write_details_client(trans_ch)
                            elif rail_admin_client == 2:
                                read_details_client(trans_ch)
                            elif rail_admin_client == 3:
                                copy_details(trans_ch, rail_ch)
                            elif rail_admin_client == 4:
                                search_details_client(trans_ch)
                            elif rail_admin_client == 5:
                                delete_details(trans_ch, rail_ch)
                            else:
                                break
                    else:
                        break
            elif rail_ch==2:
                while(True):
                    print()
                    print()
                    print("1. STAFF ")
                    print("2. CLIENTS")
                    print("0. EXIT")
                    rail_user=int(input("ENTER YOUR CHOICE: "))
                    print("\n")
                    if rail_user==1:
                        ps = input("Enter the password : ")
                        res = password_staff(ps)
                        if res == 0:
                            exit("Invalid Password")
                        while(True):
                            print()
                            print()
                            print("STAFF ")
                            print("press 1 to enter personal details")
                            print("0. EXIT")
                            rail_user_staff=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if rail_user_staff == 1:
                                append_details_staff(trans_ch)
                            else:
                                break
                    elif rail_user==2:
                        while(True):
                            print()
                            print()
                            print("USER ")
                            print("press 1 to start booking")
                            print("0. EXIT")
                            rail_user_client=int(input("ENTER YOUR CHOICE: "))
                            print("\n")
                            if rail_user_client == 1:
                                append_details_client(trans_ch)
                            else:
                                break
                    else:
                         break
            else:
                break
    else:
        break
