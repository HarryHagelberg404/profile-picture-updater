import os

def extract_credentials(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("USERNAME="):
                username = line.split("=")[1].strip()
            if line.startswith("PASSWORD="):
                password = line.split("=")[1].strip()
    return username, password

file_path = ".env"
username, password = extract_credentials(file_path)
print("Username:", username)
print("Password:", password)

# Update Twitter
# Update Github
