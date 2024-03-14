import subprocess

# Function to execute a Python script
def execute_script(script_name):
    subprocess.run(["python", script_name])

# Execute the first script
execute_script("getPhotos.py")
    
execute_script("Post.py")

# Execute the second script
execute_script("removeConfig.py")
