InstaUploader
Welcome to InstaUploader! This is a tool designed to simplify the process of uploading images to Instagram.

Setup Instructions
Creds File Configuration:

Create a creds.py file in the root directory of the application.
Inside creds.py, enter the correct values for the following variables:
python
Copy code
client_id = ''
username = ''
password = ''
Modify Instabot Library:

Comment out lines 560 to 586 in api.py of the Instabot library.
Comment out line 556 in api.py to suppress unnecessary logs.
Location: /home/<username>/anaconda3/lib/python3.11/site-packages/instabot/api/api.py
Edit Image Resizing Method:

Replace Image.ANTIALIAS with Image.LANCZOS in api_photos.py.
Location: /home/<username>/anaconda3/lib/python3.11/site-packages/instabot/api/api_photo.py
Update: PIL's ANTIALIAS method has been renamed to LANCZOS as of version 2.7.0.
Running the Application
One way to run the application is by executing python gui.py. This will open a Tkinter GUI where you can enter your client ID from Unsplash and your Instagram account details.
ToDo
Implement a scheduler for daily uploads.
Beautify this README file for better readability and aesthetics.
Feel free to contribute to this project and enhance its functionality!

Note: Replace <username> in file paths with your actual username.
