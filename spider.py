import urllib.request


def getHtml(url):
    myHead = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"}
    myRequest = urllib.request.Request(url, data=None, headers=myHead)
    page = urllib.request.urlopen(myRequest)

    html = page.read()
    return html


myUrl = "http://www.lifanacg.com"
myHtml = getHtml(myUrl)
print(myHtml)
