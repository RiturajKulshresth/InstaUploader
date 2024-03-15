from instabot import Bot
import json
import Creds
# import removeConfig

# import os
# import shutil
def main():
    file_path = './photo_descriptions.json'
    with open(file_path, 'r') as file:
        # Load JSON data from the file
        data = json.load(file)

    # description = data[0]["Alt Description"]+"\n"+data[0]["Description"]
    description = ""
    if data[0]["Alt Description"]:
        description += data[0]["Alt Description"] + "\n"
    if data[0]["Description"]:
        description += data[0]["Description"]

    # Initialize Instabot
    bot = Bot()

    # Login to your Instagram account
    bot.login(username=Creds.username, password=Creds.password)


    # Specify the image file path and caption
    image_path = "./photo_1.jpg"

    # Post the image with the specified caption
    bot.upload_photo(image_path, caption=description)

    # Logout from your Instagram account
    bot.logout()
    # removeConfig.main()

# def step_3():
#     folder_path = "./config"
#     if os.path.exists(folder_path):
#         try:
#             shutil.rmtree(folder_path)  # Deletes the folder and its contents
#             print(f"Folder '{folder_path}' deleted successfully.")
#         except OSError as e:
#             print(f"Error: {e.strerror}")
#     else:
#         print(f"Folder '{folder_path}' does not exist.")

if __name__ == "__main__":
    main()

    # step_3()
