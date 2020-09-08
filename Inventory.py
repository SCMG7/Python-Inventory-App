from tkinter import *
import tkinter as tkr
import tkinter.ttk as tkrttk
from tkinter import ttk
import sqlite3



#Create Window root
root = tkr.Tk()
root.geometry("1420x620")
root.title("11B-Tool-Log")
root.resizable(False, False)
root['background']='#36cbd9'

'''def edit_item():
	editor = tkr.Tk()
	editor.geometry("500x310")
	editor.title("Inventory")
	editor.resizable(False, False)

	#Creating Entrys
	c_name_editor=Entry(editor,width=30)
	c_name_editor.grid(row=0,column=1,pady=5,padx=20)
	p_no_editor=Entry(editor,width=30)
	p_no_editor.grid(row=1,column=1,pady=5)
	t_no_editor=Entry(editor,width=30)
	t_no_editor.grid(row=2,column=1,pady=5)
	d_item_editor=Entry(editor,width=30)
	d_item_editor.grid(row=3,column=1,pady=5)
	c_code_editor=Entry(editor,width=30)
	c_code_editor.grid(row=4,column=1,pady=5)
	l_item_editor=Entry(editor,width=30)
	l_item_editor.grid(row=5,column=1,pady=5)
	b_code_editor=Entry(editor,width=30)
	b_code_editor.grid(row=6,column=1,pady=5)
	n_comm_editor=Entry(editor,width=30)
	n_comm_editor.grid(row=7,column=1,pady=5)
	#Creating lbl
	ca_name_editor = Label(editor,text="Customer Name:")
	ca_name_editor.grid(row=0,column=0)
	pr_no_editor = Label(editor,text="B2B Part Number:")
	pr_no_editor.grid(row=1,column=0)
	to_no_editor = Label(editor,text="Tool Number:")
	to_no_editor.grid(row=2,column=0)
	de_item_editor = Label(editor,text="Description/Componets Produced")
	de_item_editor.grid(row=3,column=0)
	cu_code_editor= Label(editor,text="Customer product code:")
	cu_code_editor.grid(row=4,column=0)
	lo_item_editor = Label(editor,text="Location:")
	lo_item_editor.grid(row=5,column=0)
	ba_code_editor = Label(editor,text="Bar Code:")
	ba_code_editor.grid(row=6,column=0)
	no_comm_editor = Label(editor,text="Notes/Comments:")
	no_comm_editor.grid(row=7,column=0)
	#Create Submit Button
	btn_submit_changes = Button(editor,text="Submit Changes")
	btn_submit_changes.grid(row=8,column=0,columnspan=2,padx=20)
	'''

def Search_by_prdc_No():
	conn = sqlite3.connect('tool_log.db')
	#Clear TreeView
	for x in tree.get_children():
		tree.delete(x)
	customer_prod_code = e_Search_by_prdc_code.get()
	#Connect to db
	c=conn.cursor()

	select = c.execute("select*from inventory where customer_prod_code = (?)", (customer_prod_code,))
	conn.commit()

	e_Search_by_prdc_code.delete(0, END)

	for row in select:
		tree.insert('',END,values=row)
	conn.close()

def Search_by_tool():
	conn = sqlite3.connect('tool_log.db')
	#Clear TreeView
	for x in tree.get_children():
		tree.delete(x)
	tool_no = e_Search_by_tool.get()
	#Connect to db
	c=conn.cursor()

	select = c.execute("select*from inventory where tool_no = (?)", (tool_no,))
	conn.commit()

	e_Search_by_tool.delete(0, END)

	for row in select:
		tree.insert('',END,values=row)
	conn.close()

def Search_by_customer():
	conn = sqlite3.connect('tool_log.db')
	#Clear TreeView
	for x in tree.get_children():
		tree.delete(x)
	customer_name = e_Search_by_customer.get()
	#Connect to db
	c=conn.cursor()

	select = c.execute("select*from inventory where customer_name = (?)", (customer_name,))
	conn.commit()

	e_Search_by_customer.delete(0, END)

	for row in select:
		tree.insert('',END,values=row)
	conn.close()

def show_by_name():
	conn = sqlite3.connect('tool_log.db')
	#Clear TreeView
	for x in tree.get_children():
		tree.delete(x)
	#Connect to db
	c=conn.cursor()

	select = c.execute("select*from inventory order by customer_name asc")
	conn.commit()

	for row in select:
		tree.insert('',END,values=row)
	conn.close()

def Add_New():
	#Create Second Window
	add_win=Toplevel()
	add_win.geometry("500x310")
	add_win.title("Add a new item")
	add_win['background']='#36cbd9'
	#Create a database or connect to one
	conn=sqlite3.connect('tool_log.db')
	#Create cursor
	c=conn.cursor()
	#Create Table ONLY ONCE after that comment it.
	#c.execute("""CREATE TABLE inventory(
	#	id_no integer primary key AUTOINCREMENT,
	#	customer_name text,
	#	part_no integer,
	#	tool_no text,
	#	descr_item_produced text,
	#	customer_prod_code text,
	#	location_item text,
	#	bar_code text,
	#	notes_comments text
	#	)""")
	#Commit Changes
	conn.commit()
	#Create Submit Function for New Item
	def submit():
		#Make Connection
		conn=sqlite3.connect('tool_log.db')
		#Create cursor
		c=conn.cursor()	
		#Insert Into Table
		c.execute("INSERT INTO inventory VALUES(NULL,:c_name,:p_no,:t_no,:d_item,:c_code,:l_item,:b_code,:n_comm)",
				{	

					'c_name' : c_name.get(),
					'p_no' : p_no.get(),
					't_no':t_no.get(),
					'd_item':d_item.get(),
					'c_code':c_code.get(),
					'l_item':l_item.get(),
					'b_code':b_code.get(),
					'n_comm':n_comm.get(),
				})
		#Commit Changes
		conn.commit()
		#Close Connection with db
		conn.close()
		#Make Connection
		conn=sqlite3.connect('tool_log.db')
		#Create cursor
		c=conn.cursor()	
		select = c.execute("SELECT*FROM inventory ORDER BY id_no desc")
		select=list(select)
		tree.insert('',END, value=select[0])
		conn.close()


		#Clear the text Boxes on SUBMIT
		c_name.delete(0, END)
		p_no.delete(0, END)
		t_no.delete(0, END)
		d_item.delete(0, END)
		c_code.delete(0, END)
		l_item.delete(0, END)
		b_code.delete(0, END)
		n_comm.delete(0, END)
	#Creating Entrys
	c_name=Entry(add_win,width=30)
	c_name.grid(row=0,column=1,pady=5,padx=20)
	p_no=Entry(add_win,width=30)
	p_no.grid(row=1,column=1,pady=5)
	t_no=Entry(add_win,width=30)
	t_no.grid(row=2,column=1,pady=5)
	d_item=Entry(add_win,width=30)
	d_item.grid(row=3,column=1,pady=5)
	c_code=Entry(add_win,width=30)
	c_code.grid(row=4,column=1,pady=5)
	l_item=Entry(add_win,width=30)
	l_item.grid(row=5,column=1,pady=5)
	b_code=Entry(add_win,width=30)
	b_code.grid(row=6,column=1,pady=5)
	n_comm=Entry(add_win,width=30)
	n_comm.grid(row=7,column=1,pady=5)
	#Creating lbl
	ca_name = Label(add_win,text="Customer Name:",bg="#36cbd9")
	ca_name.grid(row=0,column=0)
	pr_no = Label(add_win,text="B2B Part Number:",bg="#36cbd9")
	pr_no.grid(row=1,column=0)
	to_no = Label(add_win,text="Tool Number:",bg="#36cbd9")
	to_no.grid(row=2,column=0)
	de_item = Label(add_win,text="Description/Componets Produced",bg="#36cbd9")
	de_item.grid(row=3,column=0)
	cu_code = Label(add_win,text="Customer product code:",bg="#36cbd9")
	cu_code.grid(row=4,column=0)
	lo_item = Label(add_win,text="Location:",bg="#36cbd9")
	lo_item.grid(row=5,column=0)
	ba_code = Label(add_win,text="Bar Code:",bg="#36cbd9")
	ba_code.grid(row=6,column=0)
	no_comm = Label(add_win,text="Notes/Comments:",bg="#36cbd9")
	no_comm.grid(row=7,column=0)
	#Create Submit Button
	btn_submit = Button(add_win,text="Add Record To Database",command=submit)
	btn_submit.grid(row=8,column=0,columnspan=2,padx=20)
	#Commit Changes
	conn.commit()
	#Close Connection with db
	conn.close()

def delete_item():

	def exit_after_no():
		deleter.destroy()

	def yes_delete():
		conn = sqlite3.connect('tool_log.db')
		idSelect=(tree.item(tree.selection())['values'][0])
		c = conn.cursor()
		delete = c.execute("delete from inventory where id_no = {}".format(idSelect))
		conn.commit()
		tree.delete(tree.selection())
		conn.close()
		deleter.destroy()


	deleter=Toplevel()
	deleter.geometry("230x90")
	deleter.title("Deleting Record")
	deleter['background']='#36cbd9'

	lbl_confurm=Label(deleter,text="Are you sure ?",bg="#36cbd9").place(x=70,y=10)
	btn_YES=Button(deleter,text="Yes",width=4,command=yes_delete).place(x=50,y=40)
	btn_NO=Button(deleter,text="No",width=4,command=exit_after_no).place(x=130,y=40)
	

#Creating labels in ROOT
lbl_Search = Label(root,text="Search for Customer:",bg="#36cbd9").place(x=3, y=7)
lbl_Search_by_tool =Label(root,text="Search by Tool No:",bg="#36cbd9").place(x=480,y=7)
lbl_Search_by_prdc_code =Label(root,text="Search by Product No:",bg="#36cbd9").place(x=950,y=7)
#Creating Butons 
btn_Search_by_name = Button(root,text="Search",command=Search_by_customer).place(x=375,y=2)
btn_Search_by_tool = Button(root,text="Search",command=Search_by_tool).place(x=837,y=2)
btn_Search_by_prdc_code = Button(root,text="Search",command=Search_by_prdc_No).place(x=1340,y=2)
btn_Add = Button(root,text="Add New Item",command=Add_New).place(x=1160,y=582)
btn_Delete = Button(root,text="Delete Selected",command=delete_item).place(x=1284,y=582)
#btn_Update = Button(root,text="Edit Selected",command=edit_item).place(x=1290,y=582)
btn_Sort_by_name = Button(root,text="Show All by Customer",command=show_by_name).place(x=5,y=582)
#Creating Entrys for inputs
e_Search_by_customer=Entry(root,borderwidth=3,width=27)
e_Search_by_customer.place(x=144, y=3 )
e_Search_by_tool=Entry(root,borderwidth=3,width=27)
e_Search_by_tool.place(x=606, y=3 )
e_Search_by_prdc_code=Entry(root,borderwidth=3,width=27)
e_Search_by_prdc_code.place(x=1110, y=3 )
#Creating TreeView
tree = ttk.Treeview(root,columns=("1","2","3","4","5","6","7","8","9"),height='26', show='headings',selectmode="extended")
tree.place(x=3,y=35,width=1410)
tree.heading("1", text="ID")
tree.column("1", width=10) 
tree.heading("2", text="Customer")
tree.column("2", minwidth=70, width=100) 
tree.heading("3", text="B2B Part No")
tree.column("3", minwidth=100, width=120)
tree.heading("4", text="Tool No")
tree.column("4", minwidth=80, width=90)
tree.heading("5", text="Description")
tree.column("5", minwidth=100, width=200)
tree.heading("6", text="Customer Product No")
tree.column("6", minwidth=180, width=150)
tree.heading("7", text="Location'")
tree.column("7", minwidth=20, width=40)
tree.heading("8", text="Bar Code'")
tree.column("8", minwidth=70, width=100)
tree.heading("9", text="Comments'")
tree.column("9", minwidth=100, width=200)
##Display data in Treeview
conn=sqlite3.connect('tool_log.db')
c=conn.cursor()
select = c.execute("select*from inventory")
for row in select:
	tree.insert('',END,value=row)
conn.commit()
conn.close()



#Activate
tkr.mainloop()
