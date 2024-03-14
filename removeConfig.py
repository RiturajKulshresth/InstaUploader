import os
import shutil

def main():
    folder_path = "./config"
    Cred_path = "./Creds.py"
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)  # Deletes the folder and its contents
            print(f"Folder '{folder_path}' deleted successfully.")
        except OSError as e:
            print(f"Error: {e.strerror}")
    else:
        print(f"Folder '{folder_path}' does not exist.")

    if os.path.exists(Cred_path):
        try:
            os.remove(Cred_path)  # Deletes the folder and its contents
            print(f"File '{Cred_path}' deleted successfully.")
        except OSError as e:
            print(f"Error: {e.strerror}")
    else:
        print(f"File '{Cred_path}' does not exist.")

if __name__ == "__main__":
        main()