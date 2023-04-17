# importing the requests library 
import requests 
  
# Proxies api-endpoint 
URL = "http://api.proxiesapi.com"
  
# insert your auth key here
auth_key = "128657a01b7523fffa14df84ee9bb964_sr98766_ooPq87"
url = "http://www.reddit.com/r/programming/"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'auth_key':auth_key, 'url':url} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

with open("request.txt", "w+") as f:
	f.write(str(r.content))
