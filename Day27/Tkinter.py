import tkinter

window = tkinter.Tk()
window.title("atlas25")
window.minsize(width=500,height=300)

#components:
#Label

label = tkinter.Label(text="Deustch!",font=("Arial",24,"bold"))
label.pack(expand=True)

# ..., suggests argument has got a default value
# kwargs
# Functions that can take any no. of arguments
# *args -> tells fn that it cn accept any no of arguments
# this *args is a tuple

#The concept of **kwargs comes from the utility that we need to access elements through some keywords
# **kwargs is a dictionary
# dict.get() method is preferred over dict["key"] as former doesnt make the app crash if the key isn't present


window.mainloop()