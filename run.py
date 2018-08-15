# !/usr/bin/python3.6

import signal
import os
import sys
import gi
gi.require_version('Gtk', '3.0')
sys.path.append(os.path.abspath('./shared'))
from gi.repository import Gtk, GObject
from chr1sp1n_imm import IconMenuMaker
from gi.repository import Notify

APPINDICATOR_ID = 'chr1sp1n_system_utility'

def ciao(self):
	self.set_label("HELLO WORLD!")
	Notify.Notification.new(" < b > Joke < /b > ", 'fetch_joke()', None).show()

def quit(self):
	Notify.uninit()
	Gtk.main_quit()

if __name__ == "__main__":
	
	GObject.threads_init()
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	Notify.init(APPINDICATOR_ID)

	imm = IconMenuMaker(APPINDICATOR_ID)
	imm.add_menu_item('Ciao', ciao)
	imm.add_menu_separator()
	imm.add_menu_item('Quit', quit)

	imm.start()
	Gtk.main()


