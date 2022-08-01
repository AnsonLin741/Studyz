
import tkinter as tk
import tkinter.messagebox
import pickle
#window
window=tk.Tk()
window.title('StudyZ')
window.geometry('450x200')
#label for username and password
tk.Label(window,text='username:').place(x=90,y=50)
tk.Label(window,text='password:').place(x=90,y=90)
#username entry
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=50)
#password entry
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=90)
 
def usr_log_in():
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',
                                   message='Welcome：'+usr_name)
        else:
            tk.messagebox.showerror(message='password error')
    #user name and password can't be empty
    elif usr_name=='' or usr_pwd=='' :
        tk.messagebox.showerror(message='username and password can\'t be empty')
    else:
        is_signup=tk.messagebox.askyesno('welcome','you have not sign up yet,do you want to sign up?')
        if is_signup:
            usr_sign_up()

def usr_sign_up():
    def signtowcg():
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
 
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}           
            
        if nn in exist_usr_info:
            tk.messagebox.showerror('error','username already exists')
        elif np =='' or nn=='':
            tk.messagebox.showerror('error','username or password is empty')
        elif np !=npf:
            tk.messagebox.showerror('error','password and confirm password is not the same')
        else:
            exist_usr_info[nn]=np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('Welcome','sign up successful')
            window_sign_up.destroy()
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('sign up')
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='username：').place(x=10,y=10)
    tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='please enter password：').place(x=10,y=50)
    tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text='please confirm password：').place(x=10,y=90)
    tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
    bt_confirm_sign_up=tk.Button(window_sign_up,text='confirm register',command=signtowcg)
    bt_confirm_sign_up.place(x=150,y=130)

def usr_sign_quit():
    window.destroy()
bt_login=tk.Button(window,text='login',command=usr_log_in)
bt_login.place(x=140,y=130)
bt_logup=tk.Button(window,text='sign up',command=usr_sign_up)
bt_logup.place(x=210,y=130)
bt_logquit=tk.Button(window,text='exit',command=usr_sign_quit)
bt_logquit.place(x=280,y=130)
window.mainloop()