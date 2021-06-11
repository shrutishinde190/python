from tkinter import*
import sqlite3

root=Tk()
root.title("Registeration Form")
root.geometry("500x500")

#connect or create a database
conn = sqlite3.connect('customer.db')
#create cursor
c = conn.cursor()
#Create the table
c.execute("CREATE TABLE IF NOT EXISTS users(UserID integer(10), Username varchar(20),Password varchar(20))" )

#Create function to delete a record
def delete():
    #connect or create a database
    conn = sqlite3.connect('customer.db')
    #create cursor
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from users WHERE UserID = " + del_box.get())

    #commit the changes in database
    conn.commit()
    conn.close()    


#Create button submit
def submit():
    #connect or create a database
    conn = sqlite3.connect('customer.db')
    #create cursor
    c = conn.cursor()
    #insert tables
    c.execute("INSERT INTO users VALUES (:UserID, :Username, :Password)",
            {
                'UserID' : Userid_box.get(),
                'Username' :Username_box.get(),
                'Password' :Password_box.get()
            })
    #commit the changes in database
    conn.commit()
    conn.close()

    #clear the textboxes
    Userid_box.delete(0, END)
    Username_box.delete(0, END)
    Password_box.delete(0, END)

#Create query function
def addtoDB():
    #connect or create a database
    conn = sqlite3.connect('customer.db')
    #create cursor
    c = conn.cursor()
    #Query the db
    c.execute("SELECT * FROM users")
    record = c.fetchall()
    #print(record)
    #Loop through results
    print_record  = ''
    for x in record:
        print_record += str(x[0]) + " " + str(x[1])+ "  " + "\t\t" + str(x[2])+"\n"
        
    #Query label
    query_label=Label(root,text = print_record)
    query_label.grid(row=12,column=1)
        
    #commit the changes in database
    conn.commit()
    conn.close()

#Create labels
Userid_label= Label(root,text="User ID").grid(row=0,column=0,padx=5,pady=10)
Username_label=Label(root,text="Username").grid(row=1,column=0,padx=5,pady=10)
Passwd_label= Label(root,text="Password").grid(row=2,column=0,padx=5,pady=20)
delete_label=Label(root,text="Delete ID").grid(row=8 ,column=0, padx=10, pady=10)
#Entry boxes
Userid_box=Entry(root,textvariable=Userid_label)
Userid_box.grid(row=0,column=1,padx=5,pady=10)
Username_box=Entry(root,textvariable=Username_label)
Username_box.grid(row=1,column=1,padx=5,pady=10)
Password_box=Entry(root,show='*',textvariable=Passwd_label)
Password_box.grid(row=2,column=1,padx=5,pady=20)
del_box=Entry(root,width=30)
del_box.grid(row=8,column=1,padx=10,pady=10)

#button
submit_button=Button(root,text="Submit",cursor="hand2",command=submit).grid(row=6,column=1,padx=5,pady=5,ipadx=100,ipady=5)
#Create a button add values to db
query_button=Button(root, text="Show database",command=addtoDB).grid(row=7,column=1,padx=5,pady=5,ipadx=100,ipady=5)
#Create a DElete button 
delete_button=Button(root, text="Delete Record",command=delete).grid(row=11,column=1,padx=5,pady=5,ipadx=100,ipady=5)
#Create a update button 
#update_button=Button(root, text="Add Record",command=update).grid(row=11,column=1,padx=5,pady=5,ipadx=100,ipady=5)

#c.execute("DROP TABLE users")
#commit the changes in database
conn.commit()
conn.close()


root.mainloop()






















