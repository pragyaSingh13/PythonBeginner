import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename

def open_file():
    #open file for editing
    filepath = askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0,tk.END)
    with open(filepath,"r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END,text)
    window.title("Simple text editior - {filepath}")

def save_file():
    """Save the current file as a new file"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files","*.txt"),("All Files","*.*")],
    )
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text = txt_edit.get(1.0,tk.END)
        output_file.write(text)
    window.title(f"Made by Pragya Singh {filepath}")

window = tk.Tk()
window.title("Made by Pragya")
window.rowconfigure(0,minsize=600,weight=1)
window.columnconfigure(1, minsize=400,weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window,relief=tk.RAISED,bd=8,bg="#fade72")
btn_open = tk.Button(fr_buttons,text="Open",command=open_file,bg="#fade72",fg="#121122")
btn_save = tk.Button(fr_buttons,text="Save As...",command=save_file,bg="#112233",fg="#fff")

btn_open.grid(row=0, column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)
fr_buttons.grid(row=0,column=0, sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()