from urllib import request

imgUrl='https://common.cnblogs.com/images/icon_weibo_24.png'
fileName=r'd:\test\test.jpg'

request.urlretrieve(imgUrl,fileName)