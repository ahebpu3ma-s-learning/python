import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter import *

app = tk.Tk()
app.title('Поисковая система')

app.configure(background='#ececec')

app_name = ttk.Label(app, text='Поисковое приложение',
                     font='verdana 10 italic bold', foreground= '#ff0200')
app_name.grid(row=0, column=1)

search_label = ttk.Label(app, text='Поиск')
search_label.grid(row=1, column=0)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=1, column=1)

search_engine = StringVar()
search_engine.set ("yandex")

def search():
    if text_field.get().strip() != '':
        if search_engine.get() == "google":
            webbrowser.open('https://www.google.ru/search?newwindow=1&client=opera&source=hp&ei=MGMAXcnrD-3IrgSvj4rAAw&q='
                            + text_field.get())
        elif search_engine.get() == "yandex":
            webbrowser.open('https://yandex.ru/search/?lr=213&clid=9403&oprnd=3631267571&text='
                            + text_field.get())

def searchBtn():
    search()

def enterBtn(event):
    search()

btn_search = ttk.Button(app, text = 'Найти', width=10, command = search)
btn_search.grid(row=1, column=2)

text_field.bind ('<Return>', enterBtn)

radio_google = ttk.Radiobutton(app, text = 'Google', value = 'google',
                               variable=search_engine)
radio_google.grid(row=2, column=1, sticky=E)

radio_yandex = ttk.Radiobutton(app, text = 'Яндекс', value = 'yandex',
                               variable=search_engine)
radio_yandex.grid(row=2, column=1, sticky=W)

app.wm_attributes ('-topmost', True)

text_field.focus()

app.mainloop()
