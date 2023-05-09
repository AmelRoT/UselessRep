import wget 
import sys 
import requests
import os 

#url = 'https://www.google.com/search?q=download+photo+dummy&sxsrf=ALiCzsZLy8eZnhWZqgYbrnKEOCJLJt15nw:1670236850170&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiOl5SRpeL7AhVwSPEDHTWVDXwQ_AUoAXoECAEQAw&biw=2048&bih=1170&dpr=1.25#imgrc=mDsDDNXlAmNNsM'
#wget.download(url, '/Users/Amel/Downloads/withPython1.jpg')
url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
r = requests.get(url, allow_redirects=True)
#print(r.headers.get('content-type'))
print("---------------#-----------------")





remote_url = 'https://www.google.com/robots.txt'
# Define the local filename to save data
local_file ='/Users/Amel/Desktop/filee.txt.txt'
local_file1 = '/Users/Amel/Downloads'
# Make http request for remote file data
data = requests.get(remote_url)
# Save file data to local copy
with open(local_file,'wb') as f:
   f.write(data.content)



#r = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
#data1 = requests.get(r)
#local_file1 = os.path.join('/Users/Amel/Downloads',os.path.basename(r)); 
#with open(local_file1,'wb') as f:
#  f.write(data1.content)



r = 'https://mail.google.com/mail/u/0/#inbox/FMfcgzGrbRPlkmKtJpQNkdHRJsKhnsGZ?projector=1&messagePartId=0.1'
data1 = requests.get(r)
local_file1 = os.path.join('/Users/Amel/Downloads','file2.pdf'); 
with open(local_file1,'wb') as f:
   f.write(data1.content)


url = 'https://storage.googleapis.com/static.configserverfirewall.com/images/windows10/windows-clear.webp'
wget.download(url, '/Users/Amel/Downloads/withPython333.jpg')


