
# This application is released under the GNU General Public License 
# v3 (or, at your option, any later version). You can find the full 
# text of the license under http://www.gnu.org/licenses/gpl.txt. 
# By using, editing and/or distributing this software you agree to 
# the terms and conditions of this license. 
# Thank you for using free software!
#
#(c) Whise 2008,2009 <helderfraga@gmail.com>
#
# MateNu tray loader
# Part of the MateNu

import gtk
import sys
from Popup_Menu import add_image_menuitem
import os
try:
	INSTALL_PREFIX = open("/etc/matenu/prefix").read()[:-1] 
except:
	INSTALL_PREFIX = '/usr'
sys.path.append(INSTALL_PREFIX + '/lib/matenu')
import gettext
gettext.textdomain('matenu')
gettext.install('matenu', INSTALL_PREFIX +  '/share/locale')
gettext.bindtextdomain('matenu', INSTALL_PREFIX +  '/share/locale')
import backend

class MateNu():


	def __init__(self):
		self.tray = gtk.StatusIcon()

		#app = mateapplet.Applet()
		#g = MateNu(app,"")
		self.tray.connect("activate", self.ShowMenu)
		self.tray.connect("popup-menu", self.show_menu)
		self.menu = gtk.Menu()
		self.m = gtk.Menu()
		add_image_menuitem(self.menu, gtk.STOCK_PROPERTIES, _("Preferences"), self.properties)
		add_image_menuitem(self.menu, gtk.STOCK_ABOUT, _("About"), self.about_info)
		add_image_menuitem(self.menu, gtk.STOCK_EDIT, _("Edit Menus"), self.edit_menus)
		add_image_menuitem(self.menu, gtk.STOCK_QUIT, _("Quit"), self.end)

		self.tray.set_tooltip("MateNu")
		self.tray.set_visible(True)

		from Menu_Main import Main_Menu
		self.hwg = Main_Menu(self.HideMenu)
		import Globals as Globals
		self.Globals = Globals
		if Globals.Settings['Distributor_Logo']:
			import IconFactory as iconfactory
			self.iconfactory = iconfactory
			self.applet_button = self.iconfactory.GetSystemIcon('distributor-logo')
		else: self.applet_button = self.Globals.Applogo
		pixbuf = gtk.gdk.pixbuf_new_from_file(self.applet_button)
		self.tray.set_from_pixbuf(pixbuf)
		self.show = False
		gtk.main()		
		#app.reparent(main_window)


	def end(self,widget,event=None):
		self.hwg.destroy()
		gtk.main_quit()

	def edit_menus(self,event, data=None):
		os.system(self.Globals.Settings['MenuEditor'] + ' &')
		#ConstructMainMenu()

	def show_menu(self, status_icon, button, activate_time):
		self.menu.popup(None, None, None, button,  activate_time)
		self.menu.show_all()

	def about_info(self,event,data=None):

		os.system("/bin/sh -c " + INSTALL_PREFIX +"'/lib/"+self.Globals.appdirname+"/MateNu-Settings.py --about' &")

	def properties(self,event,data=None):

		#os.spawnvp(os.P_WAIT,Globals.ProgramDirectory+"MateNu-Settings.py",[Globals.ProgramDirectory+"MateNu-Settings.py"])
		os.system("/bin/sh -c '"+self.Globals.ProgramDirectory+"MateNu-Settings.py' &")
		# Fixme, reload stuff properly

	def ShowMenu(self,widget):
		if self.show == False:


			#rootwin = self.hwg.window.get_screen().get_root_window()
			#x, y, mods = rootwin.get_pointer()
			x,y,z = gtk.status_icon_position_menu(self.m, self.tray)
			if self.hwg:
				if not self.hwg.window.window:
					if y < gtk.gdk.screen_height()/2:
						backend.save_setting('orientation', 'top')
					else:
						backend.save_setting('orientation', 'bottom')				
			self.hwg.Adjust_Window_Dimensions(x,y)
			self.hwg.show_window()
			self.show = True
		else:
			self.HideMenu()

	def HideMenu(self):
		self.show = False
		if self.hwg:
			if self.hwg.window.window:
				if self.hwg.window.window.is_visible()== True:
					self.hwg.hide_window()

if __name__ == '__main__':
    MateNu()
    sys.exit(0)


