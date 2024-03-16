import sqlite3
import os
import pandas as pd
import datetime

# database:
database = sqlite3.connect("Gym DataBase.db")
c = database.cursor()

# database_excel:
try:
    os.mkdir("BlueGym_Excel")
except:
    pass


def creating_customer_withHistory_table():
    c.execute(""" CREATE TABLE  IF NOT EXISTS CUSTOMERS_HISTORY(
 ID int ,
 Name text,
 Phone_number text,
 Gender text,
 pack_duaration text,
 pack_type text,
 Balance int,
 Start_date DATE,
 End_date DATE,
 paid int,
 paid_date DATE,
 Discount_amount int
 )""")


creating_customer_withHistory_table()
df_history = pd.read_sql_query("SELECT * FROM CUSTOMERS_HISTORY;", database)


def update_History_dataframe():
    global df_history
    df_history = pd.read_sql_query(
        "SELECT * FROM CUSTOMERS_HISTORY;", database)


def adding_recordtoHistory(id, name, phone, gender, packdur, packtyp, balance, start, end, paid, paiddate, dis):
    c.execute("INSERT INTO CUSTOMERS_HISTORY"
              "(  ID, Name,Phone_number,Gender,pack_duaration,pack_type,Balance,Start_date,End_date,paid,paid_date,Discount_amount) "
              f"VALUES(?,?,?,?,?,?,?,?,?,?,?,?);",
              (id, name, phone, gender, packdur, packtyp, balance, start, end, paid, paiddate, dis))
    database.commit()
    update_History_dataframe()


def DeleteAllRecordFromHistory():
    c.execute("DELETE FROM CUSTOMERS_HISTORY;")
    database.commit()
    update_History_dataframe()


def addinghistory(a):
    if a.isnumeric():
        temp = pd.read_sql_query(
            f"SELECT * FROM CUSTOMERS WHERE ID=\'{a}\'", database)
    else:
        temp = pd.read_sql_query(
            f"SELECT * FROM CUSTOMERS WHERE Name=\'{a}\'", database)
    return (temp.head(1).values.tolist()[0])


def creating_customertable():
    c.execute(""" CREATE TABLE  IF NOT EXISTS CUSTOMERS(
 ID INTEGER PRIMARY KEY,
 Name text,
 Phone_number text,
 Gender text,
 pack_duaration text,
 pack_type text,
 Balance int,
 Start_date DATE,
 End_date DATE,
 paid int,
 paid_date DATE,
 Discount_amount int
 )""")


# customer table:
creating_customertable()
df = pd.read_sql_query("SELECT * FROM CUSTOMERS;", database)


def update_dataframe():
    global df
    df = pd.read_sql_query("SELECT * FROM CUSTOMERS;", database)


def get_id():
    global df
    try:
        a = df.tail(1)["ID"].values[0]
        return int(a)
    except:
        pass


get_id()


def adding_record(name, phone, gender, packdur, packtyp, balance, start, end, paid, paiddate, dis):

    c.execute("INSERT INTO CUSTOMERS"
              "(Name,Phone_number,Gender,pack_duaration,pack_type,Balance,Start_date,End_date,paid,paid_date,Discount_amount) "
              f"VALUES(?,?,?,?,?,?,?,?,?,?,?);",
              (name, phone, gender, packdur, packtyp, balance, start, end, paid, paiddate, dis))
    database.commit()
    update_dataframe()


def DeleteAllRecord():
    c.execute("DELETE FROM CUSTOMERS;")
    database.commit()
    update_dataframe()


def DeleteRecord(record):
    c.execute(f"DELETE FROM CUSTOMERS WHERE ID=\'{record}\' ;")
    database.commit()
    update_dataframe()


def updaterecord(record, packdur, packtyp, balance, paid, start, end, paiddate):
    c.execute(
        f""" UPDATE CUSTOMERS
                 SET Pack_duaration= \'{packdur}\', Balance={balance}+Balance,paid={paid},start_date=\"{start}\",end_date=\"{end}\",Pack_type=\'{packtyp}\',paid_date=\'{paiddate}\'  WHERE Name=\'{record}\' OR ID=\'{record}\'""")
    database.commit()
    update_dataframe()


def updatedept(record, paid):
    c.execute(
        f"""UPDATE CUSTOMERS  SET Balance =\"{paid}\"+Balance , paid=\"{paid}\"+paid WHERE Name=\'{record}\' OR ID=\'{record}\'  """)
    database.commit()


# packs database:
pack_types = ["BodyBuilding", "Boxing", "Fitness", "Weight Loss"]
pack_durations = ["1 Month", "2 Months", "3 Months",
                  "6 Months", "9 Months", "12 Months", "24 Months"]


def creating_packstable():
    c.execute(""" CREATE TABLE  IF NOT EXISTS Packs(
    pack_type text,
    pack_duration text,
    price int)""")


creating_packstable()
dfpacks = pd.read_sql_query("SELECT * FROM Packs;", database)


def update_packsdataframe():
    global dfpacks
    dfpacks = pd.read_sql_query("SELECT * FROM Packs;", database)


def Adding_packs(ptype, duration, cost):
    c.execute("INSERT INTO Packs"
              "(pack_type,pack_duration,price) "
              f"VALUES(?,?,?);",
              (ptype, duration, cost))

    database.commit()
    update_packsdataframe()


# packtypes table:

def packstypetabel():
    c.execute(""" CREATE TABLE  IF NOT EXISTS Packtypes(
    ID INTEGER PRIMARY KEY,
    packtype text
    )""")


packstypetabel()

dfpacktypes = pd.read_sql_query("SELECT * FROM Packtypes;", database)


def update_pack_types_dataframe():
    global dfpacktypes
    dfpacktypes = pd.read_sql_query("SELECT * FROM Packtypes;", database)


def addpacktype(x):
    c.execute("INSERT INTO Packtypes"
              "(packtype) "
              f"VALUES(\'{x}\');")
    database.commit()
    update_pack_types_dataframe()


def deletepacktype(x):
    c.execute(f"DELETE FROM Packtypes WHERE packtype=\'{x}\';")
    database.commit()
    update_pack_types_dataframe()


# packdur table:
def packdurtable():
    c.execute(""" CREATE TABLE  IF NOT EXISTS Packdurations(
    ID INTEGER PRIMARY KEY,
    packduration text
    )""")


packdurtable()
dfpackdurations = pd.read_sql_query("SELECT * FROM Packdurations;", database)


def sortdur():
    temp = dfpackdurations["packduration"].tolist()
    a = list()
    for i in range(len(temp)):
        a.append(int(temp[i][0:2]))

    # a=[(int(temp[i][0:2])  for i in range(len(temp))]
    a = sorted(a)
    global b
    b = list()
    for i in a:
        i = f"{i} Months"
        b.append(i)
    return b


def update_pack_durations_dataframe():
    global dfpackdurations
    dfpackdurations = pd.read_sql_query(
        "SELECT * FROM Packdurations;", database)


def addpackduration(x):
    c.execute("INSERT INTO Packdurations"
              "(packduration) "
              f"VALUES(\'{x}\');")
    database.commit()
    update_pack_durations_dataframe()


def deletepackdurations(x):
    c.execute(f"DELETE FROM Packdurations Where packduration=\"{x}\";")
    database.commit()
    update_pack_durations_dataframe()


# ===========================================================================
def Update_packs(price, ptype, duration):
    c.execute(
        f"""UPDATE Packs  SET price =\"{price}\" WHERE pack_type=\'{ptype}\' AND pack_duration=\'{duration}\'""")
    database.commit()
    update_packsdataframe()


def delete_packs(price, ptype, duration):
    c.execute(
        f"DELETE FROM Packs WHERE pack_type=\'{ptype}\' AND pack_duration=\'{duration}\' AND price=\'{price}\' ;")
    database.commit()
    update_packsdataframe()


def arrangpacks():
    global dfpacks
    df_formal = dfpacks[0:0]
    for i in dfpacks.pack_type.unique():
        temp = dfpacks[dfpacks.pack_type == i]
        temp.sort_values("price")
        df_formal = pd.concat([df_formal, temp], ignore_index=True)
    return df_formal


arrangpacks()


def monthly_income():
    update_dataframe()
    dfmonthly = df.copy()
    a = dfmonthly.paid_date.tolist()
    b = list()
    for i in a:
        b.append(i[0:7])
    c = dfmonthly
    c = c.drop("paid_date", axis=1)
    c["paid_date"] = b
    b = list(set(b))
    expectedmonthly = list()
    actualmonthly = list()
    for i in b:
        tmp = sum(c[c.paid_date == i]["paid"])+abs(
            sum(c[c.paid_date == i]["Balance"]))+sum(c[c.paid_date == i]["Discount_amount"])
        actualmonthly.append(sum(c[c.paid_date == i]["paid"]))
        expectedmonthly.append(tmp)
    dic = {"month": b,
           "expected_this_month": expectedmonthly,
           "actual_paid": actualmonthly}
    dfsss = pd.DataFrame.from_dict(dic)
    dfsss.to_excel(r"BlueGym_Excel\bluegym_monthlyIncome_excel.xlsx",
                   sheet_name='Bluegym INCOME', index=False)
    os.startfile(r"BlueGym_Excel\bluegym_monthlyIncome_excel.xlsx")


def filter_search(datetype, startDate, Enddate, Balance, subscribtion_type, gender):
    print(subscribtion_type)
    dffiltered = pd.read_sql_query(
        f"SELECT * FROM CUSTOMERS where      Balance{Balance[0] } \' {Balance[1]}\'    {subscribtion_type}   {gender}        AND ({datetype}>= \'{startDate}\' AND {datetype}<\'{Enddate}\')  ;", database)
    dffiltered.to_excel(r"BlueGym_Excel\search-filter.xlsx",
                        sheet_name='Search', index=False)
    os.startfile(r"BlueGym_Excel\search-filter.xlsx")


def closedatabase():
    database.close()
