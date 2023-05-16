from tkinter import *
from tkinter import ttk


def create_frame(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    # добавляем на фрейм метку
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    # добавляем на фрейм текстовое поле
    entry = ttk.Entry(frame)
    entry.pack(anchor=NW)
    # возвращаем фрейм из функции
    return frame


root = Tk()
root.title("Фильтры")
root.geometry("2000x1800")

main_frame = ttk.Frame(root)
main_frame.pack()

name_frame = ttk.LabelFrame(main_frame, text="Контрагент")
name_frame.grid(row=0, column=0, ipadx=10, ipady=10)

name_label = ttk.Label(name_frame, text="Введите контрагента")
name_label.grid(row=0, column=0, ipadx=10, ipady=10)



# for c in range(3):
#     root.columnconfigure(index=c, weight=1)
# for r in range(3):
#     root.rowconfigure(index=r, weight=1)
#
# main_frame = create_frame("Введите имя")
#
#
# name_frame = ttk.Frame( main_frame)
# name_frame = create_frame("Введите имя")
# name_frame.grid(row=1, column=2)
# name_frame.pack(anchor=NW, fill=X, padx=0, pady=100)

# email_frame = create_frame("Введите ИНН")
# email_frame.pack(anchor=NW, fill=X, padx=600, pady=0)

root.mainloop()