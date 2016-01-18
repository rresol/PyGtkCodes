#!/usr/bin/env python

#example-start buttons buttons.py

import pygtk
pygtk.require('2.0')
import gtk

#Create a new button with an image and a label packed into ut
#and return the box

def xpm_label_box(parent,xpm_filename,label_text):
	#Create box for xpm and label
	box1 = gtk.HBox(False,0)
	box1.set_border_width(2)

	#Now on to the image stuff
	image = gtk.Image()
	image.set_from_file(xpm_filename)

	#Create a label for the button
	label = gtk.Button(label_text)

	#Pack the pixmap and label into the box
	box1.pack_start(image,False,False,3)
	box1.pack_start(label,False,False,3)

	image.show()
	label.show()
	return box1

class Buttons:
	#Our usual callback method
	def callback(self,widget,data=None):
		print "Hello again - %s was pressed" %data

	def __init__(self):
	 	#Create a new Window.
	 	self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

	 	self.window.set_title("Image'd Buttons !")

	 	self.window.connect("destroy",lambda wid:gtk.mai_quit())
	 	self.window.connect("delete_event",lambda a1,a2:gtk.main_quit())

	 	#Sets the border width of the window.
	 	self.window.set_border_width(10)

	 	#Create a new button
	 	button = gtk.Button()

	 	#Connect the "clicked" signal of our button to our callback
	 	button.connect("clicked",self.callback,"cool button")

	 	box1 = xpm_label_box(self.window,"info.xpm","cool button")

	 	button.add(box1)

	 	box1.show()

	 	button.show()
	 	self.window.add(button)
	 	self.window.show()

def main():
	gtk.main()
	return 0
if __name__ == '__main__':
	Buttons()
	main()