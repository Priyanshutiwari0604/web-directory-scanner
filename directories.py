import requests

target_url = input('[*] Enter Target URL: ')
file_name = input('[*] Enter Name of the File Containing Directories: ')

def request(url):
    try:
        return requests.get("http://"+ url)
    except requests.exceptions.ConnectionError:
    	    pass

file=open(file_name,'r')
for line in file:
        directory = line.strip()
        full_url=target_url + '/' + directory
        response=request(full_url)
        if response:
        	print('[*] Discovered Directory AT This Path : ' + full_url)

