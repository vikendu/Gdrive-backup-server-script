# Gdrive-backup-server-script  
Schedule a backup using a cron job or something else.  

Setup requires getting client_secrets.json:  
https://medium.com/analytics-vidhya/how-to-connect-google-drive-to-python-using-pydrive-9681b2a14f20

Warnings:  
1. Deletes all files from the local dir.  
2. For some reason browser based authentication does not work on ARM64 platforms(needed for first time auth).    
3. So first run in a virtualised env, and then copy the script over to ARM with 'mycreds.txt' file in the working dir.  
4. Subfolders will get ignored.
