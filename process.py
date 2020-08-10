import ftplib
import pandas as pd
import os
from conf import Config

c = Config()
# FTP server credentials
FTP_HOST = c.get_property('host')
FTP_USER = c.get_property('user')
FTP_PASS = c.get_property('password')

class FTPFunction:
    file_list=[]
    _pwd = os.getcwd()
    def uploadFile(self,filename): 
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        upload_path = "/ftp/output/"
        ftp.cwd(upload_path)
        print(str(self._pwd)+'/'+filename)
        try:
            with open(filename, "rb") as file:
                ftp.storbinary(f"STOR {filename}", file)
            print('success in uploading')
        except:
            print("Error in uploading")        
        ftp.quit()

    def downloadFile(self,filename):
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        download_path = "/ftp/input/"        
        try:
            ftp.cwd(download_path)
            with open(filename, "wb") as file_handle:
                ftp.retrbinary(f"RETR {filename}", file_handle.write)
            print('success')            
        except:
            print("Error in uploading")
        ftp.quit()
        
    def file_split(self,filename):
        try:            
            df=pd.read_csv(str(self._pwd)+'/'+str(filename))
            file1=df.pivot(index='SystemId',columns='Field', values='Value')
            no_col= file1.shape[0]
            for i in range(no_col):
                split_row = file1.iloc[[i]]
                _filename = str(split_row.reset_index()['SystemId'][0])
                split_row.to_csv(_filename+'.csv',index=False)
                self.file_list.append(_filename+'.csv')
            print('Saving success..')
        except:
            print('Error in splitting')