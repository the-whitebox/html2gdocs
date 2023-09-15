from googleapiclient.discovery import build
from google.oauth2 import service_account

# Your service account credentials JSON file
credentials_file = 'service_account_credentials.json'

# HTML content with rich formatting
html_content = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
</body>
</html>
"""

# Authenticate with the Google Docs API using a service account
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=['https://www.googleapis.com/auth/documents']
)

# Create a Google Docs API client
docs_service = build('docs', 'v1', credentials=credentials)

# Create a new Google Docs document
document = docs_service.documents().create().execute()
document_id = document['documentId']

# Insert the HTML content into the document
requests = [
    {
        'insertText': {
            'location': {
                'index': 1,  # Adjust the index where you want to insert
            },
            'text': html_content,
        },
    },
]
docs_service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()

drive_service.permissions().create(
    fileId=doc_id,
    body={
        'role': 'writer',
        'type': 'user',
        'emailAddress': 'khurramwbox@gmail.com'
    }
).execute()

# Print the URL of the Google Docs document
print("Google Docs URL:", f'https://docs.google.com/document/d/{document_id}/edit')
