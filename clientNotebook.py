from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Clients Notebook")

conn = sqlite3.connect('crm.db')

c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        company TEXT NOT NULL,
        phone TEXT NOT NULL
        );
""")

def render_clients():
    rows = c.execute("SELECT * FROM clients").fetchall()

    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))

def insert(client):
    c.execute("""
        INSERT INTO clients (name, company, phone) VALUES (?,?,?)
    """, (client['name'], client['company'], client['phone']))
    conn.commit()
    render_clients()

def new_client():
    def save():
        if not name.get():
            messagebox.showerror("Error", "Name is required")
            return
        if not phone.get():
            messagebox.showerror("Error", "Phone is required")
            return
        if not company.get():
            messagebox.showerror("Error", "Company is required")
            return
        client = {
            'name': name.get(),
            'phone': phone.get(),
            'company': company.get()
            
        }
        insert(client)
        top.destroy()    


    top = Toplevel()
    top.title("New client")

    lname = Label(top, text="Name")
    name = Entry(top, width=40)
    lname.grid(row=0, column=0)
    name.grid(row=0, column=1)

    lphone = Label(top, text="Phone")
    phone = Entry(top, width=40)
    lphone.grid(row=1, column=0)
    phone.grid(row=1, column=1)

    lcompany = Label(top, text="Company")
    company = Entry(top, width=40)
    lcompany.grid(row=2, column=0)
    company.grid(row=2, column=1)

    save = Button(top, text='Save', command=save)
    save.grid(row=3, column=1)

    top.mainloop()

def delete_client():
    id = tree.selection()[0]

    client = c.execute("SELECT * FROM clients WHERE id = ?", (id, )).fetchone()

    answer = messagebox.askokcancel('You sure?', 'You sure you want to delete this client ' + client[1]  + '?')
    if answer:
        c.execute("DELETE FROM clients WHERE id = ?", (id, ))
        conn.commit()
        render_clients()
    else:
        pass

btn = Button(root, text='New client', command=new_client)
btn.grid(column=0, row=0)

btn_delete = Button(root, text='Delete client', command=delete_client)
btn_delete.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Phone', 'Company')
tree.column('#0', width =0, stretch=NO)
tree.column('Name')
tree.column('Phone')
tree.column('Company')

tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Company', text='Company')
tree.grid(column=0, row=1, columnspan=2)

render_clients()

root.mainloop()