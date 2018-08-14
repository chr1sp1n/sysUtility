
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import os
import sys

class IconMenuMaker:

    """Icon Maker class"""
    indicator = None

    def __init__(self, imm_id, icon = None):
        if icon == None:
            icon = os.path.abspath(os.path.dirname(__file__) + '/assets/imm.svg')
        self.menu = gtk.Menu()
        self.indicator = appindicator.Indicator.new(imm_id, icon, appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.add_menu_item('Quit', gtk.main_quit)
        self.state(True)

    def state(self, state_val=None):
        if state_val != None:
            self.indicator.set_status(state_val)
        return self.indicator.get_status()

    def add_menu_item(self, text, function):
        item = gtk.MenuItem(text)
        item.connect('activate', function)
        self.menu.append(item)
        self.menu.show_all()
        self.indicator.set_menu(self.menu)

    def activate(self):
        gtk.main()

