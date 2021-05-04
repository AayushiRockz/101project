import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from , file_to):
        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = '******'
    transferData = TransferData(access_token)

    file_from= 'sampletext1.txt'
    file_to = '/test_dropbox/sampletext1.txt'

    transferData.uploadFiles(file_from,file_to)
