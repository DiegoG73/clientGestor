from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Gestor de Clientes")

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Teléfono', 'Empresa')

tree.column('#0')
tree.column('Nombre')
tree.column('Teléfono')
tree.column('Empresa')

tree.heading('#0', text='id')
tree.heading('Nombre', text='Nombre')
tree.heading('Teléfono', text='Teléfono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=0)

tree.insert('', 'end', 'lala',values=('1', '2', '3'), text='Chanchito Felíz')
tree.insert('', 'end', 'lele',values=('4', '5', '6'), text='Chanchito Triste')
tree.insert('lele', 'end', 'lili',values=('7', '8', '9'), text='Hijo')

root.mainloop()