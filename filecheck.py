import hashlib
import aes

def Main():
	print("Choose:\n 1.For file to sha256 \n 2.File to MD5 \n 3.AES ")
	ans = raw_input("Option: ")
	
	if ans == '1':
		sha256f()
	elif ans == '2':
		md5f()
	elif ans == '3':
		aes.Main()
	else:
		print ("invalid option")
		Main()
		

def sha256f():
	file = hashlib.sha256()
	filename = raw_input('Please enter the file name: ')

	with open(filename, 'rb') as bfile:
		binary = bfile.read()
		file.update(binary)
		print(file.hexdigest())


def md5f():

	file = hashlib.md5()
	filename = raw_input('Please enter the file name: ')
	
	with open(filename, 'rb') as bfile:
		binary = bfile.read()
		file.update(binary)
	print(file.hexdigest())

if __name__ == '__main__':
	Main()
