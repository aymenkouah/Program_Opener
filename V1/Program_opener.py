import os
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog
from ProfileClass import PROFILE
import time

path = r'.'


def open_profile(file):
	global f 
	f = PROFILE(path+file, frame)

def delete_profile(profile_number):
	global frame
	frame.pack_forget()
	try: file_list.pop(int(profile_number))
	except:pass
	frame = LabelFrame(root)
	frame.pack(fill="both")
	show()

def open_profile(profile_number):
	global window, prof
	window = Toplevel()
	try: prof = PROFILE( file_list[int(profile_number)] , window)
	except: pass

def show():
	global file_list, profile_access_list, enter_number, delete_button, frame
	frame.pack(fill="both")
	
	profile_access_list = [Button(frame, text=file) for file in file_list]

	for file in profile_access_list:
		file.pack(fill="both")

	enter_number = Entry(frame)
	execute_button = Button(frame, text="run", command=lambda: execute(enter_number.get() ), bg="yellow").pack(side = "bottom", fill="both")
	save_button = Button(frame, text="save", command=lambda: save()).pack(side = "bottom")
	enter_number.pack()
	delete_button = Button(frame, text="delete", command=lambda: delete_profile(enter_number.get())).pack(side = "bottom")
	enter_button = Button(frame, text="open", command=lambda: open_profile(enter_number.get())).pack(side = "bottom")
	add_button = Button(frame, text="add", command=lambda: add(enter_number.get())).pack(side = "bottom")
	
def save():
	global file_list, profile_access_list
	to_delete = [file for file in os.scandir(path) if (path+file.name not in file_list and file.name[-3:] =="txt") ]
	for item in to_delete:
		try:os.remove(item.path)
		except: pass

	global frame
	frame.pack_forget()
	frame = LabelFrame(root)
	frame.pack()
	show()

def add(name):
	global frame, file_list
	frame.pack_forget()
	frame = LabelFrame(root)
	frame.pack()

	name = path+name+".txt"
	new = open(name, "w+")
	new.write("")
	new.close()
	file_list.append(name)


	show()


def execute(file_number):

		global file_list
		file = open(file_list[int(file_number)], "r")
		apps = file.readlines()
		for app in apps:
			if app!="\n" and app!=" \n":
				if app[0] == " ":
					os.startfile(r"%s" %app[1:-1])	

				else: os.startfile(r"%s" %app[:-1])	
				print(app[:-1])
				time.sleep(2)
			
		file.close()
	



root = Tk()
root.title("App Opener")
width = 800
root.geometry("%sx%s" %(width, width) )

frame = LabelFrame(root, borderwidth=0)
file_list = [path+file.name for file in os.scandir(path) if file.name[-3:] == "txt"]

show()




#self.save_button = Button(self.frame, text="Save", command=lambda: self.save() )
#self.reset_button = Button(self.frame, text="reset", command=lambda: self.reset() )
#self.read_deletion = Entry(self.frame, bg="white")
#self.read_deletion.insert("0", "delete ")

#self.add_button = Button(self.frame, text="add", command=lambda: self.add())
#self.exit_button = Button(self.frame, text="X", command= self.destroy_all, background="red", fg="white")







frame.pack()
enter_number.pack()


mainloop()
