import sqlite3

def save_project(name,project,p_title):
    connection=sqlite3.connect('db.sqlite3')
    c=connection.cursor()
    c.execute("INSERT INTO user_project (NAME,PROJECT,P_TITLE) VALUES (?,?,?);",(name,project,p_title))
    connection.commit()
    connection.close()

def retriveproject(name):
    connection = sqlite3.connect('db.sqlite3')
    c = connection.cursor()
    d=c.execute("SELECT PROJECT,P_TITLE FROM user_project where NAME=?",(name,))
    data={}
    for names in d.fetchall():
        data[names[0]]=names[1]
    connection.close()
    return data