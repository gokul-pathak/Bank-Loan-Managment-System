def clr():#to clear the consol
    import os
    clear = lambda : os.system('cls')
    clear()
import time #to hold or sleep screen for a some time
def intro():#intro customer and admin main menu
    print("\t\t\t\t______________________")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t______________________")

def adminintro():#intro for admin menu
    print("\t\t\t\t______________________")
    print("\t\t\t\tWelcome to admin panel")
    print("\t\t\t\t______________________")
#starting for new customer function--------------------------------------------------------------------------------------
def loan_details():
    import time
    while True:
        clr()
        intro()
        print("\n\n\n_____________LOAN DETAILS MENU______________")
        print("\tLoan Types choose according to your needs!!!")
        print("\t1.Education loan")
        print("\t2.Car loan")
        print("\t3.Home loan")
        print("\t4.Personal loan")
        print("\t5.Go back")
        print("\t:)")
        choice=int(input("\tPlease select your Loan Type: "))
        if choice == 1:
            clr()
            print("\n\n\n_____________Education Loan Details______________")
            print("\n\tMinimum Balance Required: 0")
            print("\n\tRate of interest: 2%")
            print("\tWait loading......")
            time.sleep(8)
            loan_details()
            break
            
        elif choice == 2:
            clr()
            print("\n\n\n_____________Car Loan Details______________")
            print("\n\tMinimum Balance Required: upto 50000")
            print("\n\tRate of interest: 5%")
            print("\n\tTo return back press 0:")
            print("\tWait loading......")
            time.sleep(8)
            loan_details()
            break
        elif choice == 3:
            clr()
            print("\n\n\n_____________Home Loan Details______________")
            print("\n\tMinimum Balance Required: Upto 100000")
            print("\n\tRate of interest: 3.5%")
            print("\tWait loading......")
            time.sleep(8)
            loan_details()
            break
        elif choice == 4:
            clr()
            print("\n\n\n_____________Personal Loan Details______________")
            print("\n\tMinimum Balance Required: upto 200000")
            print("\n\tRate of interest: 4.5%")
            print("\tWait loading......")
            time.sleep(8)
            loan_details()
            break
        elif choice ==5:
            print("\tWait loading......")
            time.sleep(1)
            clr()
            intro()
            new_customer()
            break  
        else:
            print("\tInvalid Selection please choose [1-4]")
            print("\tWait loading......")
            time.sleep(1)
            break

def loan_calculator():#calculator for loan calculation payment
    while True:
        clr()
        intro()
        print("<\n\n\n_______________Loan calculator_______________>")
        A=input("How much loan amount will you borrow?")
        A=float(A)
        print("Your loan amount is: RS")
        print(A)

        N=input("For how many years will you use this amount?")
        N=float(N)*12
        #print("Your years is: ")
        print(N)

        R=input("what is the interest rate that you will be paying?Enter as for eg. 10%=10 or n%=n etc.")
        R=float(R)/100
        print("Your rate of interest is: ")
        print(R) 
        T=(A/N)+R*(A/N)

        float(T)
        print("Your montly payment is: RS ")
        print(T)
        print("Do you want to continue press '1' to continue and '2' to exit")
        choice = int(input())
        if choice == 1:
            clr()
            intro()
            loan_calculator()
            break
        elif choice == 2:
            print("\tThanks for using our application!!!")
            clr()
            intro()
            new_customer()
            break
        else:
            print("Invalid selection!!!")
            print("Thanks for visiting!!!")
def registration():#registration function for new customer
    clr()
    intro()
    g=[]
    print("\n\n_________________Loan Demand form_______________\n")
    print("\t<Enter your details below>")
    fname=input("Enter your Full name: ")
    g.append(fname)

    gender=input("Enter your Gender: ")
    g.append(gender)

    address=input("Enter your Address: ")
    g.append(address)

    mobile=input("Enter your contact no.: ")
    g.append(mobile)

    email=input("Enter your E-mail.: ")
    g.append(email)

    cn=input("Enter your citizenship number.: ")
    g.append(cn)
    
    loantype=input("Enter your loan type (EL/CL/HL/PL).: ")
    g.append(loantype)

    lm=input("Enter the total loan amount?")
    g.append(lm)

    lterms=input("Enter your loan term (years).: ")
    g.append(lterms)

    ia=input("Enter your Instalment Amount.: ")
    g.append(ia)

    username=input("Enter a username for your account: ")
    g.append(username)
    while True:
        passw=input("Create new password for your account(please remember your password).: ")
        rp=input("confirm your password.: ")
        if(passw == rp and passw != " "):
            print("\tPassword matched!!")
            g.append(rp)
            c="N"
            g.append(c)
            break
        else:
            print("\tPassword did not match please try again later!!")
            print("\tWait loading......")
            wait3()
            intro()
    print(g)
    print("Check your data if data is correct type 1 and if not type 0 then enter: ")
    choice = int(input())
    if choice == 1:
        print("Your data is saved: ")
        print("Your account created successfully!!!: ")
        import random
        p=[]
        f=open("newc.txt","a")
        for i in range(1):
            r=random.randint(101,150)
            if r not in p: p.append(r)
            f.write((str(r))+" ")
            f.close()
        print("****please remember your id****")
        print("|Your id is|",r)
        time.sleep(3)
    if choice == 0:
        clr()
        g.clear()
        print("Your data is erased successfully!!!: ")
        print("\tWait loading......")
        time.sleep(3)
        intro()
        registration()
    return g

def savefiler():#to save the details about customer from the registration function
    p=registration()
    f=open("newc.txt","a")
    for i in range(len(p)):
        f.write(p[i]+" ")
    f.close()
    g=open("newc.txt","a")
    t=time.strftime("%d/%m/%Y")
    g.write((str(t))+" ")
    g.write("\n")
    g.close()
    print("\tWait loading......")
    time.sleep(3)
    clr()
    intro()
    new_customer()
def new_customer():#new customer menu of the bank
    while True:
        clr()
        intro()
        print("\tSelect Services which you want!!")
        print("\t1.Check Loan Details")
        print("\t2.Use Loan Calculator")
        print("\t3.Registration")
        print("\t4.Go back")
        choice=int(input("\tplease select your choice: "))
        if choice == 1:
            loan_details()
            break
        elif choice == 2:
            loan_calculator()
            break
        elif choice == 3:
            savefiler()
            break

        elif choice == 4:
            print("\tThanks for using our system!!")
            print("\tWait loading......")
            time.sleep(1)
            clr()
            intro()
            menu()
            break
        else:
            print("\tInvalid Selection please choose [1-4]")
            print("\tWait loading......")
            time.sleep(1)
'''
ending of New customer function...
----------------------------------------------------------------------------------------------------------------------
Starting Admin function
'''
def loan_el(a,m):#details loan for the registered customer
    print("\n\n\n_____________Your loan Details______________")
    print("\n\tMinimum Balance Required: 0")
    print("\n\tRate of interest: 2%")
    print("data will display for only 8 second")
    time.sleep(2)
    customer_menu(a, m)
    return

def loan_cl(a,m):
    print("\n\n\n_____________Your Loan Details______________")
    print("\n\tMinimum Balance Required: upto 50000")
    print("\n\tRate of interest: 5%")
    print("data will display for only 8 second")
    time.sleep(2)
    customer_menu(a, m)
    return

def loan_hl(a,m):
    print("\n\n\n_____________Your Loan Details______________")
    print("\n\tMinimum Balance Required: Upto 100000")
    print("\n\tRate of interest: 3.5%")
    print("data will display for only 8 second")
    time.sleep(2)
    customer_menu(a, m)
    return

def loan_pl(a,m):
    print("\n\n\n_____________Your Loan Details______________")
    print("\n\tMinimum Balance Required: upto 200000")
    print("\n\tRate of interest: 4.5%")
    print("data will display for only 8 second")
    time.sleep(2)
    customer_menu(a, m)
    return
    
def approv_newc():#approving new customer from admin function
    clr()
    import time
    print("Approve new customer from pending requst lists\n\n")
    det=open("newc.txt","rt")
    for t in det:
       print(t)
    det.close()

    fin=open("newc.txt","rt")
    fout=open("registeredc.txt","at")
    name=input("Enter user name to make registered user: ")
    check=False
    for i in fin:
        for j in i.split():
            if j==name:
                check=True
        if check==True:
            a=i.replace("N","R")
            fout.writelines(a)
            fin.close()
            fout.close()
            l=open("loanamount.txt","at")
            print("Enter the user id ")
            ld=int(input())
            l.write((str(ld))+" ")
            print("Enter the provided total loan amount")
            rm=int(input())
            l.write(str(rm))
            l.write("\n")
            l.close()
            print("User Verified Successfully \n balance transfered to account")
            time.sleep(1)
            print("\tWait loading......")
            time.sleep(4)
            break
    else:
        print("User not found!!")
        print("\tWait loading......")
        time.sleep(1)
    clr()
    adminintro()
    admin_menu()


def view_cust():#view customer from function of admin menu
    clr()
    file1=open("registeredc.txt","r")
    print("<-All verified customer are listed below:)->\n\n")
    for f in file1:
        print(f)
    file1.close()
    print("\tWait loading......\n\n\n\n\twait for 8 sec")
    time.sleep(8)
    clr()
    admin_menu()

def view_ltype():#view customer by loan type function of admin
    print("Please enter the loan type: ")
    b=input()
    f=open("registeredc.txt","r")
    for i in f:
        for j in i.split():
            if(j==b):
                print(i)
                break
    f.close()
    print("data will be displayed for 8 sec only")
    time.sleep(8)
    clr()
    adminintro()
    admin_menu()


def cust_transid():# to view customer transaction by id from the admin menu
        f=open("history.txt","r")
        print("Please enter the valid customer id: ")
        a=input()
        print("ID     Amount    Date")
        print("--     ------    ----\n")
        for i in f:
            for j in i.split():
                if (j==a):
                    print(i)
        f.close()
        print("data will be displayed for 8 sec only")
        time.sleep(2)
        clr()
        adminintro()
        admin_menu()
def view_alltrans():#view all transaction of all customer from admin function
    clr()
    print("all transaction of all customer is given below")
    print("ID     Amount    Date")
    print("--     ------    ----\n")
    fil=open("history.txt","r")
    for i in fil:
        print(i)
    fil.close()
    print("data will be displayed for 8 sec only")
    time.sleep(8)
    clr()
    adminintro()
    admin_menu()

def admin_menu():#admin main menu
    while True:
        clr()
        adminintro()
        print("\t1.Registration requst approv new customer")
        print("\t2.View all customer(Verified)")
        print("\t3.View customer by loan type")
        print("\t4.View transaction by id")
        print("\t5.View all transaction")
        print("\t6.coming soon")
        print("\t7.Go back")
        choice=int(input("Which option do you want to choose: "))
        if(choice==1):
            approv_newc()
            break
        elif(choice==2):
            view_cust()
            break
        elif(choice==3):
            view_ltype()
            break
        elif(choice==4):
            cust_transid()
            break
        elif(choice==5):
            view_alltrans()
            break
        elif(choice==6):
            break
        elif(choice==7):
            clr()
            menu()
            break
        else:
            print("Invalid option please enter valid input!!!")
            wait()
#admin main menu ending

def admin_auth():#admin log in process
    while True: 
        clr()
        intro()
        print("___Admin log in process__")
        username="admin"
        password="nepal123"
        a=input("Enter username: ")
        b=input("Enter password: ")
        if(username == a and password == b):
            admin_menu()
            break
        else:
            clr()
            print("Data could not match!!!\nPlease try again later!!")
            time.sleep(3)
        print("Do you want to continue y-yes and n-no?")
        choice=input()
        if choice=="y":
            continue
        else:
            menu()
            break
        #ending of admin log in process
#ending of admin menu function........................................................................
'''


-----------------------------------------------------------------------------------------------------------------
Registered customer function starting
'''
#starting of Registered customer function
def view_loan(a,m):
    clr()
    intro()
    f=open("registeredc.txt","rt")
    b=False
    for i in f:
        for j in i.split():
            if j==m:
                b=True
            if b==True:
                if j=="EL":
                    loan_el(a,m)
                    return
                elif j=="PL":
                    loan_pl(a,m)
                    return
                elif j=="CL":
                    loan_cl(a,m)
                    return
                elif j=="HL":
                    loan_hl(a,m)
                    return
    f.close()
def view_det(a,m):#to view profile of customer
    clr()
    intro()
    print("Your details are given below",a)
    file1=open("registeredc.txt","r")
    for i in file1:
        for j in i.split():
            if(m==j):
                print(i)
    file1.close()            
    print("data will be displayed for 8 sec only")
    time.sleep(8)
    clr()
    customer_menu(a, m)
def trans_history(m,am):#view transaction fo customer
    f=open("history.txt","a")
    t=time.strftime("%d/%m/%Y")
    f.write(str(m)+" ")
    f.write(str(am)+" ")
    f.write((str(t))+"\n")
    print("Transaction successfull")
    time.sleep(2)
    f.close()

def paybal(a,m):#to pay installment amount
    print("<-Amount payment->")
    print("Enter the amount ")
    am=int(input())
    f2=open("loanamount.txt","r")
    check=False
    g=0
    bal=0
    for i in f2:
        count=0
        for j in i.split():
            count = count+1
            if j==m:
                check = True
            if check==True:
                if count==2:
                    bal=int(j)
                    print(bal)
                    g=bal-am
                    print("Your remaining amount is ",g)
                    break
                    time.sleep(2)

    f2.close()
    f1=open("loanamount.txt","r")
    fg=f1.read()
    fg=fg.replace(str(bal),str(g))
    rr=open("loanamount.txt","w")
    rr.write(fg)
    rr.close()
    f1.close()
    print("done!")
    time.sleep(2)
    trans_history(m,am)
    print("\tWait loading......\n\n\nredirect to menu")
    time.sleep(3)
    clr()
    intro()
    customer_menu(a, m)

def view_trans(a,m):#to view own tranasaction of customer
    clr()
    gp=open("history.txt","r")
    print("ID     Amount    Date")
    print("--     ------    ----\n")
    for i in gp:
        for j in i.split():
            if(m==j):
                print(i)
    gp.close()
    print("data will be displayed for 8 sec only")
    time.sleep(8)
    clr()
    customer_menu(a, m)

def rem_amt(a,m):#to view remaining amount of customer to pay
    print("your remaining amount to pay is ",a)
    f=open("loanamount.txt","r")
    check=False
    for i in f:
        count=0
        for j in i.split():
            count=count+1
            if(m==j):
                check=True
            if(check==True):
                if count==2:
                    print(j)
                    print("data will be displayed for 8 sec only")
                    time.sleep(8)
                    clr()
                    customer_menu(a, m)
                    return
    f.close()

def customer_menu(a,m):# registered customer main menu
    while True:
        print("\n\tLog in success Welcome to customer menu!!",a)
        print("\n\tPay installment amount\t\t\t\t1")
        print("\n\tView transaction\t\t\t\t2")
        print("\n\tView own details\t\t\t\t3")
        print("\n\tView loan details\t\t\t\t4")
        print("\n\tView remaining amount to pay\t\t\t5")
        print("\n\tGo back\t\t\t\t\t\t6")
        print("\n\tWhich services do you want to choose?")
        ch=int(input())
        if (ch == 1):
            paybal(a,m)
            break
        elif(ch==2):
            view_trans(a,m)
            break
        elif(ch==3):
            view_det(a,m)
            break
        elif(ch==4):
            view_loan(a,m)
            break
        elif(ch==5):
            rem_amt(a,m)
            break

        elif(ch==6):
            print("\tWait loading......")
            time.sleep(1)
            clr()
            menu()
            break
        else:
            print("\n\tInvalid choice!!")

def registered_cust():#customer log in process
    clr()
    intro()
    print("Welcome to customer log in menu\n\nPlease be make sure enter details should be correct!!!\n")
    a=input("Enter your username: ")
    b=input("Enter your password: ")
    m=input("Enter your id provided by system admin: ")
    f=open("registeredc.txt","r")
    for i in f:
        count=0
        us=0
        pw=0
        R=0
        ld=0
        for j in i.split():
            if count==15:
                break
            if (j == a):
                us=1
            if (j == b):
                pw=1
            if(j == m):
                ld=1
            if (j =="R"):
                R=1
            count=count+1
        if us==1:
            break
    if (us==1 and pw==1 and R==1 and ld==1):
        print("<-Log in successfull->")
        print("\tWait loading......")
        time.sleep(1)
        clr()
        customer_menu(a,m)
    else:
        clr()
        intro()
        print("log in failed")
        print("Data could not found!!!")
        time.sleep(1)
        print("Do you want to continue y-yes and n-no?")
        choice=input()
        if(choice=='y'):
            clr()
            intro()
            registered_cust()
        else:
            clr()
            intro()
            menu()

#ending of registered customer function............................................................

'''
-----------------------------------------------------------------------------------------------------------------
Main menu or main funciton of the bank start
'''

def menu():#main menu for the bank
    while True:
        clr()
        intro()
        print("\t<-welcome to Malaysia Bank Online->")
        print("\t:)")
        print("\t---Main Menu---")
        print("\t1.Admin")
        print("\t2.New Customer")
        print("\t3.Registered Customer")
        print("\t4.Exit")
        print("\t:)")
        choice=int(input("Please choose the options [1-3]:"))
        if choice == 1:
            admin_auth()
            break
        elif choice == 2:
            new_customer()
            break
        elif choice == 3:
            registered_cust()
            break
        elif choice == 4:
            print("\tThanks for using our system!!")
            print("\tWait loading......")
            time.sleep(1)
            break
        else:
            print("\tInvalid Selection Please Enter [1-3]!!")
            print("\t:)")
            time.sleep(1)
#ending of main menu or function

clr()
print("\tWait loading......")
time.sleep(1)
print("\n\n\n\tDesigned by Gokul Pathak (NPI000095)")
time.sleep(2)
clr()
menu()#main function call
