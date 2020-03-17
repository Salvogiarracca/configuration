import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk
import os
import sys
import pyperclip as cp

os.system('mkdir ~/.tasks')
# Insert only the filename if the file is in the same folder, otherwise insert the full path
FILE_NAME = os.path.expanduser('~/.tasks/tasks')

tasks_list = []

entryString = ""


def readTasks():
    del tasks_list[:]
    try:
        file = open(FILE_NAME, 'r')
    except IOError:
        file = open(FILE_NAME, 'w')

    try:
        lines = file.read().splitlines()
    except:
        lines = []

    for line in lines:
        if line != "":
            tupl = (line,)
            tasks_list.append(tupl)
    file.close()


class TreeViewFilterWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Treeview Filter Demo")
        self.set_border_width(10)

        # Setting up the self.grid in which the elements are to be positionned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Creating the ListStore model
        self.software_liststore = Gtk.ListStore(str)
        for software_ref in tasks_list:
            # self.software_liststore.append(list(software_ref))
            self.software_liststore.append(list(software_ref))
        self.current_filter_language = None

        # Creating the filter, feeding it with the liststore model
        self.language_filter = self.software_liststore.filter_new()
        # setting the filter function, note that we're not using the
        self.language_filter.set_visible_func(self.language_filter_func)

        # creating the treeview, making it use the filter as a model, and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Task", renderer, text=0)
        self.treeview.append_column(column)

        # creating buttons to filter by programming language, and setting up their events
        self.buttons = list()
        button = Gtk.Button("Create")
        self.buttons.append(button)
        button.connect("clicked", self.on_create_button_clicked)
        button = Gtk.Button('Delete')
        self.buttons.append(button)
        button.connect("clicked", self.on_delete_button_clicked)

        # setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

    def language_filter_func(self, model, iter, data):
        """Tests if the language in the row is the one in the filter"""
        if self.current_filter_language is None or self.current_filter_language == "None":
            return True
        else:
            return model[iter][2] == self.current_filter_language

    def on_create_button_clicked(self, widget):
        win = EntryWindow()
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        self.hide()

    def on_delete_button_clicked(self, widget):
        win = ConfirmWindow(delete_entry, self)
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()


class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Hello World")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.icon = Gtk.Button.new_with_label("OK")
        self.icon.connect("clicked", self.on_ok_toggled)
        hbox.pack_start(self.icon, True, True, 0)

        self.icon = Gtk.Button.new_with_label("Cancel")
        self.icon.connect("clicked", self.on_cancel_toggled)
        hbox.pack_start(self.icon, True, True, 0)

    def on_ok_toggled(self, button):
        tasks = open(FILE_NAME, 'a')
        tasks.write('\n')
        tasks.write(self.entry.get_text())
        tasks.close()
        self.close()
        createGtkWindow()

    def on_cancel_toggled(self, button):
        self.close()
        createGtkWindow()


# Call the class with the callback for the yes button, and the args for the callback function
# The callback arguments are:
#   caller - The ConfirmWindow instance
#   tuple_args - A tuple containing all the other args needed
class ConfirmWindow(Gtk.Window):

    def __init__(self, yes_callback, *callback_args):
        Gtk.Window.__init__(self, title="Are you sure?")
        self.set_size_request(200, 50)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        label = Gtk.Label("Are you sure?")
        vbox.pack_start(label, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.icon = Gtk.Button("Yes")
        self.icon.connect("clicked", self.on_yes_click, yes_callback, callback_args)
        hbox.pack_start(self.icon, True, True, 0)

        self.icon = Gtk.Button("No")
        self.icon.connect("clicked", self.on_no_click)
        hbox.pack_start(self.icon, True, True, 0)

    def on_yes_click(self, widget, yes_callback, callback_args):
        yes_callback(self, callback_args)
        createGtkWindow()

    def on_no_click(self, widget):
        self.hide()
        # createGtkWindow()


def createGtkWindow():
    readTasks()
    win = TreeViewFilterWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


# args: confirmWindow, gtktreeview
def delete_entry(caller, tuple_args):
    confirmWindow = caller
    gtktreeview = tuple_args[0]

    selection = gtktreeview.treeview.get_selection()
    selection.set_mode(Gtk.SelectionMode.BROWSE)
    model, iter = selection.get_selected()
    tlist = []
    for line in tasks_list:
        tlist.append(line[0])

    tlist.remove(model.get_value(iter, 0))
    file = open(FILE_NAME, 'w')
    for line in tlist:
        file.write(line + '\n')
    file.close()
    gtktreeview.close()
    confirmWindow.close()


def newLinecheck(string):
    for i, el in enumerate(string[::-1]):
        if not el.isspace():
            if i != 0:
                return string[:-i]
            else:
                return string
    exit(-1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--clipboard":
            cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
            content = cb.wait_for_text()
            print(content)
            if not (content.isspace() or content == ""):
                tasks = open(FILE_NAME, 'a')
                tasks.write('\n')
                cleanContent = newLinecheck(content)
                tasks.write(cleanContent)
                tasks.close()
                print('notify-send -u normal "Created task from clipboard" "' + cleanContent + '"')
                os.system(
                    'notify-send -u normal "Created task from clipboard" "' + cleanContent.replace('"', '\"') + '"')
                exit(0)

    createGtkWindow()
