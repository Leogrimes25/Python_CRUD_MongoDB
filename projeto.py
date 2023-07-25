import json
import tkinter
from tkinter import *
from tkinter import ttk
import pymongo
import pandas as pd
from bson import ObjectId
from tkinter import messagebox

import warnings

# Connection String of Mongodb #
server = pymongo.MongoClient(
    "")
database = server.get_database('Projeto')
collection = database.get_collection('TechStore')

root_tk = tkinter.Tk()  # Configuration of GUI Tkinter#
root_tk.geometry("1004x591")
root_tk.title("Info Store Management")
root_tk.config(background='black')

while True:

    def add_data():
        data = {"Modelo Item": entry1.get(), "Preço Item": float(entry2.get()),
                "Info Item": entry3.get()}
        collection.insert_one(data)
        tkinter.messagebox.showinfo(title='Aviso', message='Dados Incluídos')


    def visualize_all():
        for item in Listbox.get_children():
            Listbox.delete(item)
        datas = list(collection.find())
        for item in datas:
            Listbox.insert("", END, values=list(item.values()))


    def visualize_byid():
        for item in Listbox.get_children():
            Listbox.delete(item)
        data = list(collection.find({"_id": ObjectId(ObjectId(entry6.get()))}))
        for item in data:
            Listbox.insert("", END, values=list(item.values()))


    def visualize_by_model():
        for item in Listbox.get_children():
            Listbox.delete(item)
        data = list(collection.find({"Modelo Item": entry1.get()}))
        for item in data:
            Listbox.insert("", END, values=list(item.values()))


    def visualize_by_price():
        for item in Listbox.get_children():
            Listbox.delete(item)
        data = list(collection.find({"Preço Item": float(entry2.get())}))
        for item in data:
            Listbox.insert("", END, values=list(item.values()))


    def update_preco():
        data = {"_id": ObjectId(ObjectId(entry6.get()))}
        data1 = {"$set": {"Preço Item": float(entry2.get())}}
        collection.update_one(data, data1)
        tkinter.messagebox.showinfo(title='Aviso', message='Dados Atualizados')


    def update_info():
        data = {"_id": ObjectId(ObjectId(entry6.get()))}
        data1 = {"$set": {"Info Item": entry3.get()}}
        collection.update_one(data, data1)
        tkinter.messagebox.showinfo(title='Aviso', message='Dados Atualizados')


    def delete_data():
        data = {"_id": ObjectId(ObjectId(entry6.get()))}
        collection.delete_one(data)
        tkinter.messagebox.showinfo(title='Aviso', message='Dados Deletados')


    def save_csv():
        csv = pd.read_csv(entry4.get())
        data_csv = csv.to_dict(orient='records')
        collection.insert_many(data_csv)
        tkinter.messagebox.showinfo(title='Aviso', message='Arquivo Importado')


    def save_json():
        json_file = open(entry5.get())
        data = json_file
        data_file = json.load(data)
        collection.insert_one(data_file)
        tkinter.messagebox.showinfo(title='Aviso', message='Arquivo Importado')


    def refresh_list():
        for item in Listbox.get_children():
            Listbox.delete(item)


    def clear_text():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)


    def exit_window():
        root_tk.destroy()


    img = tkinter.PhotoImage(file='Python.png')  # Adding Background Image with PhotoImage #

    label_img = Label(root_tk, image=img)

    label_img.pack()

    label = tkinter.Label(root_tk, text="Tech Store", font=("Helvetica", 18))

    label.pack(pady=20)

    label1 = tkinter.Label(root_tk, text=" Modelo Item:", font=('Arial', 9), fg='black')

    label1.place(x=1, y=10)

    label2 = tkinter.Label(root_tk, text="Preço Item:", foreground='black', font=('Arial', 9), fg='black')

    label2.place(x=3, y=40)

    label3 = tkinter.Label(root_tk, text="Info Item:", foreground='black', font=('Arial9', 9), fg='black')

    label3.place(x=3, y=70)

    label4 = tkinter.Label(root_tk, text='Arquivo CSV:', font=('Arial', 9), foreground='black')

    label4.place(x=250, y=10)

    label5 = tkinter.Label(root_tk, text='Arquivo JSON:', font=('Arial', 9), foreground='black')

    label5.place(x=250, y=40)

    label6 = tkinter.Label(root_tk, text='_Id', font=('Arial', 9), fg='black', foreground='black')

    label6.place(x=250, y=70)

    entry1 = Entry(root_tk)

    entry1.place(x=110, y=10)

    entry2 = Entry(root_tk)

    entry2.place(x=110, y=40)

    entry3 = Entry(root_tk)

    entry3.place(x=110, y=70)

    entry4 = tkinter.Entry(root_tk)

    entry4.place(x=350, y=10)

    entry5 = tkinter.Entry(root_tk)

    entry5.place(x=350, y=40)

    entry6 = Entry(root_tk)

    entry6.place(x=350, y=70)

    columns = ("Identificação", "Modelo Item", "Preço Item", "Info Item")

    Listbox = ttk.Treeview(root_tk, columns=columns, show="headings")  # Creating a Treeview with TTK for Visualisation
    # of Collections#
    Listbox.heading('Identificação', text='Identificação')
    Listbox.heading('Modelo Item', text='Modelo Item')
    Listbox.heading('Preço Item', text='Preço Item')
    Listbox.heading('Info Item', text='Info Item')

    Listbox.place(x=5, y=330)

    button_add = tkinter.Button(root_tk, fg="black", text="Adicionar Doc", height=2, width=15, command=add_data)
    button_add.place(x=5, y=100)

    button_update = tkinter.Button(root_tk, fg="black", text="Atualizar Preço", height=2, width=15,
                                   command=update_preco)
    button_update.place(x=250, y=150)

    button_update_info = tkinter.Button(root_tk, fg="black", text="Atualizar Info", height=2, width=15,
                                        command=update_info)
    button_update_info.place(x=125, y=150)

    button_delete = tkinter.Button(root_tk, fg="black", text="Deletar por Id", height=2, width=15, command=delete_data)
    button_delete.place(x=375, y=150)

    button_visualize = tkinter.Button(root_tk, fg="black", text="Visualizar Todos", height=2, width=15,
                                      command=visualize_all)
    button_visualize.place(x=125, y=100)

    button_visualize_model = tkinter.Button(root_tk, fg='black', text='Visualizar por Modelo', height=2, width=16,
                                            command=visualize_by_model)
    button_visualize_model.place(x=375, y=100)

    button_visualize_price = tkinter.Button(root_tk, fg='black', text='Visualizar por Preço', height=2, width=15,
                                            command=visualize_by_price)

    button_visualize_price.place(x=5, y=150)

    button_visualize_id = tkinter.Button(root_tk, fg='black', text='Visualizar por Id', height=2, width=15,
                                         command=visualize_byid)
    button_visualize_id.place(x=250, y=100)

    button_save_csv = tkinter.Button(root_tk, fg='black', text='Salvar CSV', height=2, width=15, command=save_csv)
    button_save_csv.place(x=5, y=200)

    button_save_json = tkinter.Button(root_tk, fg='black', text='Salvar JSON', height=2, width=15, command=save_json)
    button_save_json.place(x=125, y=200)

    button_refresh_list = tkinter.Button(root_tk, fg='black', text='Limpar Lista', height=1, width=10,
                                         command=refresh_list)
    button_refresh_list.place(x=850, y=500)

    button_clear_entry = tkinter.Button(root_tk, fg='black', text='Limpar Entrada', height=1, width=11,
                                        command=clear_text)
    button_clear_entry.place(x=850, y=450)

    button_exit = tkinter.Button(root_tk, fg='black', text='Sair', height=1, width=5, command=exit_window)
    button_exit.place(x=850, y=550)

    root_tk.mainloop()
