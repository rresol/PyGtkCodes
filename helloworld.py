#!/usr/bin/env python

#example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
    
    #This is a callback function.The data arguments are ignored 
    #in this example. More on callbacks below.
    def hello(self,widget,data=None):
        print "Hello World"
    
    def delete_event(self,widget,event,data=None):
        #If you return FALSE in the "delete_event" signal handler,
        #GTK will emit the "destroy" signal. Returning TRUE means
        #you dont want the window to be destroyed.
        #This is useful for popping 'are you sure you want to quit?'
        #type dialogs.
        print "delete event occured"
    
        #change FALSE to TRUE and the main window will not be 
        #destroyed with a "delete_event"
        return False
    
    #Another Callback
    def destroy(self,widget,data=None):
        gtk.main_quit()

    def __init__(self):
        #create new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        #when the window is given the "delete_event" signal (this 
        #is given by the window manager, usually by the close 
        # option,or on the titlebar), we ask it to call the 
        #delete_event() function as defined above . data passed 
        # will be null and hence will be ignored.
        self.window.connect("delete_event",self.delete_event)
        
        #Now we connect "destroy" event to the signal handler.
        #This event occurs when we call gtk_widget_destroy() on
        #the window,or if we return FALSE in the delete_event
        #callback function.
        self.window.connect("destroy",self.destroy)

        #sets the border width of the window
        self.window.set_border_width(10)
        
        #creates a new button with the label "Hello World".
        self.button = gtk.Button("Hello World")
        
        #when the button recieves the "clicked" signal, it
        #will call the function hello() passing it None as
        #its argument .The hello() function is defined
        self.button.connect("clicked",self.hello,None)

        #This will destroy the window by calling 
        #gtk_widget_destroy(window) again signal can
        #be genrated by window manager or here itself.
        self.button.connect_object("clicked",gtk.Widget.destroy,self.window)

        #this packs the button into a window
        self.window.add(self.button)
    
        #this final step is to show newly created widget.
        self.button.show()
        
        #and the window
        self.window.show()
        
    def main(self):
        #All PyGtk Apps must have gtk.main() all control ends here
        #and waits for events to occur(like a key press or mouse event)
        gtk.main()
     

if __name__ =="__main__":
    hello = HelloWorld()
    hello.main()
                 
