from PyQt5 import QtWidgets, QtSql
import os, sys
app = QtWidgets.QApplication(sys.argv)
con1 = QtSql.QSqlDatabase.addDatabase('QODBC', connectionName='P3')
con1.setDatabaseName('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEMOSTEND\PARSEC3;DATABASE=PARSEC3;UID=sa;PWD=parsec3')
con1.open()
con2 = QtSql.QSqlDatabase.addDatabase('QODBC', connectionName='P2')
con2.setDatabaseName('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DEMOSTEND\PARSECDB;DATABASE=PARSECDB;UID=sa;PWD=parsec')
con2.open()
if con1.isOpen():
    print('База Parsec3 открыта')
    # print(con.tables(QtSql.QSql.Tables))
    # print('Состав таблицы DEVICE')
    # tabs = con.record('DEVICE')
    # for i in range(tabs.count()):
        # print(tabs.fieldName(i))
    # print('Состав таблицы DEVICE_DOC')
    # tabs2 = con.record('DEVICE_DOC')
    # for j in range(tabs2.count()):
        # print(tabs2.fieldName(j))
if con2.isOpen():
    print('База Parsec2 открыта')
    # print(con2.tables(QtSql.QSql.Tables))
    # print('Состав таблицы Doors')
    # tabs3 = con2.record('Doors')
    # for i in range(tabs3.count()):
        # print(tabs3.fieldName(i))
    # print('Состав таблицы wtSelDoors')
    # tabs4 = con2.record('wtSelDoors')
    # for j in range(tabs4.count()):
        # print(tabs4.fieldName(j))
elif con1.isOpenError():
    print('Конкретная ошибка:', con1.lastError().text())
elif con2.isOpenError():
    print('Конкретная ошибка:', con2.lastError().text())
else:
    print('Oops!')
sum = 0
query1 = QtSql.QSqlQuery(con1)
query1.exec("select * from ACCGROUP")
lst1 = []
if query1.isActive():
    query1.first()
    while query1.isValid():
        lst1.append(query1.value('ACCGROUP_ID'))
        query1.next()
query2 = QtSql.QSqlQuery(con1)
query2.exec("select * from COMPGROUP")
lst2 = []
if query2.isActive():
    query2.first()
    while query2.isValid():
        lst2.append(query2.value('COMPGROUP_ID'))
        query2.next()
for p in lst1: print(p)
print('/n New list /n')
for t in lst2: print(t)
p = 0
while p < len(lst1):
    if lst1[p] in lst2:
        sum = sum + 1
    p += 1
print(sum)
con1.close()
con2.close()