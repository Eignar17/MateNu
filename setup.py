#
# This application is released under the GNU General Public License 
# v3 (or, at your option, any later version). You can find the full 
# text of the license under http://www.gnu.org/licenses/gpl.txt. 
# By using, editing and/or distributing this software you agree to 
# the terms and conditions of this license. 
# Thank you for using free software!

#(c) Whise 2009 <helderfraga@gmail.com>
#

# Install translation files
# Part of the MateNu

import os
try:
	INSTALL_PREFIX = open("/etc/matenu/prefix").read()[:-1] 
except:
	INSTALL_PREFIX = '/usr'

#files = ['src/lib/matenu/MATE_MateNu.server','src/share/mate-do/MateNu.desktop']

f = open('src/lib/matenu/MATE_MateNu.server').read()
r = f.replace('/usr/lib/matenu/',INSTALL_PREFIX + '/lib/matenu/')
a = open('src/lib/matecomponent/MATE_MateNu.server','w')
a.write(r)
a.close()

print ('Preparing to install translation')
podir = os.path.join (os.path.realpath ("."), "po")
print (podir)
if os.path.isdir (podir):
	print ('installing translations')
	buildcmd = "msgfmt -o src/share/locale/%s/LC_MESSAGES/%s.mo po/%s.po"
	
	for name in os.listdir (podir):		
		if name.endswith('.po'):
			dname = name.split('-')[1].split('.')[0]
			name = name[:-3]
			
			print ('Creating language Binary for : ' + name)
			if not os.path.isdir ("src/share/locale/%s/LC_MESSAGES" % dname):
				os.makedirs ("src/share/locale/%s/LC_MESSAGES" % dname)
			os.system (buildcmd % (dname,name.replace('-'+dname,''), name))
			
				

