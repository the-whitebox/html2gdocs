# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# # Load client information from the JSON
# client_config = {
#     "installed": {
#         "client_id": "270608701232-kv7sengfie8e5gbihukjo0afni3glnvq.apps.googleusercontent.com",
#         "project_id": "driveservices-398805",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_secret": "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",
#         "redirect_uris": ["http://localhost"]
#     }
# }

# # Initialize GoogleAuth and GoogleDrive objects with the client configuration
# gauth = GoogleAuth()
# gauth.settings["client_config"] = client_config
# drive = GoogleDrive(gauth)

# # Create GoogleDriveFile instance with title 'Hello.txt'.
# file_title = 'index.html'  # Desired title for the file in Google Drive
# local_file_path = 'index.html'  # Path to the HTML file you want to upload

# file1 = drive.CreateFile({'title': file_title})

# # Set the content of the file from the local HTML file
# file1.SetContentFile(local_file_path)
# file1.Upload()

# print('title: %s, id: %s' % (file1['title'], file1['id']))




from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload 

# Path to your service account credentials JSON file
service_account_file = 'service_account_credentials.json'

# Initialize the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    service_account_file, scopes=['https://www.googleapis.com/auth/drive'])

# Create a Google Drive service instance
drive_service = build('drive', 'v3', credentials=credentials)

# Specify the file you want to upload

file_metadata = {
<<<<<<< HEAD
    'name': 'test_output.html',
    'parents': ['1YMsURSzYgp9A9bOYXwqrkW52J5XIDsi2']  # Add the folder ID where you want to upload the file
}
# Path to the local HTML file you want to upload
local_file_path = 'jinja/test_output.html'
=======
    'name': 'sample.html',
    'parents': ['1YMsURSzYgp9A9bOYXwqrkW52J5XIDsi2']  # Add the folder ID where you want to upload the file
}
# Path to the local HTML file you want to upload
local_file_path = 'sample.html'
>>>>>>> 00a560fbf5feea7c75937daaf4ed9253f986b2b3

# Upload the file
media_body = MediaFileUpload(local_file_path, mimetype='text/html')
uploaded_file = drive_service.files().create(
    body=file_metadata,
    media_body=media_body,
    fields='id'
).execute()

<<<<<<< HEAD
print('File ID: {}'.format(uploaded_file.get('id')))
=======
print('File ID: {}'.format(uploaded_file.get('id')))



>>>>>>> 00a560fbf5feea7c75937daaf4ed9253f986b2b3
