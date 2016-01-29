__author__ = 'rresol'
__email__  = 'shashank.kumar.apc13@itbhu.ac.in'

import pygtk
pygtk.require('2.0')
import gtk

class TreeViewPrac:

	def delete_event(self,widget,event,data=None):
		gtk.main_quit()
		return False

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("My expe")
		self.window.connect("delete_event",self.delete_event)

		self.liststore = gtk.ListStore(str,str)

		self.treeview = gtk.TreeView(self.liststore)

		self.tvcolumn = gtk.TreeViewColumn("Name")
		self.tvcolumn1 = gtk.TreeViewColumn("Amount")

		self.liststore.append(['Shashank','190'])
		self.liststore.append(['Tanmay','293'])
		self.liststore.append(['Harsh','934'])

		self.treeview.append_column(self.tvcolumn)
		self.treeview.append_column(self.tvcolumn1)

		self.cell = gtk.CellRendererText()
		self.cell1 = gtk.CellRendererText()

		self.cell.set_property('cell-background','yellow')
		self.cell1.set_property('cell-background','cyan')

		self.tvcolumn.pack_start(self.cell,True)
		self.tvcolumn1.pack_start(self.cell1,True)

		self.tvcolumn.set_attributes(self.cell,text =0)
		self.tvcolumn1.set_attributes(self.cell1,text=1 )

		self.treeview.set_search_column(0)
		self.tvcolumn1.set_sort_column_id(1)

		self.treeview.set_reorderable(True)

		self.window.add(self.treeview)

		self.window.show_all()

def main():
	gtk.main()

if __name__ == '__main__':
	tvcex = TreeViewPrac()
	main()