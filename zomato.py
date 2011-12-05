import httplib, urllib, urllib2

class Zomato:
	'''
	Constructor for the Zomato class.

	Parameters:
		key										- Zomato API Key.
														Get it from http://www.zomato.com/api/key
		base_url (optional)		- base URL to be used for making API calls.
														Defaults to https://api.zomato.com/v1/
	'''
	def __init__(self, key, base_url='https://api.zomato.com/v1/'):
		self.key = key
		self.base_url = base_url

	'''
	Function to make API call.

	Parameters:
		call									- API call to be made
		method (optional)			- method to be used for making the HTTP request.
														Defaults to GET.
		params (optional)			- parameters to be sent with the request
		headers	(optional)		- extra headers to be sent with the request

	Example:
		To get a List of Cuisines, you will make the following call:
			https://api.zomato.com/v1/cuisines.json
			Parameter to be sent is city_id with value (say) 1
			Method for making the HTTP request is GET.

		See documentation on Zomato.com to get List of Cuisines:
			http://www.zomato.com/api/documentation#Get-list-of-cuisines

		In the above call,
			https://api.zomato.com/v1/ is the base URL,
			cuisines.json is the call parameter,
			city_id is a parameter with the value 1.

		For the above API call, we will use the request() in the following
		way:

			z = Zomato()
			z.request('cuisines.json', params={'city_id': 1})

		We don't have to send any extra headers for this call. The default
		method used for making the HTTP request is GET so we
		don't have to set that as well.
	'''
	def request(self, call, method='GET', params={}, headers={}):
		url = '%s%s' % (self.base_url, call)

		if method == 'GET':
			url = url + '?' + urllib.urlencode(params)
			req = urllib2.Request(url)
		else:
			req = urllib2.Request(url, urllib.urlencode(params))

		req.add_header('X-Zomato-API-Key', self.key)
		for header, value in headers.iteritems():
			req.add_header(header, value)

		r = urllib2.urlopen(req)
		return r.read()
