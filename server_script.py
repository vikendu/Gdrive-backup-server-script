from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
from datetime import datetime

import glob
import os 

# Authentication Flow started :
gauth = GoogleAuth() 

#check if fresh login or not
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
	gauth.GetFlow()
	gauth.flow.params.update({'access_type': 'offline'})
	gauth.flow.params.update({'approval_prompt': 'force'})

	gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
    
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

# Authentication flow ends

drive = GoogleDrive(gauth) 
path = r"THE DIR THAT YOU WANT TO UPLOAD GOES HERE"

dir = os.listdir(path)

if len(dir) == 0:

	#Create a folder for the upload; named according to day
	folderName = datetime.today().strftime('%Y-%m-%d')
	folder = drive.CreateFile({'title': folderName, "mimeType": "application/vnd.google-apps.folder"})
	folder.Upload() 

	# iterating throught all the files/folder 
	# of the desired directory 
	for x in os.listdir(path): 

		f = drive.CreateFile({'title': x,  'parents': [{'id': folder['id']}]})
		f.SetContentFile(os.path.join(path, x)) 
		f.Upload() 
		f = None

	
	files = glob.glob(path + '/*')
	for f in files:
		os.remove(f)
