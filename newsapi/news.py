# Author: Ruben Dicker

from sys import argv, stderr, exit
import requests
import json
import datetime


###### parameters to construct API request #######

# show results from API-decided 'top results', or from everything 
everything = True # we might wanna set this to false sometimes
everythingOrHeadlines = 'everything' if everything else 'top-headlines'

# a topic that the user might want to query for
q = 'Apple'

# options: 'popularity' 'relevancy' 'date'
#		this is only a parameter when using a topic query
sortby = 'popularity' 

# today's date should be default I guess
fromdate = datetime.datetime.today().strftime('%Y-%m-%d')

# don't change this it's mine
apiKey = '3d4dc26e4cf2447cb02ba95175aff880'





###### API Request #########

# this is how we get the data. Simply a url that returns a json object
url = ('https://newsapi.org/v2/' + everythingOrHeadlines + '?'
	   'q=' + q + '&'
       'from=' + fromdate + '&'
       'sortBy=' + sortby + '&'
       'apiKey=' + apiKey)

try:
	response = requests.get(url)
	data = json.loads(response.text)
except Exception as e:
	print >> stderr, 'news.py: %s' % e
	exit(1)

if data['status'] == 'error':
	print >> stderr, 'news.py: status not ok \n'
	print >> stderr, 'status: %s \n' % data['status']
	print >> stderr, 'code: %s \n' % data['code']
	print >> stderr, 'message: %s' % data['message']
	exit(1)

if data['totalResults'] == 0:
	print 'no articles found'
	exit(1)


###### JSON parsing #########

# There will usually be many articles in the response. The [0] means
#    I'm accessing the first article in the json array of articles. We could
#    put this through a for loop or something if we wanted to
article = data['articles'][0]

if article is not None:

	# unicode is stupid and sometimes it complains if i don't encode to utf
	print article['author'].encode('utf-8') + '\n'
	print article['title'].encode('utf-8') + '\n'
	print article['description'].encode('utf-8') + '\n'
	print article['url'].encode('utf-8') + '\n'
	print article['urlToImage'].encode('utf-8') + '\n'
	print article['publishedAt'].encode('utf-8') + '\n'
	print article['content'].encode('utf-8') + '\n'


