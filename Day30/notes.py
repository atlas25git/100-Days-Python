#Handling errors

from typing import Type


try:
    file = open("atlas25.txt")
    #something which might cause exception
except FileNotFoundError:
    #except is quite broad it'd do the smae thing for all the errors that might occur,
    #thus we specufy errors after except, in multiple blocks
    file = open("atlas25.txt","w")
    print('except called')
    #Will be executed when an exception is found
except KeyError as error:
    print(f"{error}")
else:
    print("executed when no exception found")
    #No exceptions found
finally:
    file.close()
    print("Runs irrespective of the contingencies")
    #Do this no matter what

#Creating custom exceptions

raise TypeError("From the class of avl errors we choose one and put up a msg, the program exec stops")

if height>3:
    raise ValueError("Not a human height")