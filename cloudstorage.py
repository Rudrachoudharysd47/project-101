import dropbox
"""
access_token = "sl.BGPoJDEsVfFAsgnWzOlsiboCWoH-b7VZY8NOI_SqAKPxWbmxiHu6AZL10WqgqcwXt4eUf_zdgvvkeJ3-Dr5asfiAJGZH2Bk1PX-wo_BtKv8eUzA54HZSVVxKxtPnDKzApU83yi4"
file_from = 'car.py' #local file path
file_to = '/rudrapratapchoudhary/index/car.py'     # dropbox path
def upload_file(file_from,file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from,'rb')
    dbx.files_upload(f.read(),file_to)
upload_file(file_from,file_to)
"""
class Transferdata:
    def __init__(self,access_token):
         self.access_token  = access_token
    def uploadfiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token = "sl.BGPoJDEsVfFAsgnWzOlsiboCWoH-b7VZY8NOI_SqAKPxWbmxiHu6AZL10WqgqcwXt4eUf_zdgvvkeJ3-Dr5asfiAJGZH2Bk1PX-wo_BtKv8eUzA54HZSVVxKxtPnDKzApU83yi4"
    transferdata = Transferdata(access_token)
    file_from = input("enter the filepath or name to transfer")
    file_to = input("enter the dropbox path to transfer")
    transferdata.uploadfiles(file_from,file_to)
    print("file as being both")
main()
