# Author: Ruben Dicker

from sys import argv, stderr, exit
import requests
import json
import datetime


def getNews(query):
	if not query:
		return None
	everything = True # we might wanna set this to false sometimes
	everythingOrHeadlines = 'everything' if everything else 'top-headlines'
	# options: 'popularity' 'relevancy' 'date' 'top'
	#		this is only a parameter when using a topic query
	sortby = 'top' 

	# today's date should be default I guess
	fromdate = datetime.datetime.today().strftime('%Y-%m-%d')

	# don't change this it's mine
	apiKey = '3d4dc26e4cf2447cb02ba95175aff880'
	#apiKey = '724373d22c8642549ea0b69da2087c56'
	# this is how we get the data. Simply a url that returns a json object
	url = ('https://newsapi.org/v2/everything?' + 'q=' + str(query) + '&sortBy=' + str(sortby) + '&apiKey=' + str(apiKey))
	# url = ('https://newsapi.org/v2/' + everythingOrHeadlines + '?'
	# 		'sources=' + 'google-news' + '&'
	# 	   'q=' + str(query) + '&'
	#        'from=' + str(fromdate) + '&'
	#        'sortBy=' + str(sortby) + '&'
	#        'apiKey=' + str(apiKey))

	try:
		response = requests.get(url)
		data = json.loads(response.text)
	except Exception as e:
		print('news.py: %s' % e, file=stderr) 
		exit(1)

	if data['status'] == 'error':
		print('news.py: status not ok \n', file=stderr) 
		print('status: %s \n' % data['status'], file=stderr) 
		print('code: %s \n' % data['code'], file=stderr) 
		print('message: %s' % data['message'], file=stderr) 
		exit(1)

	if data['totalResults'] == 0:
		print ('no articles found')
		return None


	article = [data['articles'][i] for i in range(len(data['articles']))]

	return article

# article = getNews('Apple')[0]

# if article is not None:
# 	# unicode is stupid and sometimes it complains if i don't encode to utf
# 	print (str(article['author'].encode('utf-8')) + '\n')
# 	print (str(article['title'].encode('utf-8')) + '\n')
# 	print (str(article['description'].encode('utf-8')) + '\n')
# 	print (str(article['url'].encode('utf-8')) + '\n')
# 	print (str(article['urlToImage'].encode('utf-8')) + '\n')
# 	print (str(article['publishedAt'].encode('utf-8')) + '\n')
# 	print (str(article['content'].encode('utf-8')) + '\n')

# ###### parameters to construct API request #######

# # show results from API-decided 'top results', or from everything 
# everything = True # we might wanna set this to false sometimes
# everythingOrHeadlines = 'everything' if everything else 'top-headlines'

# # a topic that the user might want to query for
# q = 'Trump'

# # options: 'popularity' 'relevancy' 'date'
# #		this is only a parameter when using a topic query
# sortby = 'popularity' 

# # today's date should be default I guess
# fromdate = datetime.datetime.today().strftime('%Y-%m-%d')

# # don't change this it's mine
# apiKey = '3d4dc26e4cf2447cb02ba95175aff880'		





# ###### API Request #########

# # this is how we get the data. Simply a url that returns a json object
# url = ('https://newsapi.org/v2/' + everythingOrHeadlines + '?'
# 	   'q=' + q + '&'
#        'from=' + fromdate + '&'
#        'sortBy=' + sortby + '&'
#        'apiKey=' + apiKey)

# try:
# 	response = requests.get(url)
# 	data = json.loads(response.text)
# except Exception as e:
# 	print >> stderr, 'news.py: %s' % e
# 	exit(1)

# if data['status'] == 'error':
# 	print >> stderr, 'news.py: status not ok \n'
# 	print >> stderr, 'status: %s \n' % data['status']
# 	print >> stderr, 'code: %s \n' % data['code']
# 	print >> stderr, 'message: %s' % data['message']
# 	exit(1)

# if data['totalResults'] == 0:
# 	print ('no articles found')
# 	exit(1)


# ###### JSON parsing #########

# # There will usually be many articles in the response. The [0] means
# #    I'm accessing the first article in the json array of articles. We could
# #    put this through a for loop or something if we wanted to
# article = data['articles'][0]

# if article is not None:

# 	# unicode is stupid and sometimes it complains if i don't encode to utf
# 	print (str(article['author'].encode('utf-8')) + '\n')
# 	print (str(article['title'].encode('utf-8')) + '\n')
# 	print (str(article['description'].encode('utf-8')) + '\n')
# 	print (str(article['url'].encode('utf-8')) + '\n')
# 	print (str(article['urlToImage'].encode('utf-8')) + '\n')
# 	print (str(article['publishedAt'].encode('utf-8')) + '\n')
# 	print (str(article['content'].encode('utf-8')) + '\n')


