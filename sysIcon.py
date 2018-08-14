# !/usr/bin/python3.6

import signal
import os
import sys
sys.path.append(os.path.abspath('./shared'))
import chr1sp1n_imm

def ciao(self):
	os.system('notify-send "TITLE" "MESSAGE"')

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	imm = chr1sp1n_imm.IconMenuMaker('chr1sp1n_system_utility')
	imm.add_menu_item('Ciao', ciao)
	imm.activate()


