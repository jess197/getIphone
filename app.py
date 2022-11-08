import requests, time

def getApple():

    uri = "https://www.apple.com/shop/pickup-message-recommendations?mts.0=regular&cppart=UNLOCKED/US&location=Orlando,%20FL&product=MQ1D3LL/A"

    # sending get request and saving the response as response object
    r = requests.get(url = uri)
    
    # extracting data in json format
    data = r.json()

    for store in data["body"]["PickupMessage"]["stores"]:
        if store["partsAvailability"]:
             if store["storeName"] in ("Florida Mall","Millenia","Altamonte"):
                  for model in store["partsAvailability"]:
                    print(f'{store["storeName"]} - {store["storeDistanceWithUnit"]} - {store["partsAvailability"][model]["messageTypes"]["regular"]["storePickupProductTitle"]}')
                    print("==================================================")
while 1==1:
    getApple()
    time.sleep(30) 