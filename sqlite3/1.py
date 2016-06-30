import sqlite3

expFileName = ['\Experium.exe', '\exprus.dll', '\expenu.dll', '\MailEngine.dll', '\SMSEngine.dll', '\GCalDav.dll', '\Telephony.dll']

conn = sqlite3.connect('exp.sqlite')
cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS exp.sqlite;')
cur.execute('''CREATE TABLE exp (expFileName text, expPath text)''')
# cur.execute("INSERT INTO exp(ExpFileName) VALUES ('Experium.exe'),('exprus.dll'),('expenu.dll'),('MailEngine.dll'),('SmsEngine.dll');")
cur.execute('INSERT INTO exp(ExpFileName) VALUES(?)', (str[expFileName[0]],))
conn.commit()
