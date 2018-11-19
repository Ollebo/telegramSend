import requests

def sendToTelegram(message,level="info"):
	'''
	Send Message to group
	'''


	if level == "info":
		'''
		Stadard info
		'''

		botid=''
		groupid=''
		r = requests.get("https://api.telegram.org/{0}/sendMessage?chat_id={1}&text={2}".format(botid,groupid,message))

	else:
		botid=''
		groupid=''
		r = requests.get('https://api.github.com/events')

def sendImageTelegram():
	'''
	Send a local image to group
	'''



	botid=''
	groupid=''

	url = "https://api.telegram.org/{0}/sendPhoto".format(botid);
	files = {'photo': open('bild.jpg', 'rb')}
	data = {'chat_id' : groupid}
	r= requests.post(url, files=files, data=data)
	print(r.status_code, r.reason, r.content)

