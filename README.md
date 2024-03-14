Create a Creds File in the root location of the application and Enter the correct values in the following
client_id =''
username=''
password=''

Comment Lines 560 to 586 in api.py of the instabot library 
/home/<username>/anaconda3/lib/python3.11/site-packages/instabot/api/api.py
Comment line 556 of the api.py file as it prints unnecesary logs

In the api_photos.py edit the Image.ANTIALIAS to  Image.LANCZOS
/home/<username>/anaconda3/lib/python3.11/site-packages/instabot/api/api_photo.py
PIL::ANTIALIAS method name update: As of 2.7.0, all resize methods are ANTIALIAS & the real (new) name for the specific ANTIALIAS filter is LANCZOS.

