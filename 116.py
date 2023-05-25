import tkinter
from tkinter import ttk


#win1
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
    (1, 'Онохов Павел Сергеевич', 21452354235, 1234, 'ИП Онохов Павел Сергеевич'),
    (2, 'Мухутдинов Руслан Маисович', 123421415, 4321, 'ИП Мухутдинов Руслан Маисович'),
    (3, 'Абобов Дмитрий Сергеевич ', 124213456, 8642, 'ИП Абобов Дмитрий Сергеевич '),
    (4, 'Перегудов Дмитрий Ильич', 589629856, 9123, 'ИП Перегудов Дмитрий Ильич'),
    (5, 'Переломова Анастасия Константиновна', 53645638563, 3495, 'ИП Переломова Анастасия Константиновна'),
    (6, 'Моисеев Артем Ростиславович', 548932562589, 4382, 'ИП Моисеев Артем Ростиславович'),
    (7, 'Критенко Демид Харитонович', 452352365436, 7345, 'ИП Критенко Демид Харитонович'),
    (8, 'Солевой Артур Владиславович', 4573451569, 2358, 'ИП Солевой Артур Владиславович'),
    (9, 'Лебедев Фанис Дмитриевич', 452212389, 2346, 'ИП Лебедев Фанис Дмитриевич'),
    (10, 'Губов Родион Владимирович', 684578395932, 7584, 'ИП Губов Родион Владимирович'),
    (11, 'Дмитриева Ангелина Шахрузовна', 13543525432, 6548, 'ИП Дмитриева Ангелина Шахрузовна'),
    (12, 'Грибоедов Павел Алексеевич', 3452352667, 1565, 'ИП Грибоедов Павел Алексеевич'),
    (13, 'Клюжина Елена Станиславовна', 235423523, 2323, 'ИП Клюжина Елена Станиславовна'),
    (14, 'Дудник Ольга Сергеевна', 523752896582, 2222, 'ИП Дудник Ольга Сергеевна'),
    (15, 'Кукутин Данил Николаевич', 3453246346, 1337, 'ИП Кукутин Данил Николаевич'),
    (16, 'Хорошева Светлана Анатольевна', 2452135423, 2828, 'ИП Хорошева Светлана Анатольевна'),
    (17, 'Виноградова Наталья Борисовна', 43532522, 7777, 'ИП Виноградова Наталья Борисовна'),
    (18, 'Королева Марья Алексеевна', 4353252634, 2343, 'ИП Королева Марья Алексеевна'),
    (19, 'Поносов Петр Максимович', 22636356, 4795, 'ИП Поносов Петр Максимович'),
    (20, 'Конченных Екатерина Михаиловна', 23543252, 6465, 'ИП Конченных Екатерина Михаиловна'),
    (21, 'Деревяшкина Виктория Романовна', 345326236, 6454, 'ИП Деревяшкина Виктория Романовна'),
]
#1 поиск сотрудников
def serch1():
    table1.delete(*table1.get_children())
    for row1 in sotr:
        if fio_entry1.get() == row1[1] or int(inn_entry1.get()) == row1[3]:
            table1.insert('', tkinter.END, values=row1)
def clear1():
    table1.delete(*table1.get_children())
    for row1 in sotr:
        table1.insert('', tkinter.END, values=row1)

#2 поиск контрагентов
def serch2():
    table2.delete(*table2.get_children())
    for row2 in companies:


        if fio_entry1.get() == "" and int(inn_entry2.get()) == "":
            for row2 in companies:
                table2.insert('', tkinter.END, values=row2)


        elif fio_entry1.get() == row2[1] or int(inn_entry2.get()) == row2[3]:
            table2.insert('', tkinter.END, values=row2)


def clear2():
    table2.delete(*table2.get_children())
    for row1 in companies:
        table2.insert('', tkinter.END, values=row2)


#3 Добавление 1

def add11():
    def add12():
        sotr.append(((len(sotr) + 1), f_entry3.get()+" "+i_entry3.get()+" "+o_entry3.get(), cn_entry3.get(), inn_entry3.get(), con_entry3.get()))
        table1.delete(*table1.get_children())
        for row1 in sotr:
            table1.insert('', tkinter.END, values=row1)
    window2 = tkinter.Tk()
    window2.title("Добавление сотрудников")
    window2.geometry('1200x200')
    frame = tkinter.Frame(window2)
    frame.pack()

    # добавление сотрудников
    f_label3 = tkinter.Label(frame, text="Фамилия")
    f_label3.grid(row=0, column=0)
    f_entry3 = tkinter.Entry(frame)
    f_entry3.grid(row=1, column=0)

    i_label3 = tkinter.Label(frame, text="Имя")
    i_label3.grid(row=0, column=1)
    i_entry3 = tkinter.Entry(frame)
    i_entry3.grid(row=1, column=1)

    o_label3 = tkinter.Label(frame, text="Отчество")
    o_label3.grid(row=0, column=2)
    o_entry3 = tkinter.Entry(frame)
    o_entry3.grid(row=1, column=2)

    cn_label3 = tkinter.Label(frame, text="Снилс Сотрудника")
    cn_label3.grid(row=0, column=3)
    cn_entry3 = tkinter.Entry(frame)
    cn_entry3.grid(row=1, column=3)

    inn_label3 = tkinter.Label(frame, text="ИНН сотрудника")
    inn_label3.grid(row=0, column=4)
    inn_entry3 = tkinter.Entry(frame)
    inn_entry3.grid(row=1, column=4)

    con_label3 = tkinter.Label(frame, text="Контрагент")
    con_label3.grid(row=0, column=5)
    con_entry3 = tkinter.Entry(frame)
    con_entry3.grid(row=1, column=5)

    add_button1 = tkinter.Button(frame, text="Добавить", command=add12)
    add_button1.grid(row=1, column=6, sticky="news", padx=0)


# таблица
heads1 = ["№", "ФИО сотрудника", "   Снилс сотрудника   ", "ИНН сотрудника", "Контрагент"]
table1 = ttk.Treeview(tab1, show='headings')
scr_p1 = ttk.Scrollbar(tab1, command=table1.yview)
table1 = ttk.Treeview(tab1, show='headings', yscrollcommand=scr_p1.set)
table1.configure(yscrollcommand=scr_p1.set)
scr_p1.grid(row=2, column=3, sticky='ns')
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

sot_label1 = tkinter.Label(tab1, text="ФИО сотрудника")
sot_label1.grid(row=0, column=1)

inn_label1 = tkinter.Label(tab1, text="ИНН сотрудника")
inn_label1.grid(row=0, column=0)

fio_entry1 = tkinter.Entry(tab1)
fio_entry1.grid(row=1, column=1)

inn_entry1 = tkinter.Entry(tab1)
inn_entry1.grid(row=1, column=0)

confirm_button1 = tkinter.Button(tab1, text="Применить", command=serch1)
confirm_button1.grid(row=0, column=2, sticky="news", padx=30)

reset_button1 = tkinter.Button(tab1, text="Сбросить", command=clear1)
reset_button1.grid(row=1, column=2, sticky="news", padx=30)

add_button1 = tkinter.Button(tab1, text="Добавить", command=add11)
add_button1.grid(row=0, column=4, sticky="news", padx=0)


heads2 = ['№', 'Наименование контрагента', 'ИНН контрагента']
table2 = ttk.Treeview(tab2, show='headings')
scr_p2 = ttk.Scrollbar(tab2, command=table2.yview)
table2 = ttk.Treeview(tab2, show='headings', yscrollcommand=scr_p2.set)
table2.configure(yscrollcommand=scr_p2.set)
scr_p2.grid(row=2, column=4, sticky="ns")
window.grid_rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

company_label2 = tkinter.Label(tab2, text="Наименование контрагента")
company_label2.grid(row=0, column=0)

inn_label2 = tkinter.Label(tab2, text="ИНН контрагента")
inn_label2.grid(row=0, column=1)

cont_entry2 = tkinter.Entry(tab2)
cont_entry2.grid(row=1, column=0)

inn_entry2 = tkinter.Entry(tab2)
inn_entry2.grid(row=1, column=1)

confirm_button2 = tkinter.Button(tab2, text="Применить", command=serch2)
confirm_button2.grid(row=0, column=2, sticky="news", padx=0)

reset_button2 = tkinter.Button(tab2, text="Сбросить", command=clear2)
reset_button2.grid(row=1, column=2, sticky="news", padx=0)


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
table2.grid(row=2, column=0, columnspan=3)

window.mainloop()
