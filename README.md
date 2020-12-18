# Gdrive-backup-server-script  
Schedule a backup using a cron job or something else.  

Setup requires getting client_secrets.json:  
https://medium.com/analytics-vidhya/how-to-connect-google-drive-to-python-using-pydrive-9681b2a14f20   

You also need pydrive `pip3 install PyDrive`  
  
A few dependencies whose latest versions break the script when uploading large files  
So install the older versions as follows  
`pip3 install httplib2==0.15.0`  
`pip install google-api-python-client==1.6`

Warnings:  
1. Deletes all files from the local dir after uploading.  
2. For some reason browser based authentication does not work on ARM64 platforms(needed for first time auth).    
3. So first run in a virtualised env, and then copy the script over to ARM with 'mycreds.txt' file in the working dir.  
4. Subfolders will get ignored.
