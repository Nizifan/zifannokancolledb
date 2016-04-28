from Tkinter import *
from Tkconstants import *

'''
import informixdb
import os

Database = 'd_1442910194518478'
#Server='172.16.13.186'
Server='ifxserver1'
Username = 'gnyqdtrl'
Password = 'MMXznJT6Ps'

'''



class Search_Windows:
        def __init__(self):
                window = Tk()
                window.title("Search")
		
		Label(window,text="Input name of the fleetgirl you want").pack()
		self.fleetgirlid = StringVar()
		Entry(window,textvariable = self.fleetgirlid).pack()

		windows=Frame(window)
		windows.pack()

		Label(windows,text="Name").pack(side=LEFT)
		Label(windows,text="Trans level").pack(side=LEFT)
                Label(windows,text="Firepower").pack(side=LEFT)
                Label(windows,text="Torpedo").pack(side=LEFT)
                Label(windows,text="Antiair").pack(side=LEFT)
                Label(windows,text="Armor").pack(side=LEFT)
 

		windows2=Frame(window)
		windows2.pack()


		search_name = StringVar()
		Label(windows2,textvariable=search_name).pack(side=LEFT)
                search_translevel = StringVar()
                Label(windows2,textvariable=search_translevel).pack(side=LEFT)
                search_firepower = StringVar()
                Label(windows2,textvariable=search_firepower).pack(side=LEFT)
                search_torpedo = StringVar()
                Label(windows2,textvariable=search_torpedo).pack(side=LEFT)
                search_antiair = StringVar()
                Label(windows2,textvariable=search_antiair).pack(side=LEFT)
                search_armor = StringVar()
                Label(windows2,textvariable=search_armor).pack(side=LEFT)
		

		button_search = Button(window,text="Search",command=self.search)
		button_search.pack(side = BOTTOM )
	    
		button_exit = Button(window,text="Exit",command=window.destroy)
		button_exit.pack(side=BOTTOM)	
                
		window.mainloop()

	def search(self):
		print("unimplemented")		
		'''
		cur.execute("select * from kancolle_db where name like :1",self.fleetgirlid.get())
		a = cur.fetchone()
		search_name.set(a[0])
		search_translevel.set(a[1])
		search_firepower.set(a[2])
		search_torpedo.set(a[3])
		search_antiair.set(a[4])
		search_armor.set(a[5])
		'''
def opensearchwindow():
        Search_Windows()
		
class Add_Windows:
        def __init__(self):
                window = Tk()
                window.title("Add")
		

		windows = Frame(window)
		windows.pack(side = TOP)

		Label(window,text="Name").pack()
		self.name = StringVar()
                Entry(window,textvariable = self.name,justify = RIGHT).pack()	
 
		Label(window,text="Type").pack()
                self.type = StringVar()
                Entry(window,textvariable = self.type,justify = RIGHT).pack()

		Label(window,text="level").pack()
                self.translevel = StringVar()
                Entry(window,textvariable = self.translevel,justify = RIGHT).pack()

		Label(window,text="Firepower").pack()
                self.firepower = StringVar()
                Entry(window,textvariable = self.firepower,justify = RIGHT).pack()

		Label(window,text="Torpedo").pack()
                self.torpedo = StringVar()
                Entry(window,textvariable = self.torpedo,justify = RIGHT).pack()

		Label(window,text="Antiair").pack()
                self.antiair = StringVar()
                Entry(window,textvariable = self.antiair,justify = RIGHT).pack()

		Label(window,text="Armor").pack()
                self.armor = StringVar()
                Entry(window,textvariable = self.armor,justify = RIGHT).pack()


                button_search = Button(window,text="Add",command=self.add)
                button_search.pack(side = BOTTOM )

                button_exit = Button(window,text="Exit",command=window.destroy)
                button_exit.pack(side=BOTTOM)

                window.mainloop()
	
	def add(self):
		print("unimplemented")


def openaddwindow():
        Add_Windows()

class Delete_Windows:
        def __init__(self):
                window = Tk()
                window.title("Delete")

		Label(window,text="Input name of the fleetgirl you want to delete").pack()
		self.fleetgirlid = StringVar()
                Entry(window,textvariable = self.fleetgirlid).pack()

                button_search = Button(window,text="Delete",command=self.delete)
                button_search.pack(side = BOTTOM )

                button_exit = Button(window,text="Exit",command=window.destroy)
                button_exit.pack(side=BOTTOM)

                window.mainloop()

	def delete(self):
		print("unimplenmented")

def opendeletewindow():
        Delete_Windows()

FleetgirlDatabase = Tk()
frame = Frame(FleetgirlDatabase, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

backg_image=PhotoImage(file = 'image/xiaobei.gif')
Label(frame,image=backg_image).pack(side=LEFT)

label = Label(frame, text="Fleet girls database")
label.pack(fill=X, expand=1)
button_exit = Button(frame,text="Exit",command=FleetgirlDatabase.destroy)
button_exit.pack(side=BOTTOM)
button_search = Button(frame,text="Search",command=opensearchwindow)
button_search.pack(side=LEFT)
button_add = Button(frame,text="Add",command=openaddwindow)
button_add.pack(side=LEFT)
button_delete = Button(frame,text="Delete",command=opendeletewindow)
button_delete.pack(side=LEFT)

'''
cur = conn = None 
#connect
conn = informixdb.connect(Database+'@'+Server,Username,Password)
if not conn:
	raise Exception("Failed to connect via SQL to " + dbservername)
else:
	print("connect !!!!")
#get cursor
cur = conn.cursor()
#query count of testtable(if not exists,created)
cur.execute("select count(*) from testtable")
a = cur.fetchall()

'''

FleetgirlDatabase.mainloop()
