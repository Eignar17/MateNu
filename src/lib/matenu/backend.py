#!/usr/bin/env python

# All references to "mateconf" gone

# This application is released under the GNU General Public License 
# v3 (or, at your option, any later version). You can find the full 
# text of the license under http://www.gnu.org/licenses/gpl.txt. 
# By using, editing and/or distributing this software you agree to 
# the terms and conditions of this license. 
# Thank you for using free software!
#
#
# backend for saving and loading settings
# Part of the MateNu

import os

import xml.dom.minidom
print "xml backend"

HomeDirectory = os.path.expanduser("~")
ConfigDirectory = HomeDirectory + '/.matenu'
mateconf_app_key = '/apps/matenu'

def save_setting(name,value):
	if name == '': return
	if os.path.isfile(ConfigDirectory + "/.MateNu-Settings.xml"):
		XMLSettings = xml.dom.minidom.parse(ConfigDirectory + "/.MateNu-Settings.xml")
		XBase = XMLSettings.getElementsByTagName('matenu')[0]
	else:
		XMLSettings = xml.dom.minidom.Document()
		XBase = XMLSettings.createElement('matenu')

	try:
		node = XMLSettings.getElementsByTagName('settings')[0]
	except:
		node = XMLSettings.createElement('settings')
	node.setAttribute(name, str(value))
	XBase.appendChild(node)
	XMLSettings.appendChild(XBase)
	file = open(ConfigDirectory + "/.MateNu-Settings.xml","w")
	XMLSettings.writexml(file, "    ", "", "", "UTF-8")
	XMLSettings.unlink()

def load_setting(name):
	if os.path.isfile(ConfigDirectory + "/.MateNu-Settings.xml"):
		XMLSettings = xml.dom.minidom.parse(ConfigDirectory + "/.MateNu-Settings.xml")
		#print XMLSettings.getElementsByTagName('matenu')[0].childNodes[0].localName
		x = XMLSettings.getElementsByTagName('matenu')[0].getElementsByTagName("settings")[0]
		try:
			x = x.attributes[name].value
			try: 
				a = int(x)
			except:
				if str(x).find('[]') != -1 and name == 'favorites': return []
				if str(x).find(':') != -1:					
					x = str(x).replace(" u'","").replace("u'","").replace("[","").replace("]","").replace("'","").replace('&quot;','"')
					a = x.split(',')
					print a				
				else:
					a = str(x)
			return a
		except: 
			if name == 'favorites': return []
			return None
	else: 
		return None

def get_default_mail_client():
	return "xdg-open mailto:"

def get_default_internet_browser():
	return "xdg-open http:"
