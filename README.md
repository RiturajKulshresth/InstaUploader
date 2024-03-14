# InstaUploader

Welcome to InstaUploader! This is a tool designed to simplify the process of uploading images to Instagram. 

## Setup Instructions

1. **Creds File Configuration**: 
   - Create a `creds.py` file in the root directory of the application.
   - Inside `creds.py`, enter the correct values for the following variables:
     ```python
     client_id = ''
     username = ''
     password = ''
     ```

2. **Modify Instabot Library**:
   - Comment out lines 560 to 586 in `api.py` of the Instabot library.
   - Comment out line 556 in `api.py` to suppress unnecessary logs.
   - Location: `/home/<username>/anaconda3/lib/python3.11/site-packages/instabot/api/api.py`

3. **Edit Image Resizing Method**:
   - Replace `Image.ANTIALIAS` with `Image.LANCZOS` in `api_photos.py`.
   - Location: `/home/<username>/anaconda3/lib/python3.11/site-packages/instabot/api/api_photo.py`
   - Update: PIL's ANTIALIAS method has been renamed to LANCZOS as of version 2.7.0.

## Running the Application

- One way to run the application is by executing `python gui.py`. This will open a Tkinter GUI where you can enter your client ID from Unsplash and your Instagram account details.
- Another Way to ruin this application is by manually adding the `creds.py` file and running `python launcher.py`:
   ```python
     client_id = ''
     username = ''
     password = ''
     ```

## ToDo

- Implement a scheduler for daily uploads.
- Let users choose a folder instead of downloading

Feel free to contribute to this project and enhance its functionality!

--- 

**Note**: Replace `<username>` in file paths with your actual username.
