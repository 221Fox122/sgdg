import tkinter
from tkinter import ttk

# Создание окна программы
window = tkinter.Tk()

# Заголовок окна
window.title('Справочник организаций контрагентов')

window.geometry("600x600")

frame = tkinter.Frame(window)
frame.pack()

company_label = tkinter.Label(frame, text="Наименование контрагента")
company_label.grid(row=0, column=0)

inn_label = tkinter.Label(frame, text="ИНН контрагента")
inn_label.grid(row=0, column=1)

company_entry = tkinter.Entry(frame)
company_entry.grid(row=1, column=0)

inn_label = tkinter.Entry(frame)
inn_label.grid(row=1, column=1)

confirm_button = tkinter.Button(frame, text="Применить")
confirm_button.grid(row=1, column=2, sticky="news", padx=20)

reset_button = tkinter.Button(frame, text="Сбросить")
reset_button.grid(row=1, column=3, sticky="news", padx=20)

companies = [
    (1, 'ИП Онохов Павел Сергеевич', 1234),
    (2, 'ИП Мухутдинов Руслан Маисович', 4321)
]

heads = ['№', 'Наименование контрагента', 'ИНН контрагента']
table = ttk.Treeview(frame, show='headings')
table['columns'] = heads

for header in heads:
    table.heading(header, text=header, anchor="center")
    table.column(header, anchor="center")

for row in companies:
    table.insert('', tkinter.END, values=row)

# table.pack(expand=tkinter.YES, fill=tkinter.BOTH)

window.mainloop()
