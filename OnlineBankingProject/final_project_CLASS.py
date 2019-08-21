
class Bank(object):
    
    accountList=[]
    def display(self):
        for account in Bank.accountList:
            print ("*********************")
            for k,v in account.options.items():
                print ('{}: {}'.format(k,v))
            print ("*********************")

    def login_validity(self, u, p):
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return True
        return False

    def load_account(self,u, p):
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return account #account object
        return None #no object found
    
    
        
class Account(object):
    default_options = {'accountno':None,'acctype': None, \
               'balance': 0, 'fname': None, 'lname': None, 'line1':None, \
                       'line2': None, 'username': None, 'pin': None}
    def __init__(self, **kwargs):
        self.options = Account.default_options.copy()
        self.options.update(kwargs)
        Bank.accountList.append(self)

    def __getitem__(self, key): #get an item by key
        return self.options[key]
    def __setitem__(self, key, new_value): #set an item by key
        self.options[key] = new_value
        
    def getBalance(self, accno):
        if accno == self['accountno'] :
                return self['balance']
 
    
        
    def deposit(self, amount_to_deposit, accno):
        if accno == self['accountno'] :
                self['balance']+= int(amount_to_deposit)

    def summary(self, accno):
        if accno == self['accountno'] :
                name = self['fname'] + ' ' +self['lname']
                address = self['line1'] + ' ' + self['line2']                
                return (name, address, self['acctype'], self['balance'])
 
        
class Saving(Account):

    withdraw_charge = 2.53
        
    def withdraw(self, amount_to_withdraw, accno):
            if accno == self['accountno'] :
                self['balance']=self['balance'] - int(amount_to_withdraw) \
                                 - Saving.withdraw_charge

class Checking(Account):
    
    withdraw_charge = 1.00

    def withdraw(self, amount_to_withdraw, accno):
            if accno == self['accountno'] :
                self['balance']=self['balance'] - int(amount_to_withdraw) \
                                 - Saving.withdraw_charge

#testing code
b = Bank()

print ('*****c ****')
d = {'fname' : 'Irina', 'lname': 'hashmi', 'balance': 200}
c = Checking(**d)
print(c.options['fname'])
c.withdraw(100, c.options['accountno'])
print(c.options['balance'])
#c.deposit(1000)
#print(c.options['balance'])




print ('*****s ****')
d = {'fname' : 'Jane', 'lname' : 'Jo', 'balance' : 100}

s = Saving(**d)
print(s.options['fname'])
#s.withdraw(40)
#print(s.options['balance'])
#s.deposit(1000)
#print(s.options['balance'])


b.display()

  

        

    
    
    
