__author__ = 'rresol'

#example table.py 

import pygtk
import gtk    
pygtk.require('2.0') #specifying to use pygtk 2.x even u 
                     # pygtk 3.x

class Table:
    #Our callback.
    #The data passed to this method is printef to stdout
    def callback(self,widget,data=None):
        print "Hello again -%s was presed" %data

    #This call back quites the program
    def delete_event(self,widget,event,data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        #Create a new Window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        #Set the window title
        self.window.set_title("Table")

        #set a handler for delete_event that immediately
        #exits GTK.
        self.window.connect("delete_event",self.delete_event)

        #Sets the border width of the window.
        self.window.set_border_width(20)

        #Create a 2x2 table
        table = gtk.Table(2,2,True)

        #Put the table in the main window
        self.window.add(table)

        #Create the first button 
        button = gtk.Button("button 1")

        #When the button is clicked we call the "callback" method.
        #with a pointer to button 1 as its argument.
        button.connect("clicked",self.callback,"button 1")

        #Insert button 1 to upper left quadrant of the table.
        table.attach(button,0,1,0,1)

        button.show()

        #Create a second button
        button = gtk.Button("button 2")

        #When the button is clicked , we call the "callback" method
        #with a pointer to "button 2" as its argument
        button.connect("clicked",self.callback,"button 2")
        #Insert button 2 into the upper right quadrant of the table
        table.attach(button,1,2,0,1)

        button.show()

        #Create "Quit" button
        button = gtk.Button("Quit")
        button.connect("clicked",lambda w: gtk.main_quit())

        #insert the quit button into the both lower quadrants of the table.
        table.attach(button,0,2,1,2)

        button.show()

        table.show()
        self.window.show()

def main():
    gtk.main()
    return 0

if __name__ == '__main__':
    Table()
    main()

