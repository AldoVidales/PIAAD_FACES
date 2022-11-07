import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from capturadoRostros import faceCapture
import os
import sys
from ReconocimientoFacial import facerec
from entrenandoRF import training
# root window

root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()

def restart():   # ESTA ES LA SENTENCIA QUE DA ORIGEN A LA CONSULTA
  os.execl(sys.executable, sys.executable, * sys.argv)
def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(
        title='Information',
        message=msg)


    faceCapture(email.get())

    print("training")
    training()
    root.destroy()
    facerec()

    email.set('')
    password.set('')
    respuesta=tk.messagebox.askquestion(message="¿Desea continuar?", title="Título")
    if respuesta == True:
        try:
            print("Leyendo datos")

            facerec()


        except:
            print('No se pudo')





        ''' root.update()
        root.destroy()
        root.__init__()
        '''



    if respuesta==False:
        root.destroy()
        root.quit()


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Name:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="fingerprint:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)



root.mainloop()