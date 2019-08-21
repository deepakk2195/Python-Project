from tkinter import *
from final_project_CLASS import Saving, Checking, Account, Bank
from final_project_utility import createAccountNo

class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.bank = Bank()
        self.welcome()
 
    def clear_frame(self): #clears the previous frame
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        root.destroy()

    def logout(self):
        del self.account
        self.welcome()
        
    def welcome(self): #welcome screen
        self.clear_frame()
        
        welcome_label = Label(self, text = 'Welcome to 209 Banking!')
        self.b1  = Button(self, text = "Existing User", \
                     command=self.existing_account_widget)
        self.b2  = Button(self, text = "New User", \
                     command=self.new_account_widget)
        self.b3  = Button(self, text = "Exit Application", \
                     command=self.exit_application)

        welcome_label.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        
        
    def new_account_widget(self):
        
        self.clear_frame()
        # ********************* create widgets *********************
        label_fname = Label(self, text = "First name: ")
        self.entry_fname = Entry(self, width=15)
        label_lname = Label(self, text = "Last name: ")
        self.entry_lname = Entry(self, width=15)


        label_line1 = Label(self, text= "Address line1: ")
        self.entry_line1 = Entry(self, width = 15)

        label_line2 = Label(self, text= "Address line2: ")
        self.entry_line2 = Entry(self, width = 15)

        label_type = Label(self, text="Account Type: ")
        self.entry_accounttype = Entry(self, width = 15)

        label_username = Label(self, text = "Username: ")
        self.entry_username = Entry(self, width=15)
        label_pin = Label(self, text = "Pin: ")
        self.entry_pin = Entry(self, width=15)

        
        button_create  = Button(self, text = "Create account", \
                                command=self.create_account_button_click)
        button_main_menu  = Button(self, text = "Main Menu", \
                                command=self.welcome)

        # ********************* Layout Widgets *********************
        #name
        label_fname.grid(row=0, column = 0)
        self.entry_fname.grid(row=0, column = 1)
        label_lname.grid(row = 1, column = 0)
        self.entry_lname.grid(row = 1, column = 1)
        #address
        label_line1.grid(row = 2, column = 0)
        self.entry_line1.grid(row = 2, column = 1)
        label_line2.grid(row = 3, column = 0)
        self.entry_line2.grid(row = 3, column = 1)
        #account type
        label_type.grid(row=4, column = 0)
        self.entry_accounttype.grid(row=4, column =1)
        #login info
        label_username.grid(row=5, column = 0)
        self.entry_username.grid(row=5, column = 1)
        label_pin.grid(row=6, column = 0)
        self.entry_pin.grid(row=6, column = 1)

        
        #button
        button_create.grid(row = 7, column = 0)
        button_main_menu.grid(row = 7, column = 1)

 

    #Create account object
    def create_account_button_click(self):
        
        cfname= self.entry_fname.get()
        clname= self.entry_lname.get()

        cline1= self.entry_line1.get()
        cline2= self.entry_line2.get()

        t = self.entry_accounttype.get().lower()
        u = self.entry_username.get()
        p = self.entry_pin.get()

        self.clear_frame()
        label_accountno = Label(self, text = "Your account no: ")
        self.accountno  = StringVar(self, '') #create StringVar object
        label_final_accountno  = Label(self, \
                                       textvariable=self.accountno) #associate self.result with this label


        s = createAccountNo()
        self.accountno.set(s) #setting the self.result label
        if t.lower() == 'saving': #creating saving object
            d = {'fname':cfname, 'lname':clname,\
                 'line1':cline1, 'line2':cline2, 'accountno':s,\
                 'balance':0, 'acctype':t,'username':u, 'pin':p}
            self.account= Saving(**d)

        elif t.lower() == 'checking':
            d = {'fname':cfname, 'lname':clname,\
                 'line1':cline1, 'line2':cline2, 'accountno':s,\
                 'balance':0, 'acctype':t,'username':u, 'pin':p}
            self.account= Checking(**d)
        
        self.bank.display()
        self.button_next  = Button(self, text = "Please Login Again", command=self.existing_account_widget)
        label_accountno.grid(column=0, columnspan = 2)
        label_final_accountno.grid(column=0, columnspan = 2)
        self.button_next.grid(column = 0, columnspan = 2 )
 

    def existing_account_widget(self):
        self.clear_frame()
        #login
        label_username = Label(self, text = "Username: ")
        self.entry_exist_username = Entry(self, width=15)
        label_pin = Label(self, text = "Pin: ")
        self.entry_exist_pin = Entry(self, width=15)

        label_username.grid(row = 0, column = 0)
        self.entry_exist_username.grid(row = 0, column = 1)

        label_pin.grid(row = 1, column = 0)
        self.entry_exist_pin.grid(row = 1, column = 1)

        
        self.login_button  = Button(self, text = "Login", command=self.login_button_click)
        self.login_button.grid(column = 0, columnspan = 2)

        self.button_main  = Button(self, text = "Main Menu", command=self.welcome)
        self.button_main.grid(column =0,columnspan = 2)

    def login_button_click(self):
        u = self.entry_exist_username.get()
        p = self.entry_exist_pin.get()
        if (self.bank.login_validity(u, p)):
            self.account = self.bank.load_account(u, p) #returns account object
            self.existing_user_options()
        else:
            self.existing_account_widget()
            

    def existing_user_options(self):
        self.clear_frame()
        self.deposit_button  = Button(self, text = "Deposit", \
                                      command=self.deposit_interface)
        self.deposit_button.grid()

        self.withdraw_button  = Button(self, text = "Withdraw",\
                                       command=self.withdraw_interface)
        self.withdraw_button.grid()

        self.summary_button  = Button(self, text = "Account Summary", \
                                            command=self.summary_interface)
        self.summary_button.grid()

        self.button_logout  = Button(self, text = "Logout", command=self.logout)
        self.button_logout.grid(column =0,columnspan = 2)



        self.button_exit  = Button(self, text = "Exit Application", \
                                   command=self.exit_application)
        self.button_exit.grid(column =0,columnspan = 2)
        
    def summary_interface(self):
        self.clear_frame()
        self.label_accno = Label(self, text = 'Account Number')
        self.entry_accno=Entry(self, width = 15)

        self.label_accno.grid(row=0, column = 0)
        self.entry_accno.grid(row=0, column = 1)

        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.grid(row =2, column = 0)

        self.button_next  = Button(self, text = "Next", \
                                            command=self.summary)
        self.button_next.grid(row =2, column =1 )

        
    
    def summary(self):
        accno = self.entry_accno.get()
        name, address, acctype, balance = self.account.summary(accno)
        
        self.clear_frame()
        self.info_label = Label(self, text = "Accout Information")
        self.name_label = Label(self, text = name)
        self.address_label = Label(self, text = address)
        self.acctype_label = Label(self, text = acctype)
        self.balance_label = Label(self, text = str(balance))
        self.info_label.pack()
        self.name_label.pack()
        self.address_label.pack()
        self.acctype_label.pack()
        self.balance_label.pack()
        

        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.pack()
        
    def deposit_interface(self):
        self.clear_frame()
        self.label_deposit = Label(self, text = 'Amount to deposit')
        self.entry_deposit=Entry(self, width = 15)

        self.label_deposit.grid(row=0, column = 0)
        self.entry_deposit.grid(row=0, column = 1)

        self.label_accno = Label(self, text = 'Account Number')
        self.entry_accno=Entry(self, width = 15)

        self.label_accno.grid(row=1, column = 0)
        self.entry_accno.grid(row=1, column = 1)
        
        
        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.grid(row =2, column = 0)

        self.button_next  = Button(self, text = "Next", \
                                            command=self.deposit)
        self.button_next.grid(row =2, column =1 )

    def deposit(self):
        d = self.entry_deposit.get()
        accno = self.entry_accno.get()
        self.account.deposit(d, accno)
        self.check_balance(accno)

        
    def withdraw_interface(self):
        self.clear_frame()
        self.label_withdraw = Label(self, text = 'Amount to withdraw')
        self.entry_withdraw=Entry(self, width = 15)
        self.label_withdraw.grid(row=0, column = 0)
        self.entry_withdraw.grid(row=0, column = 1)

        self.label_accno = Label(self, text = 'Account Number')
        self.entry_accno=Entry(self, width = 15)
        self.label_accno.grid(row=1, column = 0)
        self.entry_accno.grid(row=1, column = 1)

        
        
        self.button_options  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.button_options.grid(row =2, column = 0)

        self.button_next  = Button(self, text = "Next", \
                                            command=self.withdraw)
        self.button_next.grid(row =2, column =1 )


    def withdraw(self):
        w = self.entry_withdraw.get()
        accno = self.entry_accno.get()
        self.account.withdraw(w, accno)
        self.check_balance(accno)


        
    def check_balance(self, accno):

        self.clear_frame()
        label_balance = Label(self, text = 'Current balance: ' + \
                              str(self.account.getBalance(accno)))
        label_balance.grid()
        
        self.options_button  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.options_button.grid()


             
#driver
root = Tk()
frame = MyFrame(root)
frame.pack()
root.mainloop()
