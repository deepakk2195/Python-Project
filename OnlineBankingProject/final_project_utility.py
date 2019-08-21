import random, string

def createAccountNo():
    
    number = ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))
    return number

#print(createAccountNo())
