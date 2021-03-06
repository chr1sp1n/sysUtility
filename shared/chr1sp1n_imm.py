
import os
import sys
import gi
import time
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GObject
from threading import Thread
from chr1sp1n_labas_sensors import North

class IconMenuMaker:

    """Icon Maker class"""
    menu_items = 0

    def __init__(self, app_id, icon = None):
        self.north = North()
        self.app_id = app_id
        if icon == None:
            icon = os.path.abspath(os.path.dirname(__file__) + '/assets/imm.svg')
        self.menu = Gtk.Menu()
        self.indicator = AppIndicator3.Indicator.new(self.app_id, icon, AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_title("Labas utility")
        
    def start(self):
        self.menu.show_all()
        self.indicator.set_menu(self.menu)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.update = Thread(target = self.get_north)
        self.update.setDaemon(True)
        self.update.start()

    def add_menu_item(self, text, function):
        item = Gtk.MenuItem(text)
        item.set_name(self.app_id + '_menu_item_' + str(self.menu_items))
        item.connect('activate', function)
        self.menu.append(item)
        self.menu_items += 1

    def add_menu_separator(self):
        self.menu.append(Gtk.SeparatorMenuItem())

    def get_north(self):
        while True:
            time.sleep(1)
            n = 'North: ' + str(self.north.read())
            GObject.idle_add( self.indicator.set_title, n, priority = GObject.PRIORITY_DEFAULT )
