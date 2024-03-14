import os
import shutil

def main():
    folder_path = "./config"
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)  # Deletes the folder and its contents
            print(f"Folder '{folder_path}' deleted successfully.")
        except OSError as e:
            print(f"Error: {e.strerror}")
    else:
        print(f"Folder '{folder_path}' does not exist.")

if __name__ == "__main__":
        main()