import os
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog
path =r"F:\hidehere"


class PROFILE():
	def __init__(self, file_path, mainframe):
		self.path = file_path
		self.name = os.path.basename(r"%s" %self.path)
		self.contents = self.contents_extract()

		self.frame = mainframe #The root
		

		self.apps = LabelFrame(self.frame, text=self.name, fg="green", width=375, height=115, borderwidth=5) 
		#self.labels = [Label(self.apps, text=var, bg="white") for var in self.contents ] #not in use in this version


		self.checkboxes, self.vars_for_checkboxes = self.generate_checkboxes()


		self.save_button = Button(self.frame, text="Save", command=lambda: self.save() )
		self.reset_button = Button(self.frame, text="reset", command=lambda: self.reset() )

		self.delete_button = Button(self.frame, text="delete", command=lambda: self.delete())
		self.add_button = Button(self.frame, text="add", command=lambda: self.add())
		self.exit_button = Button(self.frame, text="X", command= self.destroy_all, background="red", fg="white")
		#self.read_deletion = Entry(self.frame, bg="white")
		#self.read_deletion.insert("0", "delete ")

		self.show()


	def contents_extract(self):
		file = open(self.path, 'r')
		content = file.readlines()
		file.close()
		return content

	def generate_checkboxes(self):
		to_return_checks = []
		to_return_vars = []
		for i in range( len(self.contents)):
			to_return_vars.append(IntVar())
			to_return_checks.append(Checkbutton(self.apps, text=f"%s" %self.contents[i], variable=to_return_vars[i]))
		return to_return_checks, to_return_vars


	def save(self):
		new_file = open(path+"temporary_file.txt", "w+")
		for i in range(len(self.contents)):
			if self.contents[i] != "" : new_file.write(self.contents[i])
		new_file.close()
		try:
			os.remove(self.path)
		except:pass
		os.rename(path + "temporary_file.txt", self.path)
		self.show()


	def reset(self):
		try: self.hide()
		except: pass

		self = PROFILE(self.path, self.frame)

		self.show()


	def delete(self):
		
		self.hide()

		lis = self.to_del()
		to_delete = [""] * len(lis)
		for item in range(len(lis)):
			to_delete[item] = self.contents[ int(lis[item]) ]

		self.contents = [item for item in self.contents if item not in to_delete ]
		print(self.vars_for_checkboxes)
		self.vars_for_checkboxes = []
		self.checkboxes = []

		self.vars_for_checkboxes = [ IntVar() for var in range(len(self.contents)) ]
		self.checkboxes = [Checkbutton(self.apps, text="%s" %self.contents[i]) for i in range(len(self.contents)) ]
		
		

		self.show()

	def add(self):
		try: self.hide()
		except: pass

		filename = filedialog.askopenfilename(initialdir='.', title="choose app", filetypes=(("apps", "*.exe"), ("all", "*.*") ) ) +"\n"
		self.contents.append(filename)
		self.vars_for_checkboxes.append(len(self.contents) -1 )
		self.checkboxes.append( Checkbutton(self.apps, text=filename, variable=self.vars_for_checkboxes[len(self.contents) - 1]))

		self.show()


	def show(self):
		try: self.hide()
		except: pass
		self.exit_button.pack(anchor="e")
		self.apps.pack(fill="both")
		for check in self.checkboxes:
			check.pack()


		self.save_button.pack(side = "bottom")
		self.reset_button.pack(side = "bottom")
		self.delete_button.pack(side = "bottom")
		self.add_button.pack(side = "bottom")
		#self.read_deletion.pack(side = "bottom")

	def to_del(self):
		ret = []
		for i in range(len(self.contents)):
			try:
				if self.vars_for_checkboxes[i].get() != 0:
					ret.append(i)
			except:
				ret.append(i)
		return ret



	def hide(self):
		for check in self.checkboxes:
			check.pack_forget()

		self.apps.pack_forget()
		self.save_button.pack_forget()
		self.reset_button.pack_forget()
		
		self.delete_button.pack_forget()
		self.add_button.pack_forget()
		self.exit_button.pack_forget()
		#self.read_deletion.pack_forget()
		
	def destroy_all(self):
		self.frame.destroy()


