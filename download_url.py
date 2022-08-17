from mega import Mega


mega = Mega()
m = mega.login(email, password)

# FIND FILE
file = m.find('myfile.doc')

# THEN DOWNLOAD USING THE FILE OBJECT
m.download(file)

# DOWNLOAD FILE USING MEGA FILE URL
m.download_url(
	'https://mega.co.nz/#!3tUF2KQD!Rg-zOOUIs9L\
	ipsqwH9c_9ZOfRjZ48Xb5k2I1M6QTMa4')

# SPECIFY DOWNLOAD LOCATION
m.download(file, '/home/john-smith/Desktop')
