class Session:
    def __init__(self):
        self.user = None

    def login(self, username):
        self.user = username
        print(f"{username} logged in")

    def logout(self):
        print(f"{self.user} logged out")
        self.user = None



s = Session()
s.login("Ali")   
s.logout()       
