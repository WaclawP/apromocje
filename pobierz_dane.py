
import requests
import json
import datetime
import pandas as pd

def api_call(raf_cookie):
    y = datetime.date.today()
    x = datetime.datetime.now()
    time = x.strftime("%d_%b_%H%M")
    url = "https://edge.allegro.pl/sale/offers"

    def make_QXLSESSID(cookie):
        key = cookie.replace("/", "%2F")
        return f"QXLSESSID={key}"
    
    key = make_QXLSESSID(raf_cookie)

    querystring = {"publication.marketplace":"allegro-pl","country.code":"PL","limit":"1000","publication.status":"ACTIVE","sellingMode.format":"BUY_NOW","sort":"-soldAmount","offset":"0"}

    payload = ""
    headers = {
        "cookie": key,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0",
        "Accept": "application/vnd.allegro.web.v2+json",
        "Accept-Language": "pl-PL",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://allegro.pl/",
        "x-representative-of": "101994159",
        "Origin": "https://allegro.pl",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }

    data = [1]
    while data[-1]: 
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        data.append(response.json()['offers'])

        #zwiększeni offset czyli przejście na następną stronę
        offset = int(querystring["offset"])
        offset += 1000
        offset = str(offset)
        querystring["offset"] = offset
    try:
        data = data[1:-1]
    except:
        data = data[1:]




    # In[2]:


    data_export = {}
    data_export_list = []

    for pagedata in data:
        for offer in pagedata:
            a = {}
            a['id'] = offer['id']
            a['visitsCount'] = offer['stats']['visitsCount']
            a['sold'] = offer['stock']['sold']
            a['updatedAt'] = offer['updatedAt']
            a['last30days_from'] = y    
            #a['watchersCount'] = offer['stats']['watchersCount']
            
            data_export_list.append(a)
            data_export[offer['id']] = a     
    with open(r"D:\DocumentsFiles\Biznes ALE-ADSY\Allegro Teraz\AUTO_SHOP24\Nowe kampanie 14.05.2024\data.txt", "w") as file:
        file.write(str(data_export_list))


    # In[3]:



    # In[7]:


    print(data_export_list[2])


    # In[10]:


    df = pd.DataFrame(data_export_list)
    df.head()

    return df


