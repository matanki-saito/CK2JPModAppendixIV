from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)

file1 = drive.CreateFile({
    'title': 'Hello.txt',
    'parents': [
        {
            "kind": "drive#fileLink",
            "id": '1MUdH6S6O-M_Y5jRUzNrzQ8tPZOhm_aES'
        }
    ]
})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello World!')  # Set content of the file from given string.
file1.Upload()

permission = file1.InsertPermission({
    'type': 'anyone',
    'value': 'anyone',
    'role': 'reader'})

file1.FetchMetadata()

# Fetches all metadata available.
# file1.FetchMetadata(fetch_all=True)

print(file1['id'])
