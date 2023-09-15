import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace these with your credentials file and the folder ID where your DOCX/DOC files are stored
CREDENTIALS_FILE = 'service_account_credentials.json'
FOLDER_ID = '1YMsURSzYgp9A9bOYXwqrkW52J5XIDsi2'
EMAIL_TO_ADD_PERMISSION = 'khurramwbox@gmail.com'

# Initialize Google Drive API
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=['https://www.googleapis.com/auth/drive'])
drive_service = build('drive', 'v3', credentials=credentials)

# List all the files in the specified folder
def list_files_in_folder(folder_id):
    results = drive_service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
    files = results.get('files', [])
    return files

# Initialize Google Docs API
docs_service = build('docs', 'v1', credentials=credentials)

# Function to convert a DOCX/DOC file to Google Docs format and add permission
def convert_to_google_docs(file_id, email):
    file = drive_service.files().get(fileId=file_id).execute()
    document = {
        'title': file['name']
    }
    doc = docs_service.documents().create(body=document).execute()
    
    # Add permissions to the document for the specified email address
    drive_service.permissions().create(
        fileId=doc['documentId'],
        body={'type': 'user', 'role': 'writer', 'emailAddress': email}
    ).execute()
    
    return doc

# Main function to convert all DOCX/DOC files in the folder to Google Docs and add permission
def main():
    files = list_files_in_folder(FOLDER_ID)
    for file in files:
        if file['name'].endswith('.docx') or file['name'].endswith('.doc'):
            converted_doc = convert_to_google_docs(file['id'], EMAIL_TO_ADD_PERMISSION)
            print(f"Converted '{file['name']}' to Google Docs with ID: {converted_doc['documentId']}")

if __name__ == '__main__':
    main()

