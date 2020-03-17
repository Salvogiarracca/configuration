import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import os

SCREENLAYOUT_PATH = "/home/giuseppe/.config/cheatsheets"

layouts = []

def  read_layouts():
    for el in os.listdir(SCREENLAYOUT_PATH):
        layouts.append((el,))

class LayoutMenuWindows(Gtk.ApplicationWindow):

    def __init__(self):
        Gtk.Window.__init__(self, title="CheatsheetViewer")

        self.set_default_size(200, 200)

        # Setting up the self.grid in which the elements are to be positionned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Creating the ListStore model
        self.software_liststore = Gtk.ListStore(str)
        for software_ref in layouts:
            # self.software_liststore.append(list(software_ref))
            self.software_liststore.append(list(software_ref))

        # creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView(model=self.software_liststore)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Cheatsheet", renderer, text=0)
        self.treeview.append_column(column)


        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

        self.treeview.connect("row-activated", self.signal_handler, self.treeview.get_selection())


    def signal_handler(self, treeview, path, column, param):
        (model, iter) = param.get_selected()
        os.system("st -t 'CheatsheetViewer' -e /home/giuseppe/.config/i3/CheatsheetsViewer/Cheatsheet_viewer.sh " + model[iter][0])
        self.close()

if __name__ == "__main__":
    read_layouts()
    win = LayoutMenuWindows()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()