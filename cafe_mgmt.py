import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------------- MENU ----------------
menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 80,
    "Cake": 60,
    "Burger": 100
}

# ---------------- SAVE ORDER ----------------
def save_order(order, total, date):

    with open("orders.txt", "a") as file:

        file.write("\nDate: " + date + "\n")

        for item in order:
            file.write(f"{item[0]} x {item[1]} = ₹{item[2]}\n")

        file.write("Total = ₹" + str(total) + "\n")
        file.write("--------------------------\n")


# ---------------- GENERATE BILL ----------------
def generate_bill():

    receipt.delete("1.0", tk.END)

    total = 0
    order = []

    for item in menu:

        qty = int(entries[item].get())
        price = menu[item]
        cost = qty * price

        if qty > 0:
            order.append((item, qty, cost))
            total += cost

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    receipt.insert(tk.END,"        CAFE RECEIPT\n")
    receipt.insert(tk.END,"------------------------------\n")
    receipt.insert(tk.END,"Date: "+now+"\n\n")

    for item in order:
        receipt.insert(tk.END,f"{item[0]} x {item[1]}   ₹{item[2]}\n")

    receipt.insert(tk.END,"\n------------------------------\n")
    receipt.insert(tk.END,"Total Bill: ₹"+str(total))
    receipt.insert(tk.END,"\n------------------------------\n")

    save_order(order,total,now)

    messagebox.showinfo("Success","Order generated successfully!")


# ---------------- CLEAR ----------------
def clear():

    for item in entries:
        entries[item].delete(0, tk.END)
        entries[item].insert(0,"0")

    receipt.delete("1.0",tk.END)


# ---------------- WINDOW ----------------
window = tk.Tk()
window.title("Cafe Management System")
window.geometry("700x500")
window.configure(bg="#f0f0f0")

# ---------------- TITLE ----------------
title = tk.Label(window,
text="Cafe Management System",
font=("Arial",20,"bold"),
bg="#333",
fg="white",
pady=10)

title.pack(fill="x")

# ---------------- MAIN FRAME ----------------
main_frame = tk.Frame(window,bg="#f0f0f0")
main_frame.pack(pady=20)

# ---------------- MENU FRAME ----------------
menu_frame = tk.LabelFrame(main_frame,
text="Menu",
font=("Arial",12,"bold"),
padx=20,
pady=20)

menu_frame.grid(row=0,column=0,padx=20)

entries = {}

row = 0

for item in menu:

    tk.Label(menu_frame,
    text=f"{item} (₹{menu[item]})",
    font=("Arial",11)).grid(row=row,column=0,pady=5,sticky="w")

    entry = tk.Entry(menu_frame,width=5,justify="center")
    entry.insert(0,"0")
    entry.grid(row=row,column=1,padx=10)

    entries[item] = entry

    row += 1


# ---------------- BUTTONS ----------------
button_frame = tk.Frame(menu_frame)
button_frame.grid(row=row,columnspan=2,pady=15)

bill_btn = tk.Button(button_frame,
text="Generate Bill",
command=generate_bill,
bg="#4CAF50",
fg="white",
width=12)

bill_btn.grid(row=0,column=0,padx=5)

clear_btn = tk.Button(button_frame,
text="Clear",
command=clear,
bg="#f44336",
fg="white",
width=12)

clear_btn.grid(row=0,column=1,padx=5)


# ---------------- RECEIPT FRAME ----------------
receipt_frame = tk.LabelFrame(main_frame,
text="Receipt",
font=("Arial",12,"bold"),
padx=10,
pady=10)

receipt_frame.grid(row=0,column=1)

receipt = tk.Text(receipt_frame,
height=20,
width=35,
font=("Courier",11))

receipt.pack()

window.mainloop()
