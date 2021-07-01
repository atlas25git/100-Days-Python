class className:
    pass

#pass is required to avoid indentation required warning
var = className()


#using constructors
#__inti__() -> used to intialize attributes

class user:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.default = 0;

user_1=user("69","atlas")

print(user_1.default)