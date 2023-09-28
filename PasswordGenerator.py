from tkinter import *
import random, string
import pyperclip



###window intialization

password =Tk()
password.geometry("500x500")
password.resizable(0,0)
password.configure(background="#B2004C")
password.title("Random - PASSWORD GENERATOR")

#Labeling
heading = Label(password, text='PASSWORD GENERATOR', font='arial 15 bold',bg='#B9195D')
heading.pack(pady=30)  # Adjust the padding (pady) to move the label down

Label(password, text ='Random', font ='arial 15 bold').pack(side = BOTTOM,pady=20)




#Lenght of password selection
pass_label = Label(password, text='PASSWORD LENGTH', font='arial 10 bold')
pass_label.pack()

pass_len = IntVar()
length = Spinbox(password, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()



#function definition

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   


#buttons

Button(password, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(password , textvariable = pass_str).pack()

#function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(password, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)




# loop to run program
password.mainloop()

