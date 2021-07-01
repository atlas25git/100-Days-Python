class user:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.following = 0;
        self.followers = 0;

   
    def follow(self,user):
        user.followers+=1
        self.following+=1

user_1=user("69","atlas")
user_2=user("69","atlas")
user_1.follow(user_2)
user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)