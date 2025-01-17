import  threading
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

reminders = {}

def Add_reminder(reminder_time,reminder_msg,output_box):
    try:
        reminder_time = datetime.strptime(reminder_time, "%Y-%m-%d %H:%M:%S")
        if reminder_time <= datetime.now():
            messagebox.showerror("ERROR")
            return
        reminders[reminder_time]=reminder_msg
        output_box.insert(tk.END,f"Add:{reminder_time}-{reminder_msg}\n")

        threading.Thread(target=trigger_reminder,args=(reminder_time,reminder_msg),daemon=True).start()
        messagebox.showinfo("Success","Add Reminder Successfully")
    except ValueError:
        messagebox.showerror("Error","Please try again date_formate")

def viwe_reminder(output_box):
    output_box.delete(1.0,tk.END)
    if reminders:
        output_box.insert(tk.END,"Successfully reminder:\n ")
        for reminder_time, reminder_msg in sorted(reminders.items()):
            output_box.insert(tk.END,f"{reminder_time}-{reminder_msg}\n")
    else:
        output_box.insert(tk.END,"No reminder set\n")

def delete_reminder(reminder_time,output_box):
    try:
        reminder_time = datetime.strptime(reminder_time, "%Y-%m-%d %H:%M:%S")
        if reminder_time in reminders:
            del reminders[reminder_time]
            output_box.insert(tk.END,f"Deleted:{reminder_time}\n")
            messagebox.showinfo("Succes","deleted a reminder")
        else:
            messagebox.showerror("Error")

    except ValueError:
            messagebox.showerror("Error","invalid formate")

def trigger_reminder(reminder_time,reminder_msg):
    while True:
        current_time = datetime.now()
        if current_time >= reminder_time:
            messagebox.showinfo("Reminder",f"reminder:{reminder_msg}\n")
            break
        time.sleep(1)

def main():
    root=tk.Tk()
    root.title("Reminder Application")
    root.geometry("500x500")
#bg colour
    root.configure(bg="lightblue")

#lables for time
    tk.Label(root,text="Reminder time (yyyy-mm-dd HH:MM:SS):",bg="lightblue").pack(pady=5)
    reminder_time_input=tk.Entry(root,width=40)
    reminder_time_input.pack(pady=5)
#lables for msg
    tk.Label(root,text="reminder_msg:",bg="lightblue").pack(pady=5)
    reminder_msg_input=tk.Entry(root,width=40)
    reminder_msg_input.pack(pady=5)

    output_box=tk.Text(root, height=15, width=55, state="normal",bg="pink",fg="black")
    output_box.pack(pady=10)

#lambda is used to pass arguments from the input fields to the functions.-

    tk.Button(root,text="Add Reminder",command=lambda: Add_reminder(reminder_time_input.get(),reminder_msg_input.get(),output_box)).pack(pady=5)
    tk.Button(root,text="View Reminder",command=lambda: viwe_reminder(output_box)).pack(pady=5)
    tk.Button(root,text="Delete Reminder", command=lambda: delete_reminder(reminder_time_input.get(),output_box)).pack(pady=5)
    tk.Button(root,text="Exit",command=root.destroy).pack(pady=10)

#Starts the Tkinter event loop, which keeps the GUI running
    root.mainloop()

if __name__ == "__main__":
    main()




