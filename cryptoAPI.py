import http.client
import requests

class CryptoAPI:
    
    def __init__(self):
        self.Connect  

    def Connect():
        conn = http.client.HTTPSConnection("investing-cryptocurrency-markets.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
            'X-RapidAPI-Host': "investing-cryptocurrency-markets.p.rapidapi.com"
            }

        conn.request("GET", "/get-meta-data?locale_info=en_US&lang_ID=1&time_utc_offset=28800", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
    

    def GetDESO():
        url = "https://investing-cryptocurrency-markets.p.rapidapi.com/coins/search"

        querystring = {"string":"bit","time_utc_offset":"28800","lang_ID":"1"}

        headers = {
	        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	        "X-RapidAPI-Host": "investing-cryptocurrency-markets.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)


    def GetChart():
        url = "https://investing-cryptocurrency-markets.p.rapidapi.com/coins/get-brief-chart"

        querystring = {"pair_ID":"33","lang_ID":"1","time_utc_offset":"28800","range":"p"}

        headers = {
	        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	        "X-RapidAPI-Host": "investing-cryptocurrency-markets.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)