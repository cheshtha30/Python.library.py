import mysql.connector as sq

cn=sq.connect(host="localhost", user="root",passwd="root",database="travel")

cur=cn.cursor(prepared=True)
ch='y'

print(""" 

  --------------------------------------------------------------
 |==============================================================| 
 |============ Welcome To Library Management System	========|
 |==============================================================|
  --------------------------------------------------------------

 """)


while ch=="y":
    print("Please Seclect an option")
    print("1. Customer")
    print("2. Book")
    print("3. Issue")
    print("4. Return")
    print("5 Exit")
    ch1=int(input ("\t\t\tenter a choice"))
    while ch1>=1 and ch1<=5:
        if(ch1==1):
            print("\n\t\t\t1. Add New Customer")
            print("\t\t\t2. Delete a customer")
            print("\t\t\t3. Modify a value in Customer")
            print("\t\t\t4. Display a Customer")
            print("\t\t\t5. Move to main")
            ch11=int(input("\t\t\tEnter your choice"))
            if ch11==1:
                a=input("\n\t\t\tEnter the customer name")
                b=input("\t\t\tEnter the customer id")
                c=input("\t\t\tEnter the customer phone number")
                d=input("\t\t\tEnter the customer age")   
                t=(a,b,c,d)
                s='''Insert into CUSTOMER values(%s,%s,%s,%s)'''
                cur.execute(s,t)
                cn.commit()
                print(cur.rowcount,"Record Inserted")
                cur.execute("SELECT* FROM CUSTOMER")
                #cur=cn.fetchall()
                for x in cur:
                    print(x,end=" | ")
                #print("Record Insrted")
            elif ch11==2:
                a=input("Enter the User ID to be deleted")
                t=(a,)
                s='''Delete from customer where co_id=%s'''
                print(s)
                cur.execute(s,t)    
                cn.commit()
                print(cur.rowcount,"Deleted")
            elif ch11==3:
                cur.execute("Select * from customer")    
                a=input("Enter the customer code which has to be changed")
                b=input ("Enter the new phone number ")
                               
                s="UPDATE table_customer SET phonenumber=%s where co_id=%s"
                t=(a,b)
                cur.execute(s,t)
                cn.commit()
            elif ch11==4:
                c=[]
                a=input("\t\t\tEnter the customer id")
                t=(a,)
                s="Select * from CUSTOMER where co_id=%s"
                cur.execute(s,t)
                c.append(cur.fetchone())
                for x in list(c):
                    print(x)                 
            elif ch11==5:
                break
        elif(ch1==2):
            print("\n\t\t\t1. Add New Book")
            print("\t\t\t2. Delete a Book")
            print("\t\t\t3. Modify a value in Book")
            print("\t\t\t4. Display Books")
            print("\t\t\t5. move to main")
            ch21=int(input("Enter your choice"))
            if ch21==1:
                a=input("\t\t\tEnter the book code")
                b=input("\t\t\tEnter the book name")
                c=input("\t\t\tEnter the book price")
                d=input("\t\t\tEnter the book Author Name")
                e=input("\t\t\tEnter the book Publisher Name")
                t=(a,b,c,d,e)
                s='''Insert into BOOK values(%s,%s,%s,%s,%s)'''
                cur.execute(s,t)
                cn.commit()
                print(cur.rowcount,"Record Inserted")
                print("Record Insrted- Book")
            elif ch21==2:
                a=input("Enter the book code")
                s="delete from BOOK where bno=%s"
                t=(a,)
                cur.execute(s,t)
                print(cur.rowcount,"Record deleted")
                print("Record Deleted- Book")
            elif ch21==3:
                cur.execute("Select * from BOOK")     
                a=input("Enter the book code")
                b=input ("Enter the price")
                               
                s="UPDATE table_Book SET price=%s where bno=%s"
                t=(a,b)
                cur.execute(s,t)
                cn.commit()
            elif ch21==4:
                a=input("Enter the book code")
                s="Select * from BOOK where bno=%s"
                t=(a,)
                cur.execute(s,t)    
                for x in list(cur):
                    print(x)   
            elif ch21==5:
                break
        elif(ch1==3):
            print("\t\t\tIssue a Book")
            a=input("\n\t\t\tEnter the issue number")
            b=input("\t\t\tEnter the book number")
            c=input("\t\t\tEnter the customer id")
            d=input("\t\t\tEnter the date of issue")
            e=input("\t\t\tEnter the date of return")

            s='''Insert into issue values(%s,%s,%s,%s,%s)'''
            t=(a,b,c,d,e)          
            cur.execute(s,t)
            cn.commit()
            print(cur.rowcount,"Record Inserted")
            print("Record Insrted- issue")
        elif(ch1==5):
            print ("Exiting")
            exit()
            ch=input ("Do you want to continue")
