import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("Добро пожаловать!")
window.geometry('1800x1200')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Сотрудники')
tab_control.pack(expand=1, fill='both')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Контрагенты')
companies = [
    (1, 'ИП Онохов Павел Сергеевич', 1234),
    (2, 'ИП Мухутдинов Руслан Маисович', 4321),
    (3, 'ИП Абобов Дмитрий Сергеевич ', 8642),
    (4, 'ИП Перегудов Дмитрий Ильич', 9123),
    (5, 'ИП Переломова Анастасия Константиновна', 3495),
    (6, 'ИП Моисеев Артем Ростиславович', 4382),
    (7, 'ИП Критенко Демид Харитонович', 7345),
    (8, 'ИП Солевой Артур Владиславович', 2358),
    (9, 'ИП Лебедев Фанис Дмитриевич', 2346),
    (10, 'ИП Губов Родион Владимирович', 7584),
    (11, 'ИП Дмитриева Ангелина Шахрузовна', 6548),
    (12, 'ИП Грибоедов Павел Алексеевич', 1565),
    (13, 'ИП Клюжина Елена Станиславовна', 2323),
    (14, 'ИП Дудник Ольга Сергеевна', 2222),
    (15, 'ИП Кукутин Данил Николаевич', 1337),
    (16, 'ИП Хорошева Светлана Анатольевна', 2828),
    (17, 'ИП Виноградова Наталья Борисовна', 7777),
    (18, 'ИП Королева Марья Алексеевна', 2343),
    (19, 'ИП Поносов Петр Максимович', 4795),
    (20, 'ИП Конченных Екатерина Михаиловна', 6465),
    (21, 'ИП Деревяшкина Виктория Романовна', 6454),
]
sotr = [
    (1, 'Онохов Павел Сергеевич', 21452354235, 1234),
    (2, 'Мухутдинов Руслан Маисович', 123421415, 4321),
    (3, 'Абобов Дмитрий Сергеевич ', 124213456, 8642),
    (4, 'Перегудов Дмитрий Ильич', 589629856, 9123),
    (5, 'Переломова Анастасия Константиновна', 53645638563, 3495),
    (6, 'Моисеев Артем Ростиславович', 548932562589, 4382),
    (7, 'Критенко Демид Харитонович', 452352365436, 7345),
    (8, 'Солевой Артур Владиславович', 4573451569, 2358),
    (9, 'Лебедев Фанис Дмитриевич', 452212389, 2346),
    (10, 'Губов Родион Владимирович', 684578395932, 7584),
    (11, 'Дмитриева Ангелина Шахрузовна', 13543525432, 6548),
    (12, 'Грибоедов Павел Алексеевич', 3452352667, 1565),
    (13, 'Клюжина Елена Станиславовна', 235423523, 2323),
    (14, 'Дудник Ольга Сергеевна', 523752896582, 2222),
    (15, 'Кукутин Данил Николаевич', 3453246346, 1337),
    (16, 'Хорошева Светлана Анатольевна', 2452135423, 2828),
    (17, 'Виноградова Наталья Борисовна', 43532522, 7777),
    (18, 'Королева Марья Алексеевна', 4353252634, 2343),
    (19, 'Поносов Петр Максимович', 22636356, 4795),
    (20, 'Конченных Екатерина Михаиловна', 23543252, 6465),
    (21, 'Деревяшкина Виктория Романовна', 345326236, 6454),
]

def serch():
    table1.delete(*table1.get_children())
    for row1 in sotr:
        print(fio_entry.get(), inn_entry.get())
        if fio_entry.get() == row1[1] or int(inn_entry.get()) == row1[3]:
            table1.insert('', tkinter.END, values=row1)
def clear():
    table1.delete(*table1.get_children())
    for row1 in sotr:
        table1.insert('', tkinter.END, values=row1)
heads1 = ["№", "ФИО сотрудника", "   Снилс сотрудника   ", "ИНН сотрудника"]
heads2 = ['№', 'Наименование контрагента', 'ИНН контрагента']
table1 = ttk.Treeview(tab1, show='headings')
scr_p1 = ttk.Scrollbar(tab1, command=table1.yview)
table1 = ttk.Treeview(tab1, show='headings', yscrollcommand=scr_p1.set)
table1.configure(yscrollcommand=scr_p1.set)
scr_p1.grid(row=2, column=3, sticky='nsew')
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
company_label = tkinter.Label(tab1, text="ФИО сотрудника")
company_label.grid(row=0, column=1)

inn_label = tkinter.Label(tab1, text="ИНН сотрудника")
inn_label.grid(row=0, column=0)

fio_entry = tkinter.Entry(tab1)
fio_entry.grid(row=1, column=1)

inn_entry = tkinter.Entry(tab1)
inn_entry.grid(row=1, column=0)

confirm_button = tkinter.Button(tab1, text="Применить", command=serch)
confirm_button.grid(row=0, column=2, sticky="news", padx=20)

reset_button = tkinter.Button(tab1, text="Сбросить", command=clear)
reset_button.grid(row=1, column=2, sticky="news", padx=20)


table2 = ttk.Treeview(tab2, show='headings')
scr_p2 = ttk.Scrollbar(tab2, command=table2.yview)
table2 = ttk.Treeview(tab2, show='headings', yscrollcommand=scr_p2.set)
table2.configure(yscrollcommand=scr_p2.set)
scr_p2.grid(row=3, column=4, sticky="ns")
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

table1['columns'] = heads1
table2['columns'] = heads2
for header1 in heads1:
    table1.heading(header1, text=header1, anchor="center")
    table1.column(header1, anchor="center")

for row1 in sotr:
    table1.insert('', tkinter.END, values=row1)

for header2 in heads2:
    table2.heading(header2, text=header2, anchor="center")
    table2.column(header2, anchor="center")

for row2 in companies:
    table2.insert('', tkinter.END, values=row2)


table1.grid(row=2, column=0, columnspan=3)
table2.grid(row=2, column=0)

window.mainloop()

