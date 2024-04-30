from tkinter import*
from tkinter import messagebox
import base64
screen = Tk()
screen.geometry("420x420")
screen.title("Encryption and Decryption")
screen.configure(bg="grey")
def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")

        Message = text1.get(1.0,END)
        encode_message = Message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="code is Encrypted",font="impack 10 bold").place(x=5,y=6)
        text2 = Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)
       

    elif(password==""):
        messagebox.showerror("Error","please enter the secret key")
    elif(password!="1234"):
        messagebox.showerror("OOPS","Invalid secret key")

def decrypt():
    password=code.get()
    if password=="1234":
           screen2=Toplevel(screen)
           screen2.title("Encryption")
           screen2.geometry("400x250")
           screen2.configure(bg="green")

           Message = text1.get(1.0,END)
           encode_message = Message.encode("ascii")
           base64_bytes = base64.b64decode(encode_message)
           encrypt=base64_bytes.decode("ascii")

           Label(screen2,text="code is Decrypted",font="impack 10 bold").place(x=5,y=6)
           text2 = Text(screen2,font="30",bd=4,wrap=WORD)
           text2.place(x=2,y=30,width=390,height=180)
           text2.insert(END,encrypt)
           

    elif(password==""):
        messagebox.showerror("Error","please enter the secret key")
    elif(password!="1234"):
        messagebox.showerror("OOPS","Invalid secret key")
def reset():
      text1.delete(1.0,END)
      code.set("")


        






      Label(screen,text="enter the text for encryption and decryption",font="impack 14 bold").place(x=5,y=6)
text1=Text(screen,font="20")
text1.place(x=5,y=45,width=410,height=120)
code=StringVar()
Label(screen,text="Enter Secret key",font="impack 13 bold").place(x=138,y=185)
Entry(textvariable=code,bd=4,font="20",show="*").place(x=110,y=220)
Button(screen,text="ENCRYPT",font="arial 15 bold",bg="red",fg="white",command=encrypt).place(x=15,y=280,width=180)
Button(screen,text="DECRYPT",font="arial 15 bold",bg="green",fg="white",command=decrypt).place(x=220,y=280,width=180)
Button(screen,text="RESET",font="arial 15 bold",bg="orange",fg="white",command=reset).place(x=60,y=350,width=280)








mainloop()