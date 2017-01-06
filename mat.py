'''
Mysql Analytic Tool

MAT is a simple tool that created by Python language which used to analyze Mysql directory files. It is able to create image file for entire Mysql directory and analyze the log files from the image. This tool provides fastest and easiest way to analyze Mysql database to find out which data had been modified, inserted or deleted after an attack.

This tool is a prototype, may contain several bugs and lack of features. 

Contributor - Anson Tan
'''

import os
import sys
import fileinput

def man():
	print '\nMysql Analytic tool command list and description'
	print 'Command			- Description\n'
	print 'show binary filename	- show binary file'
	print 'show log		- show log files'
	print 'show history		- show mysql history'
	print 'show error		- show error log'
	print 'show query		- show general query file'
	print 'analyze binary filename	- analyze binary file, such as analyze binary mysql000.000'
	print 'create mysql		- create mysql image file'
	print 'mount mysql.iso		- mount an image file called mysql.iso'
	print 'unmount mysql.iso	- unmount an image file called mysql.iso\n'
	forensic()
		
#command line
def forensic():
	#input command line
	option = raw_input("\nmat > ")

	#show binary file	
	if option == 'show binary':
		#Accept binary file name from user input
		binaryfile = raw_input('\nEnter binary file name: ')
		#Read binary file
		os.system('mysqlbinlog ~/Downloads/mysql-iso/' + binaryfile)
		######ask user whether want to save file
		forensic()

	#show log files
	elif option == 'show log':
		os.system("ls -la ~/Downloads/mysql-iso")
		forensic()

	#show mysql history
	elif option == 'show history':
		os.system('cat /home/wk/.mysql_history')
		forensic()

	#show error log
	elif option == 'show error':
		print '\nError Log\n'
		os.system('cat ~/Downloads/mysql-iso/error.log')
		forensic()

	#detect mysql directory
	elif option == 'detect mysql':
		os.system('ls -l /var/log/mysql')
		forensic()

	#show general query file
	elif option == 'show query':
		print '\nGeneral Query Log\n'
		os.system('cat ~/Downloads/mysql-iso/mysql.log')
		forensic()

	#create mysql image file
	elif option == 'create mysql':
		con = raw_input("May takes a while to backup, type 'Yes' to proceed or 'R' to return : ")
		if con == 'Yes':
			os.system('sudo mkisofs -o ~/Downloads/mysql.iso /var/log/mysql')
			print '\n'

		elif con == 'R':
			forensic()
		else:
			print 'Invalid option'
			forensic()

	#mount mysql image file
	elif option == 'mount mysql.iso':
		os.system('sudo mkdir ~/Downloads/mysql-iso')
		os.system('sudo mount -o loop mysql.iso ~/Downloads/mysql-iso')
		forensic()

	#unmount mysql image flle
	elif option == '':
		os.system('sudo umount mysql-iso')
		forensic()

	elif option == 'analyze binary':
		#Accept binary file name
		filename = raw_input('Please input file name : ')
		#Open sum.sh but read only
		f1 = open('sum.sh', 'r')
		#Open analyze.sh but write only
		f2 = open('analyze.sh', 'w')
		for line in f1:
			#Copy all lines from sum.sh and replace user input into analyze.sh
			f2.write(line.replace('logfile', filename))
		f1.close()
		f2.close()
		#Execute analyze.sh
		os.system('. ~/Downloads/analyze.sh')
		print '\n'
		#Display menu options
		forensic()

	#mat command list and description
	elif option == 'man':
		man()

	#exit program
	elif option == 'exit':
		###################save into a file?
		sys.exit(1)

	#return to forensic function after accepted invalid input
	else:
		print 'Invalid option'
		forensic()
		

#Display menu options
#Menu options
print '\n*********************'
print '       MAT'
print 'MYSQL Analytics Tool'
print '*********************'
forensic()
