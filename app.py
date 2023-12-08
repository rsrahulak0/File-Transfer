from tkinter import *
import socket
from tkinter import filedialog, messagebox
import os

root = Tk()
root.title("Share Your Files")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=(('file_type', '*.txt'), ('all files', '*.*')))

    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print("waiting for any incoming connections.......")
        conn, address = s.accept()
        file = open(filename, 'rb')
        file_data = file.read((1024))
        conn.send(file_data)
        print("Data has been transmitted successfully....")

    #icon
    image_icon1 = PhotoImage(file="resources/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="resources/sender.png")
    Label(window, image=Sbackground).place(x=0, y=0)

    Mbackground = PhotoImage(file="resources/id.png")
    Label(window, image=Mbackground, bg="#f4fdfe").place(x=100, y=260)

    host = socket.gethostname()
    Label(window, text=f'ID:{host}', bg='white', fg='black').place(x=170, y=330)

    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file).place(x=160, y=150)
    Button(window, text="Send", width=8, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=sender).place(x=300, y=150)

    window.mainloop()

def Receive():
    window1 = Toplevel(root)
    window1.title("Receive")
    window1.geometry("450x560+500+200")
    window1.configure(bg="#f4fdfe")
    window1.resizable(False, False)

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        file = open(filename1, 'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")

    # icon
    image_icon1 = PhotoImage(file="resources/receive.png")
    window1.iconphoto(False, image_icon1)

    Hbackground = PhotoImage(file="resources/receiver.png")
    Label(window1, image=Hbackground).place(x=0, y=0)

    logo = PhotoImage(file="resources/profile.png")
    Label(window1, image=logo, bg="#f4fdfe").place(x=10, y=250)

    Label(window1, text="Receive", font=('arial', 20), bg="#f4fdfe").place(x=100, y=280)

    Label(window1, text="Input sender id", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry(window1, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(window1, text="filename for the incoming file", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(window1, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    incoming_file.place(x=20, y=450)

    rr = Button(window1, text="Receive", compound=LEFT, width=20, bg="#39c790", font="arial 14 bold")
    rr.place(x=20, y=500)

    window1.mainloop()
#icon
image_icon = PhotoImage(file="resources/icon.png")
root.iconphoto(False, image_icon)

Label(root, text='File Transfer', font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").place(x=20, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

send_image = PhotoImage(file="resources/send.png")
send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
send.place(x=50, y=100)

receive_image = PhotoImage(file="resources/receive.png")
receive = Button(root, image=receive_image, bg="#f4fdfe", bd=0, command=Receive)
receive.place(x=300, y=100)

#Label
Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)

background = PhotoImage(file="resources/background.png")
Label(root, image=background).place(x=25, y=323)

root.mainloop()