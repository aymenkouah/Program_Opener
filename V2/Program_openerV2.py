import os
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog
from ProfileClassV2 import PROFILE
import time

path = r'F:\hidehere\\'


def open_profile(file):
	global f 
	f = PROFILE(path+file, frame)

def delete_profile(profile_number_list):
	global frame, file_list
	frame.pack_forget()
	delete = []
	for var in range(len(profile_number_list) ):
		if profile_number_list[var].get() != 0:
			delete.append(var)
			#file_list.pop(int(var))

	file_list = [ file_list[var] for var in range(len(file_list)) if var not in delete ]
	frame = LabelFrame(root)
	frame.pack(fill="both")
	show()

def open_profile(profile_number_list):
	global window, prof
	for var in range(len(profile_number_list)):
		if profile_number_list[var].get() != 0:
			window = Toplevel()
			try: prof = PROFILE( file_list[var] , window)
			except: pass

def show():
	global file_list, profile_access_list, profile_access_var, enter_number, delete_button, frame
	frame.pack(fill="both")
	
	profile_access_var = [ IntVar() for i in range(len(file_list))]
	profile_access_list = [Checkbutton(frame, text=file_list[file], variable=profile_access_var[file]) for file in range(len(file_list))]

	for file in profile_access_list:
		file.pack(fill="both")

	
	execute_button = Button(frame, text="run", command=lambda: execute(profile_access_var), bg="yellow").pack(side = "bottom", fill="both")
	save_button = Button(frame, text="save", command=lambda: save()).pack(side = "bottom")
	
	
	enter_button = Button(frame, text="open", command=lambda: open_profile(profile_access_var)).pack(side = "bottom")
	add_button = Button(frame, text="add", command=lambda: add(enter_number.get())).pack(side = "bottom")
	delete_button = Button(frame, text="delete", command=lambda: delete_profile(profile_access_var)).pack(side = "bottom")
	enter_number = Entry(frame)
	enter_number.pack()

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


def execute(var_list):
	global file_list
	for var in range(len(var_list)):
		if var_list[var].get() != 0:		
			file = open(file_list[int(var)], "r")
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
#enter_number.pack()


mainloop()
