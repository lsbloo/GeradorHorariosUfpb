import os

# Configuration SERVER PORT
SERVER_PORT = os.environ.get('SERVER_PORT', 'DONT FOUND SERVER.PORT')
SERVER_HOST = os.environ.get('SERVER_HOST', 'DONT FOUND SERVER.HOST')


# CONFIGURATION PATH ARCHIVES JSON 
SERVER_DIRECTORY_SAVE = os.environ.get('SERVER_DIRECTORY_SAVE', 'DONT FOUND SERVER DIRECTORY PATH SAVE JSON OBJECTS INPUT')