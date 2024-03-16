import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
from datetime import *
from dateutil.relativedelta import *
import backend
import features
# permission = True
now = datetime.now()

"""
qualitycheck=Tk()
qualitycheck.geometry("300x150")
qualitycheck.title("Source Code")
qualitycheck.resizable(False, False)
qualitycheck.config(bg="white")
def source_check():
if sourceCode_entry.get() != "yWH^MtPLme4WTbU&tt9G":
    sys.exit()
else :
    global  permission
    permission=True
    qualitycheck.destroy()



sorcecode_label = Label(qualitycheck, text="Enter Source code :", font=20, fg="navy", bg="white").place(x=10, y=5)
sourceCode_entry = Entry(qualitycheck, width=30, highlightthickness=2, highlightbackground="navy")
sourceCode_entry.place(x=40, y=55)
SourceCode_btn=Button(qualitycheck,text="Enter", bg="navy",fg="white",command=source_check).place(x=250,y=53)
# source code function







qualitycheck.mainloop()
"""


window = Tk()
window.geometry("600x450")
window.title("Reception")
window.resizable(False, False)
window.config(highlightthickness=2, highlightcolor="navy")
bg_image = PhotoImage(file='bluegymlogo.png')
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# search:

search_label = Label(window, text="Search :  (Enter ID or Name)",
                        font=20, fg="navy", bg="white").place(x=10, y=5)
search_entry = Entry(
    window, width=50, highlightthickness=2, highlightbackground="navy")
search_entry.place(x=10, y=25)

def search(*args):
    def memberinfo(x=0):
        backend.update_dataframe()
        info = Toplevel()
        info.geometry("250x250")
        info.resizable(False, False)
        info.title("Search")
        info.config(bg="white", highlightthickness=2,
                    highlightcolor="navy")
        info.grab_set()
        info.focus_set()
        color = "white"
        if x == 1:
            record1 = backend.df[backend.df.ID == int(search_entry.get())]
            if record1["End_date"].item() <= str(date.today()):
                color = "firebrick1"
            info_box1 = Listbox(info, height=50,
                                width=50,
                                bg=color,
                                activestyle='dotbox',
                                fg="navy", font='bold')

            for i in range(len(record1.columns)):
                info_box1.insert(
                    1, f"{record1.columns[-i]}   :   {record1.iloc[0][-i]}")
            info_box1.pack()
        elif x == 2:
            record2 = backend.df[backend.df.Name == (search_entry.get())]
            if record2["End_date"].item() <= str(date.today()):
                color = "firebrick1"
            info_box2 = Listbox(info, height=50,
                                width=50,
                                bg=color,
                                activestyle='dotbox',
                                fg="navy", font='bold')
            for i in range(len(record2.columns)):
                info_box2.insert(
                    1, f"{record2.columns[-i]}   :   {record2.iloc[0][-i]}")
            info_box2.pack()

    backend.update_dataframe()
    if search_entry.get().isnumeric():
        if int(search_entry.get()) in list(backend.df.ID):
            memberinfo(1)
        else:
            messagebox.showwarning("caution", " user not found ")
    else:
        if search_entry.get() in backend.df.Name.tolist():
            memberinfo(2)
        else:
            messagebox.showwarning("caution", " user not found ")
    search_entry.delete(0, END)
search_entry.bind("<Return>", search)


# new customer button


def newcustomer_command():
    customer_input = Toplevel()
    customer_input.focus_set()
    customer_input.grab_set()
    customer_input.title("Add member")
    customer_input.resizable(False, False)
    customer_input.config(
        bg="white", highlightthickness=2, highlightcolor="navy")
    customer_input.geometry("800x300")

    # name
    name_label = Label(customer_input, text="Name:", bg="white", fg="navy")
    name_label.place(x=50, y=30)
    name_box = Entry(customer_input, width=50,
                        highlightthickness=2, highlightbackground="navy")
    name_box.place(x=50, y=50)
    # phone
    phone_label = Label(
        customer_input, text="phone number:", bg="white", fg="navy")
    phone_label.place(x=400, y=30)
    phone_box = Entry(customer_input, width=50,
                        highlightthickness=2, highlightbackground="navy")
    phone_box.place(x=400, y=50)
    # gender
    gender = StringVar()
    gender.set("Gender...")
    gender_option = OptionMenu(
        customer_input, gender, "Male", "Female", gender.get())
    gender_option.place(x=50, y=150)
    gender_option.config(bg="navy", fg="white")
    gender_label = Label(
        customer_input, text="Gender:", bg="white", fg="navy")
    gender_label.place(x=50, y=130)
    # subscribtion type:
    subscribtiontype_label = Label(
        customer_input, text="Pack type:", bg="white", fg="navy").place(x=230, y=130)
    subscribtion_type = StringVar()
    subscribtion_type.set("Type..")

    def refreshdur(*args):
        if subscribtion_type.get() != "Type..":
            pack_option["menu"].delete(0, "end")
            a = list(backend.dfpacks[backend.dfpacks.pack_type ==
                        subscribtion_type.get()]["pack_duration"])
            if len(a) == 0:
                pack_option["menu"].delete(0, "end")
                pack_option["menu"].add_command(
                    label="Duration..", command=tk._setit(pack, "Duration.."))
                pack.set("Duration..")
                return
            b = list()
            for i in range(len(a)):
                b.append(int(a[i][0:2]))
            b = sorted(b)
            c = list()
            for i in b:
                i = f"{i} Months"
                c.append(i)
            for opt in c:
                pack_option["menu"].add_command(
                    label=opt, command=tk._setit(pack, opt))
            pack.set("Duration..")
        else:
            pack_option["menu"].delete(0, "end")
            pack_option["menu"].add_command(
                label="Duration..", command=tk._setit(pack, "Duration.."))
            pack.set("Duration..")

    subscribtiontype_option = OptionMenu(customer_input, subscribtion_type, *backend.dfpacks.pack_type.unique(),
                                            subscribtion_type.get(), command=refreshdur)
    subscribtiontype_option.config(fg="white", bg="navy")
    subscribtiontype_option.place(x=230, y=150)
    # pack duration
    pack = StringVar()
    pack.set("Duration..")

    def refreshpaid(*args):
        if pack.get() == "Duration..":
            paid_box.delete(0, END)
            paid_box.insert(END, 0)

            return
        else:
            a = int()
            try:
                a = backend.dfpacks[
                    (backend.dfpacks.pack_type == subscribtion_type.get()) & (backend.dfpacks.pack_duration == pack.get())][
                    "price"].values[0]
            except:
                pass
            paid_box.delete(0, END)
            paidamount.set(a)
            paid_box.insert(END, paidamount.get())
            pass

    pack_option = OptionMenu(customer_input, pack, pack.get())
    pack_option.place(x=400, y=150)
    pack_option.config(bg="navy", fg="white")
    pack_label = Label(
        customer_input, text="Pack Duration:", bg="white", fg="navy")
    pack_label.place(x=400, y=130)
    pack.trace("w", refreshpaid)

    # paid
    paidamount = IntVar()
    paidamount.set(0)
    paid_box = Entry(customer_input, highlightthickness=2,
                        highlightbackground="navy")
    paid_box.place(x=550, y=155)
    paid_box.insert(END, paidamount.get())
    paid_label = Label(
        customer_input, text="paid amount:", bg="white", fg="navy")
    paid_label.place(x=550, y=130)
    # start date:
    start_date_label = Label(
        customer_input, text="Start Date :", bg="white", fg="navy").place(x=50, y=200)
    day = IntVar()
    day.set(now.day)
    day_label = Label(customer_input, text="Day:",
                        bg="white", fg="navy").place(x=50, y=220)
    day_option = OptionMenu(customer_input, day, *list(range(1, 32)))
    day_option.config(fg="white", bg="navy")
    day_option.place(x=50, y=240)
    month_label = Label(customer_input, text="Month:",
                        bg="white", fg="navy").place(x=100, y=220)
    month = IntVar()
    month.set(now.month)
    month_option = OptionMenu(customer_input, month, *list(range(1, 13)))
    month_option.config(fg="white", bg="navy")
    month_option.place(x=100, y=240)
    month_label = Label(customer_input, text="Year:",
                        bg="white", fg="navy").place(x=150, y=220)
    year = IntVar()
    year.set(now.year)
    year_option = OptionMenu(
        customer_input, year, now.year - 2, now.year - 1, now.year, now.year + 1)
    year_option.config(fg="white", bg="navy")
    year_option.place(x=150, y=240)
    # discount:
    Label(customer_input, text="Discount Amount: ",
            bg="white", fg="navy").place(x=300, y=220)
    discountamount = IntVar()
    discountamount.set(0)
    discount_box = Entry(customer_input, textvariable=discountamount,
                            highlightthickness=2, highlightbackground="navy")
    discount_box.place(x=300, y=245)

    # submit
    def submit(*args):
        if phone_box.get().isnumeric() == False or name_box.get().isnumeric() == True or pack.get() == "Duration.." or gender.get() == "Gender..." or subscribtion_type.get() == "Type..":
            messagebox.showinfo("ERROR", "Wrong input! ,try again")
            return
        a = backend.dfpacks[
            (backend.dfpacks.pack_type == subscribtion_type.get()) & (backend.dfpacks.pack_duration == pack.get())][
            "price"].values[0]
        backend.update_dataframe()
        if int(paid_box.get()) > a:
            messagebox.showinfo(
                "ERROR", "The paid amount is bigger than the pack price!")
            return
        if int(discount_box.get()) > a:
            messagebox.showinfo(
                "ERROR", "The discount amount is bigger than the pack price!")
            return
        if int(paid_box.get()) == a and int(discount_box.get()) > 0:
            messagebox.showinfo(
                "ERROR", "cannot pay full amount when the discount is not zero")
            return
        if int(paid_box.get())+int(discount_box.get()) > a:
            messagebox.showinfo(
                "ERROR", "discount amount must be in the range of the pack price and paid amount")
            return
        if not paid_box.get().isnumeric():
            messagebox.showinfo("ERROR", "Wrong input! ,try again")
            return
        if discount_box.get().isnumeric() == False:
            messagebox.showinfo("ERROR", "Wrong input! ,try again")
            return
        if name_box.get() in list(backend.df.Name):
            messagebox.showinfo(
                "ERROR", f"\"{name_box.get()}\" Already exists !")
            return
        if int(paid_box.get()) < 0 or int(discount_box.get()) < 0:
            messagebox.showinfo("ERROR", "Wrong input! ,try again")
            return

        try:
            startdate = datetime.strptime(
                f"{month.get()}/{day.get()}/{year.get() % 100}", "%m/%d/%y").date()
        except:
            messagebox.showwarning(
                "error", "Please Check the Date you have entered .")
            return
        endDate = startdate + relativedelta(months=int(pack.get()[0:2]))
        backend.adding_record(name_box.get(), phone_box.get(), gender.get(), pack.get(), subscribtion_type.get(),
                                int(int(paid_box.get())+int(discount_box.get()) - a), startdate, endDate, int(paid_box.get()), now.date(), int(discount_box.get()))
        # history
        backend.adding_recordtoHistory(backend.get_id(), name_box.get(), phone_box.get(), gender.get(), pack.get(), subscribtion_type.get(),
                                        int(int(paid_box.get())+int(discount_box.get()) - a), startdate, endDate, int(paid_box.get()), now.date(), int(discount_box.get()))

        name_box.delete(0, END)
        phone_box.delete(0, END)
        gender.set("Gender...")
        pack.set("Pack...")
        subscribtion_type.set("type..")
        customer_input.destroy()
        messagebox.showinfo("welcome", "member added successfully!")
    submit_button = Button(customer_input, text="Submit.",
                            width=20, height=2, command=submit, bg="navy", fg="white")
    submit_button.place(x=600, y=250)

newcustomer_button = Button(window, text="New Member", pady=10, padx=50, highlightbackground="white",
                            command=newcustomer_command, bg="navy", fg="white", font=60)
newcustomer_button.place(x=10, y=390)


# view records:


def filter_Search():
    filter_window = Toplevel()
    filter_window.geometry("800x600")
    filter_window.resizable(False, False)
    filter_window.title("Search")
    filter_window.config(
        bg="white", highlightthickness=2, highlightcolor="navy")
    filter_window.grab_set()
    filter_window.focus_set()
    feats1 = features.feat()
    feats2 = features.feat()

    # tree view button

    treeButton = Button(filter_window, text="Tree view", pady=10, padx=10, highlightbackground="white",
                        bg="navy", fg="white", font=60, command=features.treeview).place(x=500, y=540)

    # filter by
    Label(filter_window, text="Filter by :", font=20,
            fg="navy", bg="white").place(x=10, y=5)
    # Date
    Label(filter_window, text="Date :", font=20,
            fg="navy", bg="white").place(x=10, y=40)
    Label(filter_window, text="FROM  :",
            bg="white", fg="navy").place(x=10, y=90)
    feats1.callender(filter_window, 40, 120)
    Label(filter_window, text=" <===========> ",
            bg="white", fg="navy").place(x=270, y=140)
    Label(filter_window, text="TO :", bg="white",
            fg="navy").place(x=400, y=90)
    feats2.callender(filter_window, 430, 120)
    Label(filter_window, text="==============================================================================================",
            bg="white", fg="navy").place(x=10, y=180)
    # subscription type
    Label(filter_window, text="Subscription Type :",
            font=20, fg="navy", bg="white").place(x=10, y=220)
    subscribtion_type = StringVar()
    subscribtion_type.set("ALL")
    subscribtiontype_option = OptionMenu(filter_window, subscribtion_type, *backend.dfpacks.pack_type.unique(),
                                            subscribtion_type.get())
    subscribtiontype_option.config(fg="white", bg="navy")
    subscribtiontype_option.place(x=100, y=260)
    Label(filter_window, text="==============================================================================================",
            bg="white", fg="navy").place(x=10, y=320)
    # Gender
    Label(filter_window, text="Gender :", font=20,
            fg="navy", bg="white").place(x=470, y=220)
    genders = {"All": " ",
                "Female": "AND Gender=\'Female\' ",
                "Male": "AND Gender=\'Male\'"}
    g = StringVar(filter_window, " ")
    i = 500
    for (text, value) in genders.items():
        Radiobutton(filter_window, text=text, variable=g,
                    value=value, fg="navy", bg="white").place(y=270, x=i)
        i += 100
    # Balance
    Label(filter_window, text="Balance :", font=20,
            fg="navy", bg="white").place(x=10, y=350)
    Balance = {"All": "<1",
                " in dept": "<0",
                "dept Free": "=0"}
    v = StringVar()
    v.set("<1")
    i = 50
    for (text, value) in Balance.items():
        Radiobutton(filter_window, text=text, variable=v,
                    value=value, fg="navy", bg="white").place(y=400, x=i)
        i += 100
    Date = {"paid date": "paid_date",

            " start date": " Start_date",
            "end date": "End_date"}
    datev = StringVar()
    datev.set("paid_date")
    i = 100
    for (text, value) in Date.items():
        Radiobutton(filter_window, text=text, variable=datev,
                    value=value, fg="navy", bg="white").place(y=60, x=i)
        i += 100

    def fltrsrch():
        if subscribtion_type.get() == "ALL":
            backend.filter_search(datev.get(), feats1.get_date(
            ), feats2.get_date(), v.get(), " ", g.get())
        else:
            backend.filter_search(datev.get(), feats1.get_date(), feats2.get_date(
            ), v.get(), f"AND   pack_type=\'{subscribtion_type.get()}\'", g.get())

    Label(filter_window, text="==============================================================================================",
            bg="white", fg="navy").place(x=10, y=460)

    # Search button

    Button(filter_window, text="Search", pady=10, padx=10, highlightbackground="white",
            bg="navy", fg="white", font=60, command=fltrsrch).place(x=700, y=540)

    def all():
        backend.df_history.to_excel(
            r"BlueGym_Excel\bluegym_customers.xlsx", sheet_name='Bluegym customers', index=False)
        os.startfile(r"BlueGym_Excel\bluegym_customers.xlsx")
    Button(filter_window, text="Show All Customers", pady=10, padx=10, highlightbackground="white",
            bg="navy", fg="white", font=60, command=all).place(x=10, y=540)

gyminfo_button = Button(window, text="Search By Filter", padx=40, pady=10, command=filter_Search, bg="navy", fg="white",
                        font=60)
gyminfo_button.place(x=390, y=390)


# update screen


def update_home():
    update_screen = Toplevel()
    update_screen.geometry("500x190")
    update_screen.resizable(False, False)
    update_screen.title("Update screen")
    update_screen.config(
        bg="white", highlightthickness=2, highlightcolor="navy")
    update_screen.grab_set()
    update_screen.focus_set()

    # ==========================================update membership button=============================================

    def update_membership():
        update_screen.destroy()
        update_window = Toplevel()
        update_window.geometry("600x200")
        update_window.resizable(False, False)
        update_window.title("Update member")
        update_window.config(
            bg="white", highlightthickness=2, highlightcolor="navy")
        update_window.grab_set()
        update_window.focus_set()
        name_label = Label(
            update_window, text="Name or ID:", bg="white", fg="navy")
        name_label.place(x=40, y=20)
        name_box = Entry(update_window, width=50,
                            highlightthickness=2, highlightbackground="navy")
        name_box.place(x=40, y=40)

        # start date:
        start_date_label = Label(
            update_window, text="Start Date :", bg="white", fg="navy").place(x=370, y=10)
        day = IntVar()
        day.set(now.day)
        day_label = Label(update_window, text="Day:",
                            bg="white", fg="navy").place(x=370, y=30)
        day_option = OptionMenu(update_window, day, *list(range(1, 32)))
        day_option.config(fg="white", bg="navy")
        day_option.place(x=370, y=50)
        month_label = Label(update_window, text="Month:",
                            bg="white", fg="navy").place(x=420, y=30)
        month = IntVar()
        month.set(now.month)
        month_option = OptionMenu(
            update_window, month, *list(range(1, 13)))
        month_option.config(fg="white", bg="navy")
        month_option.place(x=420, y=50)
        month_label = Label(update_window, text="Year:",
                            bg="white", fg="navy").place(x=470, y=30)
        year = IntVar()
        year.set(now.year)
        year_option = OptionMenu(
            update_window, year, now.year - 2, now.year - 1, now.year, now.year + 1)
        year_option.config(fg="white", bg="navy")
        year_option.place(x=470, y=50)
        subscribtiontype_label = Label(
            update_window, text="Pack type:", bg="white", fg="navy").place(x=50, y=90)
        subscribtion_type = StringVar()
        subscribtion_type.set("Type..")

        def refreshdur(*args):
            if subscribtion_type.get() != "Type..":
                pack_option["menu"].delete(0, "end")
                a = list(
                    backend.dfpacks[backend.dfpacks.pack_type == subscribtion_type.get()]["pack_duration"])
                if len(a) == 0:
                    pack_option["menu"].delete(0, "end")
                    pack_option["menu"].add_command(
                        label="Duration..", command=tk._setit(pack, "Duration.."))
                    pack.set("Duration..")
                    return
                b = list()
                for i in range(len(a)):
                    b.append(int(a[i][0:2]))
                b = sorted(b)
                c = list()
                for i in b:
                    i = f"{i} Months"
                    c.append(i)
                for opt in c:
                    pack_option["menu"].add_command(
                        label=opt, command=tk._setit(pack, opt))
                pack.set("Duration..")
            else:
                pack_option["menu"].delete(0, "end")
                pack_option["menu"].add_command(
                    label="Duration..", command=tk._setit(pack, "Duration.."))
                pack.set("Duration..")
        subscribtiontype_option = OptionMenu(update_window, subscribtion_type, *backend.dfpacks.pack_type.unique(),
                                                subscribtion_type.get(), command=refreshdur)
        subscribtiontype_option.config(fg="white", bg="navy")
        subscribtiontype_option.place(x=50, y=110)

        def refreshpaid(*args):
            if pack.get() == "Duration..":
                paid_box.delete(0, END)
                paid_box.insert(END, 0)

                return
            else:
                a = int()
                try:
                    a = backend.dfpacks[(backend.dfpacks.pack_type == subscribtion_type.get()) & (
                        backend.dfpacks.pack_duration == pack.get())]["price"].item()
                except:
                    pass
                paid_box.delete(0, END)
                paidamount.set(a)
                paid_box.insert(END, paidamount.get())
                pass
        pack = StringVar()
        pack.set("Duration..")
        pack_option = OptionMenu(update_window, pack, pack.get())
        pack_option.place(x=200, y=110)
        pack_option.config(bg="navy", fg="white")
        pack_label = Label(
            update_window, text="pack Duration:", bg="white", fg="navy")
        pack_label.place(x=200, y=90)
        paidamount = IntVar()
        paidamount.set(0)
        paid_box = Entry(update_window, highlightthickness=2,
                            highlightbackground="navy")
        paid_box.place(x=400, y=115)
        paid_box.insert(END, paidamount.get())
        paid_label = Label(
            update_window, text="paid amount:", bg="white", fg="navy")
        paid_label.place(x=400, y=90)
        pack.trace("w", refreshpaid)

        def submit(*args):
            a = backend.dfpacks[
                (backend.dfpacks.pack_type == subscribtion_type.get()) & (backend.dfpacks.pack_duration == pack.get())][
                "price"].values[0]
            if pack.get() == "Pack..." or subscribtion_type.get() == "type..":
                messagebox.showinfo("ERROR", "Wrong input! ,try again")
                return
            if name_box.get().isnumeric():
                if int(name_box.get()) not in list(backend.df.ID):
                    messagebox.showinfo("caution", " user not found ")
                    return
            else:
                if name_box.get() not in list(backend.df.Name):
                    messagebox.showinfo("caution", " user not found ")
                    return
            try:
                startdate = datetime.strptime(
                    f"{month.get()}/{day.get()}/{year.get() % 100}", "%m/%d/%y").date()
            except:
                messagebox.showwarning(
                    "error", "Please Check the Date you have entered .")
                return
            end = startdate + relativedelta(months=int(pack.get()[0]))

            backend.updaterecord(name_box.get(), pack.get(), subscribtion_type.get(),
                                    int(int(paid_box.get())-a), int(paid_box.get()), startdate, end, now.date())
            record = backend.addinghistory(name_box.get())
            backend.adding_recordtoHistory(record[0], record[1], record[2], record[3], pack.get(
            ), subscribtion_type.get(), int(int(paid_box.get())-a), startdate, end, paid_box.get(), now.date(), 0)
            name_box.delete(0, END)
            pack.set("Pack...")
            update_window.destroy()
            messagebox.showinfo("welcome", "member updated successfully!")

        submit_button = Button(update_window, text="Update.",
                                command=submit, width=20, height=2, bg="navy", fg="white")
        submit_button.place(x=400, y=150)

    updatemembership_button = Button(update_screen, text="Update Membership", padx=30, pady=10, bg="navy", fg="white",
                                        font=60, command=update_membership)
    updatemembership_button.place(x=30, y=30)

    # ========================================update debt button======================================================
    def pay_dept():
        update_screen.destroy()
        paydept = Toplevel()
        paydept.geometry("450x150")
        paydept.resizable(False, False)
        paydept.title("Update screen")
        paydept.config(bg="white", highlightthickness=2,
                        highlightcolor="navy")
        paydept.grab_set()
        paydept.focus_set()
        # name
        name_label = Label(paydept, text="Name or ID:",
                            bg="white", fg="navy")
        name_label.place(x=40, y=20)
        name_box = Entry(paydept, width=20,
                            highlightthickness=2, highlightbackground="navy")
        name_box.place(x=40, y=40)
        # paid
        paid_box = Entry(paydept, highlightthickness=2,
                            highlightbackground="navy")
        paid_box.place(x=250, y=40)
        paid_box.insert(END, paid_box.get())
        paid_label = Label(paydept, text="paid amount:",
                            bg="white", fg="navy")
        paid_label.place(x=250, y=19)

        # submit
        def submit(*args):
            if not paid_box.get().isnumeric():
                messagebox.showinfo("ERROR", "Wrong input! ,try again")
                return
            if int(paid_box.get()) < 0:
                messagebox.showinfo("ERROR", "Wrong input! ,try again")
                return
            if name_box.get().isnumeric():
                num = 1
                if int(name_box.get()) not in list(backend.df.ID):
                    messagebox.showinfo("caution", " user not found ")
                    return
            else:
                num = 0
                if name_box.get() not in list(backend.df.Name):
                    messagebox.showinfo("caution", " user not found ")
                    return
            if num:
                if backend.df.loc[backend.df.ID == int(name_box.get()), "Balance"].item() == 0:
                    messagebox.showinfo(
                        "info", "the customer already have no debt")
                    return
            else:
                if backend.df[backend.df.Name == name_box.get()]["Balance"].item() == 0:
                    messagebox.showinfo(
                        "info", "the customer already have no debt")
                    return
            # check if paid more than debt
            if num:
                if backend.df.loc[backend.df.ID == int(name_box.get()), "Balance"].item() + int(paid_box.get()) > 0:
                    messagebox.showinfo(
                        "info", "the paid amount is bigger than the actual debt!")
                    return
            else:
                if backend.df[backend.df.Name == name_box.get()]["Balance"].item() + int(paid_box.get()) > 0:
                    messagebox.showinfo(
                        "info", "the paid amount is bigger than the actual debt!")
                    return
            backend.updatedept(name_box.get(), int(paid_box.get()))
            name_box.delete(0, END)
            paydept.destroy()
            messagebox.showinfo("update", "dept paid successfully!")
            backend.update_dataframe()

        submit_button = Button(
            paydept, text="Submit", bg="navy", fg="white", font=60, command=submit)
        submit_button.place(x=200, y=100)

    paydebt_button = Button(update_screen, text="Pay Debt", padx=30, pady=10, bg="navy", fg="white", font=60,
                            command=pay_dept)
    paydebt_button.place(x=300, y=30)

    # =====================================delete member==============================================================

    def delete_record():
        update_screen.destroy()
        deleteRec = Toplevel()
        deleteRec.geometry("350x100")
        deleteRec.resizable(False, False)
        deleteRec.title("Update screen")
        deleteRec.config(bg="white", highlightthickness=2,
                            highlightcolor="navy")
        deleteRec.grab_set()
        deleteRec.focus_set()
        # name
        name_label = Label(deleteRec, text="Name or ID:",
                            bg="white", fg="navy")
        name_label.place(x=30, y=20)
        name_box = Entry(deleteRec, width=20,
                            highlightthickness=2, highlightbackground="navy")
        name_box.place(x=30, y=40)

        # delete record button
        def delete():
            if name_box.get().isnumeric():
                num = 1
                if int(name_box.get()) not in list(backend.df.ID):
                    messagebox.showinfo("caution", " user not found ")
                    return
            else:
                num = 0
                if name_box.get() not in list(backend.df.Name):
                    messagebox.showinfo("caution", " user not found ")
                    return
            if num:
                name = backend.df.loc[backend.df.ID ==
                                        int(name_box.get()), "Name"].item()
                ask = messagebox.askquestion(
                    "Delete Member!", f"Are you sure you want to Delete \'{name}\' info ?")
                if ask == 'yes':
                    backend.DeleteRecord(int(name_box.get()))
                    backend.update_dataframe()
                    deleteRec.destroy()
                    messagebox.showinfo(
                        "info", f"\"{name}\" Record is Deleted succesfully.")
            else:
                name = backend.df[backend.df.Name ==
                                    name_box.get()]["Name"].item()
                id = backend.df[backend.df.Name ==
                                name_box.get()]["ID"].item()
                print(id)
                ask = messagebox.askquestion(
                    "Delete Member!", f"Are you sure you want to Delete \'{name}\' info ?")
                if ask == 'yes':
                    backend.DeleteRecord(id)
                    deleteRec.destroy()
                    messagebox.showinfo(
                        "info", f"\"{name}\" Record is Deleted succesfully.")

        delete_button = Button(deleteRec, text="Delete Member", padx=10, pady=5, bg="navy", fg="white", font=60,
                                command=delete)
        delete_button.place(x=200, y=30)

    DeleteRecord_button = Button(update_screen, text="Delete Member", padx=30, pady=10, bg="red", fg="white",
                                    font=60, command=delete_record)
    DeleteRecord_button.place(x=30, y=110)

    # =====================================delete all records=========================================================

    def delete_Allrecords():
        ask = messagebox.askquestion(
            "Delete All Records!", "Are you sure you want to Delete All the Records ?!")
        if ask == "yes":
            backend.DeleteAllRecord()
            update_screen.destroy()
            messagebox.showinfo(
                "info", " All Records Are Deleted succesfully.")

    DeleteAllRecords_button = Button(update_screen, text="Delete All Records", padx=30, pady=10, bg="red", fg="white",
                                        font=60, command=delete_Allrecords)
    DeleteAllRecords_button.place(x=270, y=110)

update_button = Button(window, text="Update", padx=50, pady=10, bg="navy", fg="white", font=60,
                        command=update_home)
update_button.place(x=10, y=335)


# contact us


def contact():
    messagebox.showinfo(
        "info", " number : 0799048662. \n Email:ewiwisaif5@gmail.com. \n done by: SkiRaz.", )

contact_button = Button(window, text="Contact us..", padx=30,
                        pady=10, bg="navy", fg="white", font=60, command=contact)
contact_button.place(x=437, y=10)


# edit


def edit():
    edit_window = Toplevel()
    edit_window.geometry("620x200")
    edit_window.resizable(False, False)
    edit_window.title("Edit ")
    edit_window.config(bg="white", highlightthickness=2,
                        highlightcolor="navy")
    edit_window.grab_set()
    edit_window.focus_set()
    # ============================ edit packs ========================================
    windowinfo = Label(edit_window, text="Change or Add Subscription Packs Info:",
                        bg="white", fg="navy", font=("bold"))
    windowinfo.place(x=20, y=10)
    # pack_type:
    packtypelabel = Label(
        edit_window, text="Pack Type :", bg="white", fg="navy")
    packtypelabel.place(x=50, y=50)
    packtype = StringVar()
    packtype.set("Type..")
    packtypeoptions = OptionMenu(
        edit_window, packtype, packtype.get(), *backend.dfpacktypes.packtype)
    packtypeoptions.config(fg="white", bg="navy")
    packtypeoptions.place(x=50, y=70)
    # pack duration:
    packdurlabel = Label(
        edit_window, text="Pack Duration :", bg="white", fg="navy")
    packdurlabel.place(x=175, y=50)
    packdur = StringVar()
    packdur.set("Duaration..")
    packduroptions = OptionMenu(
        edit_window, packdur, packdur.get(), *backend.sortdur())
    packduroptions.config(fg="white", bg="navy")
    packduroptions.place(x=175, y=70)
    # price :
    packpricelabel = Label(
        edit_window, text="Pack Price :", bg="white", fg="navy")
    packpricelabel.place(x=310, y=50)
    price = IntVar()
    price_box = Entry(edit_window, textvariable=price, width=20,
                        highlightthickness=2, highlightbackground="navy")
    price_box.place(x=310, y=75)

    # add / delete pack :
    def adddel_type():
        adddelpack_window = Toplevel()
        adddelpack_window.geometry("300x100")
        adddelpack_window.resizable(False, False)
        adddelpack_window.title("Edit ")
        adddelpack_window.config(
            bg="white", highlightthickness=2, highlightcolor="navy")
        adddelpack_window.grab_set()
        adddelpack_window.focus_set()

        # Add pack:
        def add_pack():
            addpack_window = Toplevel()
            addpack_window.geometry("300x100")
            addpack_window.resizable(False, False)
            addpack_window.title("Edit ")
            addpack_window.config(
                bg="white", highlightthickness=2, highlightcolor="navy")
            addpack_window.grab_set()
            addpack_window.focus_set()
            # type:
            name_label = Label(
                addpack_window, text="Enter New Type Name:", bg="white", fg="navy")
            name_label.place(x=20, y=30)
            name_box = Entry(addpack_window, width=30,
                                highlightthickness=2, highlightbackground="navy")
            name_box.place(x=20, y=50)

            # add buton:
            def add():
                if name_box.get().isnumeric() == True or name_box.get() == "":
                    messagebox.showwarning("error", "Wrong input")
                    return
                backend.addpacktype(name_box.get())
                name_box.delete(0, END)
                adddelpack_window.destroy()
                addpack_window.destroy()
                edit_window.destroy()
                edit()
                messagebox.showinfo("info", "Pack type added succesfully")

            addbutton = Button(
                addpack_window, text="Add+", bg="navy", pady=5, padx=10, fg="white", command=add)
            addbutton.place(x=220, y=40)

        def del_pack():
            delpack_window = Toplevel()
            delpack_window.geometry("300x100")
            delpack_window.resizable(False, False)
            delpack_window.title("Edit ")
            delpack_window.config(
                bg="white", highlightthickness=2, highlightcolor="navy")
            delpack_window.grab_set()
            delpack_window.focus_set()
            # types options:
            type = StringVar()
            type.set("Type..")
            label = Label(delpack_window, text="Choose The Pack type you Want to Delete:", bg="white", fg="navy").place(
                x=20, y=20)
            types = OptionMenu(delpack_window, type,
                                type.get(), *backend.dfpacktypes.packtype)
            types.config(fg="white", bg="navy", padx=40)
            types.place(x=20, y=40)

            # delete button:
            def dele():
                if type.get() == "Type..":
                    messagebox.showwarning(
                        "error", "Please Choose a Type!")
                    return
                backend.deletepacktype(type.get())
                delpack_window.destroy()
                adddelpack_window.destroy()
                delpack_window.destroy()
                edit_window.destroy()
                edit()
                messagebox.showinfo("info", "Type Deleted succesfully")

            delbutton = Button(delpack_window, text="Delete-",
                                bg="red", pady=5, padx=10, fg="white", command=dele)
            delbutton.place(x=220, y=40)

        AddpackButton = Button(adddelpack_window, text="Add pack Type.", bg="navy", fg="white", pady=20, font=20,
                                command=add_pack)
        AddpackButton.place(x=10, y=20)

        delpackButton = Button(adddelpack_window, text="Delete pack Type.", bg="red", fg="white", pady=20, font=20,
                                command=del_pack)
        delpackButton.place(x=150, y=20)

    AddDeletepack = Button(
        edit_window, text="Add / Delete Type.", bg="navy", fg="white", command=adddel_type)
    AddDeletepack.place(x=320, y=160)

    # add / delete pack :
    def adddel_dur():
        adddeldur_window = Toplevel()
        adddeldur_window.geometry("360x100")
        adddeldur_window.resizable(False, False)
        adddeldur_window.title("Edit ")
        adddeldur_window.config(
            bg="white", highlightthickness=2, highlightcolor="navy")
        adddeldur_window.grab_set()
        adddeldur_window.focus_set()

        # Add dur:
        def add_dur():
            adddur_window = Toplevel()
            adddur_window.geometry("300x100")
            adddur_window.resizable(False, False)
            adddur_window.title("Edit ")
            adddur_window.config(
                bg="white", highlightthickness=2, highlightcolor="navy")
            adddur_window.grab_set()
            adddur_window.focus_set()
            # type:
            name_label = Label(
                adddur_window, text="Enter New Duration's Number of months:", bg="white", fg="navy")
            name_label.place(x=20, y=20)
            name_box = Entry(adddur_window, width=10,
                                highlightthickness=2, highlightbackground="navy")
            name_box.place(x=80, y=50)
            Label(adddur_window, text="Months : ",
                    fg="navy", bg="white").place(x=10, y=50)

            # add buton:
            def add():
                if name_box.get() == "":
                    messagebox.showwarning("error", "Wrong input")
                    return
                if name_box.get().isnumeric() == False:
                    messagebox.showwarning("error", "Wrong input")
                    return
                if int(name_box.get()) <= 0:
                    messagebox.showwarning("error", "Wrong input")
                    return
                if int(name_box.get()) >= 99:
                    messagebox.showwarning(
                        "error", "number of months too big")
                    return
                months = f"{name_box.get()} Months"
                if months in list(backend.dfpackdurations.packduration):
                    messagebox.showinfo(
                        "info", f"\"{months}\" Already Exists")
                    return
                backend.addpackduration(months)
                name_box.delete(0, END)
                adddeldur_window.destroy()
                adddur_window.destroy()
                edit_window.destroy()
                edit()
                messagebox.showinfo(
                    "info", "Pack Duration added succesfully")

            addbutton = Button(
                adddur_window, text="Add+", bg="navy", pady=5, padx=10, fg="white", command=add)
            addbutton.place(x=220, y=45)

        # del dur
        def del_dur():
            deldur_window = Toplevel()
            deldur_window.geometry("300x100")
            deldur_window.resizable(False, False)
            deldur_window.title("Edit ")
            deldur_window.config(
                bg="white", highlightthickness=2, highlightcolor="navy")
            deldur_window.grab_set()
            deldur_window.focus_set()
            # types options:
            dur = StringVar()
            dur.set("Duration..")
            label = Label(deldur_window, text="Choose The Pack Duration you Want to Delete:", bg="white",
                            fg="navy").place(
                x=20, y=20)
            types = OptionMenu(deldur_window, dur,
                                dur.get(), *backend.sortdur())
            types.config(fg="white", bg="navy", padx=40)
            types.place(x=20, y=40)

            # delete button:
            def dele():
                if dur.get() == "Duration..":
                    messagebox.showwarning(
                        "error", "Please Choose a Duuration!")
                    return
                backend.deletepackdurations(dur.get())
                adddeldur_window.destroy()
                deldur_window.destroy()
                edit_window.destroy()
                edit()
                messagebox.showinfo(
                    "info", " Duration Deleted succesfully")

            delbutton = Button(deldur_window, text="Delete-",
                                bg="red", pady=5, padx=10, fg="white", command=dele)
            delbutton.place(x=220, y=40)

        AddpackButton = Button(adddeldur_window, text="Add pack Duration.", bg="navy", fg="white", pady=20, font=20,
                                command=add_dur)

        AddpackButton.place(x=10, y=20)

        delpackButton = Button(adddeldur_window, text="Delete pack Duration.", bg="red", fg="white", pady=20, font=20,
                                command=del_dur)
        delpackButton.place(x=180, y=20)

    AddDeletedur = Button(edit_window, text="Add / Delete Duration.",
                            bg="navy", fg="white", command=adddel_dur)
    AddDeletedur.place(x=450, y=160)

    # save button:
    def save():
        if packdur.get() == "Duaration.." or packtype.get() == "Type..":
            messagebox.showwarning("error", "Please fill all info .")
            return
        try:
            int(price.get())
        except:
            messagebox.showwarning("error", "Wrong Input .")
            return

        if price.get() <= 0:
            messagebox.showwarning("error", "Wrong Input .")
            return

        n = backend.dfpacks[
            (backend.dfpacks.pack_type == packtype.get()) & (backend.dfpacks.pack_duration == packdur.get()) & (
                backend.dfpacks.price == price.get())]
        if len(n) > 0:
            print(n)
            messagebox.showinfo("info", "This Pack Already Exists")
            return
        m = backend.dfpacks[
            (backend.dfpacks.pack_type == packtype.get()) & (backend.dfpacks.pack_duration == packdur.get()) & (
                backend.dfpacks.price != price.get())]
        if len(m) > 0:
            backend.Update_packs(
                price.get(), packtype.get(), packdur.get())
            packdur.set("Duaration..")
            packtype.set("Type..")
            price_box.delete(0, END)
            messagebox.showinfo("info", "Pack Updated succesfully")
            return
        backend.Adding_packs(packtype.get(), packdur.get(), price.get())
        packdur.set("Duaration..")
        packtype.set("Type..")
        price_box.delete(0, END)
        messagebox.showinfo("info", "Pack added succesfully")

    save_button = Button(edit_window, text="Add / Update Pack.",
                            bg="navy", fg="white", font=60, command=save)
    save_button.place(x=455, y=90)

    # delete button:
    def deletepack():
        if packdur.get() == "Duaration.." or packtype.get() == "Type..":
            messagebox.showwarning("error", "Please fill all info .")
            return
        try:
            int(price.get())
        except:
            messagebox.showwarning("error", "Wrong Input .")
            return
        n = backend.dfpacks[
            (backend.dfpacks.pack_type == packtype.get()) & (backend.dfpacks.pack_duration == packdur.get()) & (
                backend.dfpacks.price == price.get())]
        if len(n) == 0:
            messagebox.showinfo("info", "This Pack Does not Exists")
            return
        backend.delete_packs(price.get(), packtype.get(), packdur.get())
        packdur.set("Duaration..")
        packtype.set("Type..")
        price_box.delete(0, END)
        messagebox.showinfo("info", "Pack Deleted succesfully")

    save_button = Button(edit_window, text="Delete Pack.",
                            bg="red", fg="white", font=60, command=deletepack)
    save_button.place(x=455, y=50)

    # show available packs:
    def Show():
        backend.arrangpacks().to_excel(r"BlueGym_Excel\bluegym_packs_excel.xlsx", sheet_name='Bluegym customers',
                                        index=False)
        os.startfile(r"BlueGym_Excel\bluegym_packs_excel.xlsx")

    showpacks_button = Button(edit_window, text="Show Available subscription packs.", bg="navy", fg="white", font=60,
                                command=Show)
    showpacks_button.place(x=30, y=150)

edit_button = Button(window, text="Add / Edit Packs", padx=5,
                        pady=10, bg="navy", fg="white", font=60, command=edit)
edit_button.place(x=455, y=335)

# monthly income:

edit_button = Button(window, text="Monthly Income", padx=5, pady=10,
                        bg="navy", fg="white", font=60, command=backend.monthly_income)
edit_button.place(x=465, y=280)

# main
mainloop()
backend.closedatabase()
