class User:
    def login(self):
        print('login')
class BusinessUser(User):
    def run(self):
        print('run')
b=BusinessUser()
b.login()
b.run()