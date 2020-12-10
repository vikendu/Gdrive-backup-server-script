from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
from datetime import datetime

import glob
import os 

print('©2020 Vikendu Singh\nFeel free to share with others.\n')
print('Starting Authentication . . . ')

# Authentication Flow started :

# Put 'client_secrets.json' in the working dir.
gauth = GoogleAuth() 

#check if fresh login or not
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
  # Next 3 lines allow OAuth token to refresh after 1Hr.
	# Instead of opening browser again & again
	gauth.GetFlow()
	gauth.flow.params.update({'access_type': 'offline'})
	gauth.flow.params.update({'approval_prompt': 'force'})

	# OAuth token generated here, login via browser required
	gauth.LocalWebserverAuth()

elif gauth.access_token_expired:
    gauth.Refresh()

else:
    gauth.Authorize()

# if not already present, 'mycreds.txt' will be created here
gauth.SaveCredentialsFile("mycreds.txt")

# Authentication flow end.

drive = GoogleDrive(gauth) 

path = r"THE DIR YOU WANT TO UPLOAD GOES HERE"

dir = os.listdir(path)
i = 1

if len(dir) != 0:

	#Create a folder for the upload
	print('Authentication Successful!')
	print('Enter a name for the folder: ')
	folderName = input()
	folder = drive.CreateFile({'title': folderName, "mimeType": "application/vnd.google-apps.folder"})
	folder.Upload() 

	print('Found '+str(len(dir))+' files: ')

	# iterating thought all the files/folder of the desired directory 
	for x in os.listdir(path): 

		print('Uploading file '+str(i)+' of '+str(len(dir))+'. . .', end = " ")
		f = drive.CreateFile({'title': x,  'parents': [{'id': folder['id']}]})
		f.SetContentFile(os.path.join(path, x)) 
		f.Upload() 
		f = None # Apparently there is a memory leak if var not emptied
		print('Done\n')
		i = i + 1

	
	files = glob.glob(path + '/*')

	print('Deleting contents of the local dir ...', end = " ")
	for f in files:
		os.remove(f)
	
	print('Done')
else:
	print('Authentication Successful.\nNo files found in directory.')
