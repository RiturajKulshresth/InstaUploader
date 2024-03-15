import requests
import os
import urllib.request
import json
from PIL import Image
import Creds
def get_random_photos(client_id, count=10, query='Wallpaper', orientation='portrait'):
    try:
        url = f"https://api.unsplash.com/photos/random/?client_id={client_id}&count={count}"
        if query:
            url += f"&query={query}"
        if orientation:
            url += f"&orientation={orientation}"
        
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # If successful, return the list of random photos
            return response.json()
        else:
            # If not successful, print the status code
            print(f"Failed to get random photos. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Print any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return None

def download_photos(photos, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        for idx, photo in enumerate(photos):
            photo_url = photo['urls']['full']
            file_path = os.path.join(download_path, f"photo_{idx + 1}.jpg")
            urllib.request.urlretrieve(photo_url, file_path)
            print(f"Downloaded photo {idx + 1} to {file_path}")
    except Exception as e:
        print(f"An error occurred while downloading photos: {e}")


def adjust_aspect_ratio(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get current aspect ratio
    width, height = img.size
    aspect_ratio = width / height

    # Define target aspect ratio (4:5)
    target_aspect_ratio = 4 / 5

    # Calculate the target width and height based on the aspect ratio
    new_height=height
    new_width=width
    if aspect_ratio > target_aspect_ratio:
        # Crop the image horizontally
        new_width = int(height * target_aspect_ratio)
        left = (width - new_width) // 2
        right = left + new_width
        img = img.crop((left, 0, right, height))
    else:
        # Crop the image vertically
        new_height = int(width / target_aspect_ratio)
        top = (height - new_height) // 2
        bottom = top + new_height
        img = img.crop((0, top, width, bottom))

    # Resize the cropped image to fit the 4:5 aspect ratio
    img = img.resize((new_width, new_height), Image.LANCZOS)

    # Replace the original image with the adjusted image
    img.save(image_path)




# Example usage:
if __name__ == "__main__":
    # Replace 'YOUR_CLIENT_ID' with your actual Unsplash API client ID

    
    # Example usage with additional parameters:
    photos = get_random_photos(Creds.client_id, count=1, query='Wallpaper', orientation='portrait')
    print(photos[0]['description'])
    print(photos[0]['alt_description'])

    if photos:
        download_path = "."
        download_photos(photos, download_path)

        # Create a list to store descriptions
        descriptions = []
        for idx, photo in enumerate(photos):
            description = photo.get('description', 'No description')
            alt_description = photo.get('alt_description', 'No alt description')
            descriptions.append({
                'Photo': idx + 1,
                'Description': description,
                'Alt Description': alt_description
            })

        # Save descriptions as JSON
        with open("photo_descriptions.json", "w") as json_file:
            json.dump(descriptions, json_file, indent=4)
        
        print("Descriptions saved to 'photo_descriptions.json'")

        input_image_path="./photo_1.jpg"
        aspect_ratio=1
        while(aspect_ratio!=0.8):
            # output_image_path = "./downloaded_photos/photo.jpg"
            img1 = Image.open(input_image_path)
            width, height = img1.size
            aspect_ratio = width / height
            print(width, height, aspect_ratio)
            adjust_aspect_ratio(input_image_path)
        
        # cropped_image.save(output_image_path)
    else:
        print("Failed to get random photos.")
