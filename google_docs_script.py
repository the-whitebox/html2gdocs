import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Define the path to your service account credentials JSON file
service_account_file = 'service_account_credentials.json'

# Initialize the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    service_account_file, scopes=['https://www.googleapis.com/auth/drive']
)

# Create a Google Drive API service instance
drive_service = build('drive', 'v3', credentials=credentials)

# Define the ID of the Google Drive folder containing your HTML files
folder_id = '1YMsURSzYgp9A9bOYXwqrkW52J5XIDsi2'

# List files in the specified folder
results = drive_service.files().list(
    q=f"'{folder_id}' in parents and mimeType='text/html'",
    fields="files(id, name)"
).execute()

# Initialize the Google Docs API service
docs_service = build('docs', 'v1', credentials=credentials)

# Iterate through the HTML files in the folder
for file_info in results.get('files', []):
    file_id = file_info['id']
    file_name = file_info['name']

    # Download the HTML content from Google Drive
    request = drive_service.files().get_media(fileId=file_id)
    downloaded_file = io.BytesIO()
    downloader = MediaIoBaseDownload(downloaded_file, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()

    # Convert the downloaded HTML content to a string
<<<<<<< HEAD
    html_content = downloaded_file.getvalue().decode('utf-8')
=======
    # html_content = downloaded_file.getvalue().decode('utf-8')
>>>>>>> 00a560fbf5feea7c75937daaf4ed9253f986b2b3

    

    # Create a new Google Docs document
    document = docs_service.documents().create().execute()
    doc_id = document['documentId']

    # Insert the HTML content as plain text into the new Google Docs document
    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={
            'requests': [
                {
                    'insertText': {
                        'location': {
                            'index': 1
                        },
                        'text': html_content
                    }
                }
            ]
        }
    ).execute()

    # Add writer permissions to khurramwbox@gmail.com
    drive_service.permissions().create(
        fileId=doc_id,
        body={
            'role': 'writer',
            'type': 'user',
            'emailAddress': 'khurramwbox@gmail.com'
        }
    ).execute()

    # Print the URL of the created and shared Google Docs document
    doc_url = f'https://docs.google.com/document/d/{doc_id}'
    print(f'Google Docs URL for {file_name}: {doc_url}')
