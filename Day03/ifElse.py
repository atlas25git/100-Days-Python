var = input("Enter your data:")

if(type(var)==type(1)):
    print("Integer")
elif(type(var)==type('s')):
    print("type is String")
else:
    print("Not an Int")
