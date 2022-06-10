class Account:
    def __init__(self,accountname,accountnumber,):
        self.accountname=accountname
        self.accountnumber=accountnumber
        self.balance=0
        self.deposites=[]
        self.withdrals=[]
        self.transaction=100

        
       
    def deposite(self,amount):
         if amount <=200:
            return f"your withdrwal should be greater than 0"
         elif amount>self.balance:
            return f"your ballance is {self.balance} you cant withdraw {amount}"
         else:
            self.balance=-amount
            self.withdrals.append(amount)

            return f"hello {self.accountname} you have withdrwan {amount}. and your new balance is {self.balace}" 
  
    def withdwal(self,amount):
      if amount <=200:
            return f"your withdrwal should be greater than 0"
      elif amount>self.balance:
            return f"your ballance is {self.balance} you cant withdraw {amount}"
      else:
        self.balance-=amount+self.transaction
        self.deposites.append(amount)
      return f"hello {self.accountname} you have withdrwan {amount}. and your new balance is {self.balace}"
    

    # Add a new method called deposits_statement which using a for loop prints each deposit in a new line
    def deposite_statements(self):
      for x in self.deposites: 
        print(x,end="\n")
           
    #  Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line       
            
    def withdrals_statement(self):
        for i in self.withdrals:
            print(i,end="\n")

# Modify the withdrawal method to include a transaction fee of 100 per transaction.
     
    #   Add a method to show the current balance      
    def current_balance(self):
        balance=self.balance
        print(balance)


        



        



        