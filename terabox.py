# use some common sense !


# modules required requests,json,bs4(BeautifulSoup),cfscrape(create_scraper)

class DirectDownloadLinkException(Exception):
    """Not method found for extracting direct download link from the http link"""
    pass

def terabox1(url):
    cookies = {
        'ndus': [get cookie from browser after loging in with your google account],
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'ndus=YSOyIKxteHuis6gXbDF4znOsmAz9Q4x0RlmWLqyX',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    session = create_scraper()
    try:
        res = session.request('GET', url)
        soup = BeautifulSoup(res.text,'lxml')
        if soup.title.text == "we can’t find the page you’re looking for":
		print(Dead)
        else:  
          key = res.url.split('?surl=')[-1]
          params = {
              'app_id': '250528',
              'shorturl': f"{key}",
              'root': '1',
          }
          res = requests.get('https://www.4funbox.com/share/list', params=params, cookies=cookies, headers=headers)
          result = res.json()['list']
    except Exception as e:
	    return f"ERROR: {e.__class__.__name__}"

    if len(result) > 1:
	    f"ERROR: Can't download mutiple files"

    result = result[0]
    if result['isdir'] != '0':
        return ("ERROR: Can't download folder")
    else:
	  print(f"title: {res.json()['title'].split('/')[-1]}")
	  print(f"Link : {result['dlink']}")
        return result['dlink']



#cred @@GdtotLinkz
