import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key, filename):
	chunksize = 64*1024
	outPutFile = 'encrypted'+filename
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = ''
	
	for i in range(16):
		IV +=chr(random.randint(0,0xFF))
	
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	
	with open(filename, 'rb') as infile:
		with open(outPutFile, 'wb') as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			
			while True:
				chunk = infile.read(chunksize)
			
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
						chunk += ' ' * (16 - (len(chunk) % 16)) 
						
						outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
	chunksize = 64*1024
	outPutFile = filename[11:]
	
	with open(filename, 'rb') as infile:
		filesize = long(infile.read(16))
		IV = infile.read(16)
		
		decryptor = AES.new(key, AES.MODE_CBC, IV)
		
		with open(outPutFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)
				
				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))
				
			outfile.truncate(filesize)
			
def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()
	
def Main():
	choice = raw_input("would you like to Encrpt or Decrypt?")
	
	
	if choice == 'E':
		filename = raw_input("file to E: ")
		password = raw_input("password to E: ")
		encrypt(getKey(password), filename)
		
		print("Done.")
		
	elif choice == 'D':
		filename = raw_input("File to D: ")
		password = raw_input("Password: ")
		decrypt(getKey(password), filename)
		print("done.")
		
	else: print("no option select")
	
if __name__ == '__main__':
	Main()
