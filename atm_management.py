import random
import mysql.connector as my


def init_db():
    return my.connect(host="localhost", user="root", password="root", database="atm")

def acct(an):
  db = init_db()
  cur= db.cursor()
  cur.execute("SELECT accounttype from atm_user where accountnumber = %s" %(an))
  b = cur.fetchone()
  u= b[0]
  return u

def bal(an):
  db = init_db()
  cur= db.cursor()
  cur.execute("SELECT balance from atm_user where accountnumber = %s" %(an))
  b = cur.fetchone()
  u= b[0]
  return u
  
def wd(an, amt):
  db = init_db()
  cur = db.cursor()
  
  if acct(an) == "savings":
    que= bal(an) - 5000
    if amt > bal(an) or bal(an) <= 5000 or amt > que:
      print("Minimun Account Balance should be 5000.")
    elif amt > 10000:
      print("Withdrawl Limit is 10,000 at a time.")
    else:
      namt = bal(an) - amt
      tid = random.randint(10000000, 99999999)
      cur.execute("UPDATE atm_user SET balance = %s WHERE accountnumber = %s" %(namt, an))
      cur.execute("INSERT INTO atm_transaction (accountnumber, type, amount, t_id) VALUES (%s, 'Debit', %s, %s)" %(an, amt, tid))
      print("Withdrawal Succesful, Remaining Balance: ", namt)
      db.commit()
      
      
  elif acct(an) == "credit":
    cur.execute("SELECT creditlimit from atm_user where accountnumber = %s" %(an))
    b = cur.fetchone()
    x = int(b[0])
    lim= bal(an) + x
    if amt > lim:
            print("Error, Credit Limit Exceeded")
    else:
            new_balance = bal(an) - amt
            tid = random.randint(10000000, 99999999)
            cur.execute("UPDATE atm_user SET balance = %s WHERE accountnumber = %s", (new_balance, an))
            cur.execute("INSERT INTO atm_transaction (accountnumber, type, amount, t_id) VALUES (%s, 'Debit', %s, %s)", (an, amt, tid))
            print("Withdrawal Successful, Remaining Balance: ", new_balance)
            db.commit()
            
  elif acct(an) == "current":
        if amt > bal(an):
            print("Error: Insufficient Funds in Current Account")
        else:
            new_balance = bal(an) - amt
            tid = random.randint(10000000, 99999999)
            cur.execute("UPDATE atm_user SET balance = %s WHERE accountnumber = %s", (new_balance, an))
            cur.execute("INSERT INTO atm_transaction (accountnumber, type, amount, t_id) VALUES (%s, 'Debit', %s, %s)", (an, amt, tid))
            print("Withdrawal Successful, Remaining Balance: ", new_balance)
            db.commit()
  else:
    print("Error: Unknown Account Type")

def dep(an, amt):
  db = init_db()
  cur = db.cursor()
  namt = bal(an) + amt
  tid = random.randint(10000000, 99999999)
  cur.execute("UPDATE atm_user SET balance = %s WHERE accountnumber = %s" %(namt, an))
  cur.execute("INSERT INTO atm_transaction (accountnumber, type, amount, t_id) VALUES (%s, 'Credit', %s, %s)", (an, amt, tid))
  print("Deposit Succesful, Current Balance: ", namt)
  db.commit()

def pin(an, pn):
  db = init_db()
  cur = db.cursor()
  cur.execute("UPDATE atm_user SET pin = %s WHERE accountnumber = %s" %(pn, an))
  print("Pin Updation Successful ")
  db.commit()

def mob(an, mn):
  db = init_db()
  cur = db.cursor()
  cur.execute("UPDATE atm_user SET mobno = %s WHERE accountnumber = %s" %(mn, an))
  print("Mobile Number Updation Successful ")
  db.commit()

def statement(an):
  db = init_db()
  cur = db.cursor()
  cur.execute("select * from atm_transaction WHERE accountnumber = %s" %(an))
  row = cur.rowcount
  s = cur.fetchmany(10)
  print("(Acc No., T_Type, Amt, T_Id)")
  for r in s:
    print(r)

  
def atm():
  print("Welcome to Vikish ATM!")
  
  while True:
    an= int(input("Enter your Accoumt Number: "))
    db = init_db()
    cur = db.cursor()
    cur.execute("SELECT accountholder from atm_user WHERE accountnumber = %s;" %(an))
    res = cur.fetchone()
    naam= res[0]
    if res:
      print("\nWelcome Back", naam, "!")
      break

  while True:
    p= int(input("\nEnter your Pin Number: "))
    db = init_db()
    cur = db.cursor()
    cur.execute("SELECT pin from atm_user WHERE accountnumber = %s;" %(an))
    pr = cur.fetchone()
    if p == pr[0]:
      break
    else:
      print("Wrong Pin!!!")
    
  while True:
     print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n=-=-=-= Vikish ATM Menu =-=-=-=\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
     print("(1) Check Balance")
     print("(2) Withdraw Money")
     print("(3) Deposit Money")
     print("(4) Update Pin")
     print("(5) Update Mobile Number")
     print("(6) Check Mini Statement")
     print("(7) Exit Menu")
     print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
     
     choice = input("Enter your choice: ")
     
     if choice == "1":
         print("Your Balance is: ", bal(an))
     elif choice == "2":
         print("Withdrawal Selected!")
         amt = int(input("Enter the Amount to Withdraw: "))
         wd(an, amt)

     elif choice == "3":
         print("Deposit Selected!")
         amt = int(input("Enter the Amount to Deposit: "))
         dep(an, amt)

     elif choice =="4":
          pn=int(input("Enter the New Pin: "))
          if pn < 100 or pn > 999:
            print("New Pin is Invalid")
          else:
            pin(an, pn)
            
     elif choice =="5":
          mn=int(input("Enter the New Mobile Number: "))
          if mn < 1000000000 or mn > 9999999999:
            print("New Number is Invalid")
          else:
            mob(an, mn)
      
     elif choice == "6":
         statement(an)

     elif choice == "7":
         print("Exiting...")
         break
     else:
         print("Invalid choice. Please try again.")
         
atm()         