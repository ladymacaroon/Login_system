import tkinter as tk
import hashlib

def encrypt_password(password):
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password_hash
 
root=tk.Tk()

root.geometry("600x400")

fname_var=tk.StringVar()
sname_var=tk.StringVar()
age_var=tk.StringVar()
passw_var=tk.StringVar()

def submit():

    fname = fname_var.get()
    sname = sname_var.get()
    age = age_var.get()
    password = passw_var.get()
    
    with open("passwords.txt", "w") as file:
        username = fname[:3] + sname[:3] + age
        encrypted_password = encrypt_password(password)
        file.write(f'{username}:{encrypted_password}\n')

    fname_var.set("")
    sname_var.set("")
    age_var.set("")
    passw_var.set("")

fname_label = tk.Label(root, text = 'First name', font=('calibre',10, 'bold'))
fname_entry = tk.Entry(root,textvariable = fname_var, font=('calibre',10,'normal'))
sname_label = tk.Label(root, text = 'Last name', font=('calibre',10, 'bold'))
sname_entry = tk.Entry(root,textvariable = sname_var, font=('calibre',10,'normal'))
age_label = tk.Label(root, text = 'Age', font=('calibre',10, 'bold'))
age_entry = tk.Entry(root,textvariable = age_var, font=('calibre',10,'normal'))
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*') 
sub_btn=tk.Button(root,text = 'Submit', command = submit)

fname_label.grid(row=0,column=0)
fname_entry.grid(row=0,column=1)
sname_label.grid(row=1,column=0)
sname_entry.grid(row=1,column=1)
age_label.grid(row=2,column=0)
age_entry.grid(row=2,column=1)
passw_label.grid(row=3,column=0)
passw_entry.grid(row=3,column=1)
sub_btn.grid(row=4,column=1)

root.mainloop()
