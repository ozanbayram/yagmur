#!/usr/bin/python3
# -*- encoder: utf-8 -*-

from tkinter import *
from cogs import Weather

class Yagmur(Tk):
    def __init__(self):
        super().__init__()

        self.labels = []
        self.index = 0

        self.wbg = '#030303'
        self.fg = '#FFFFFF'
        self.lbg = '#1A1A1B'
        self.font = ('Arial', 10)

        self.texts = ['Hissedilen', 'Nem', 'UV indeksi',
                      'Görünürlük', 'Çiy Noktası', 'Basınç']

        self.units = [' C', ' %', '', ' km', ' C', ' mb']

        self.icons = ['thermometer', 'humidity', 'sun',
                      'view', 'leaf', 'barometer']
        
        self.title('Yagmur')
        #self.geometry("{}x{}+{}+{}".format(winW, winH, posW, posH))
        self.resizable(0, 0)
        self.configure(bg=self.wbg)
        #self.overrideredirect(1)

        self.group = LabelFrame()
        self.group.config(bg=self.wbg, relief=FLAT,
                          padx=5, pady=5)
        self.group.pack(padx=5, pady=5)
        
    def show_table(self):
        for c in range(2):
            for r in range(3):
                info = ('\n'+self.texts[self.index]+'\n'+
                        str(self.datas[1][self.index])+
                        self.units[self.index])
                
                self.labels.append(Label(self.group, text=info))

                icon = PhotoImage(
                    file='icons/'+self.icons[self.index]+'.png')
                
                self.labels[self.index].config(
                    fg=self.fg, bg=self.lbg,
                    font=self.font,
                    image=icon,
                    width=100, height=90,
                    justify=CENTER,
                    compound=TOP,
                    anchor=CENTER,
                    padx=3, pady=3)

                self.labels[self.index].image = icon

                self.labels[self.index].grid(
                    row=c, column=r,
                    padx=3, pady=3)
                
                self.index += 1
        self.index = 0
                
    def update(self):
        self.datas = Weather().get_data()
        self.show_table()
        self.group.after(1000, self.update)

if __name__ == "__main__": 
    root = Yagmur()
    root.update()
    root.mainloop()
