from tkinter import *
from datetime import datetime
import backend
from tkinter import ttk
now=datetime.now()
class feat:

    def __init__(self):
         self.day=Variable()
         self.month=Variable()
         self. year=Variable()

    def callender(self,window,x,y):
        self.day.set(now.day)
        day_label = Label(window, text="Day:", bg="white", fg="navy").place(x=x, y=y)
        day_option = OptionMenu(window,self. day,*list(range(1, 32)))
        day_option.config(fg="white", bg="navy")
        day_option.place(x=x, y=y+20)
        month_label = Label(window, text="Month:", bg="white", fg="navy").place(x=x+50, y=y)
        self.month.set(now.month)
        month_option = OptionMenu(window,self.month, *list(range(1, 13)))
        month_option.config(fg="white", bg="navy")
        month_option.place(x=x+50, y=y+20)
        month_label = Label(window, text="Year:", bg="white", fg="navy").place(x=x+100, y=y)
        self.year.set(now.year)
        year_option = OptionMenu(window, self.year,now.year-2,now.year-1,now.year,now.year+1)
        year_option.config(fg="white", bg="navy")
        year_option.place(x=x+100, y=y+20)

    def get_date(self):
        try:
            print(f"{self.day.get()}... {self.month.get()}...{self.year.get()}")
            startdate = datetime.strptime(f"{self.day.get()}/{self.month.get()}/{self.year.get() % 100}", "%d/%m/%y").date()
            return  startdate
        except:
            pass



def treeview():
    treeview_window=Toplevel()
    treeview_window.geometry("1200x600")
    treeview_window.resizable(False, False)
    treeview_window.title("Tree View!")
    treeview_window.config(bg="white",highlightthickness=2, highlightcolor="navy")
    treeview_window.grab_set()
    treeview_window.focus_set()
    style=ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=20,fieldbackground="#D3D3D3")
    style.map("Treeview",backgroud=[("selected","#347083 ")]      )

    # tree frame
    treeframe=Frame(treeview_window)
    treeframe.pack(pady=10)
    tscrollbar=Scrollbar(treeframe)
    tscrollbar.pack(side=RIGHT,fill=Y)


    database= ttk.Treeview(treeframe,yscrollcommand=tscrollbar.set,selectmode="extended")
    database.pack()

    tscrollbar.config(command=database.yview)
    columns=backend.df.columns.tolist()
    database["columns"]=tuple(columns)
    database.column('#0', width=0, stretch=NO)
    database.heading('#0', text='', anchor=CENTER)
    # style
    width=90
    for col in columns:
        if col=="Discount_amount":
            width=130
        database.column(col,width=width,anchor=CENTER)
        database.heading(col,text=col,anchor=CENTER)
    rows=backend.c.execute("SELECT * FROM CUSTOMERS").fetchall()
    database.tag_configure('oddrow',background="white")
    database.tag_configure('evenrow',background="lightblue")
    for row in rows:
        if row[0]%2==0:
            database.insert("",index="end",values=row,tags=('evenrow', ))
        else:
            database.insert("",index="end",values=row,tags=('oddrow', ))



