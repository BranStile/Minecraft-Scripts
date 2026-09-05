import tkinter as tk
from tkinter import ttk
from fishing import fish

def show_selection():
    selected_item = combo.get()
    print(f"User selected: {selected_item}")
    if(selected_item == ""):
        print("Select again; invalid selection")
    else:
        if(selected_item == "Fishing"):
            fish()
        root.destroy() 

root = tk.Tk()
root.title("Application Selection")
root.geometry("300x150")


label = tk.Label(root, text="Please select a script:")
label.pack(pady=10)


options = ["","Fishing"]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.current(0) 
combo.pack(pady=5)


button = tk.Button(root, text="Confirm", command=show_selection)
button.pack(pady=15)

root.mainloop()