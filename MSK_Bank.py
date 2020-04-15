""" This is the MSK bank & someday it will be huge. """

class Bank_account:
    def __init__(self, c_name, c_acc_num, c_acc_balance):
        self.c_name = c_name
        self.c_acc_num = c_acc_num
        self.c_acc_balance = c_acc_balance

    def withraw(self, amount):
        self.c_acc_balance -= amount

    def deposite(self, amount):
        self.c_acc_balance += amount

    def __str__(self):
        return '''---MSK Bank--- \ncustmer name: {} \ncustmer account number : {}
custmer account balance: {}'''.format(self.c_name,self.c_acc_num, self.c_acc_balance)


