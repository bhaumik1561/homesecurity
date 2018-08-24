import json
import urllib

from pip._vendor import requests

datas = {'data':{'body':'hii','title':'hello','message':'hhj'},'to':'/topics/noti'}
url='https://fcm.googleapis.com/fcm/send'
headerk={'Content-Type':'application/json','Authorization':'key=AAAAHrwNmUA:APA91bEBJ78FXFZTqZCJHRmXChjQNsfevbBNrqSkngwT--0MQ0NQ-krfqqKwWkoQza2I13Bdz95-nlafAToL9TTIVUIyIbBltTZgwQaSdW3Bpd_JIp-XCPrpvK7yiGZpFahr1hhb9zGC'}
#req = urllib.Request("https://fcm.googleapis.com/fcm/send")
#req.add_header('Content-Type', 'application/json')
#req.add_header('Authorization', 'key=AAAAHrwNmUA:APA91bEBJ78FXFZTqZCJHRmXChjQNsfevbBNrqSkngwT--0MQ0NQ-krfqqKwWkoQza2I13Bdz95-nlafAToL9TTIVUIyIbBltTZgwQaSdW3Bpd_JIp-XCPrpvK7yiGZpFahr1hhb9zGC')

#response = urllib.urlopen(req, json.dumps(data))
#print(response)
#datam = urllib.parse.urlencode(datas).encode("utf-8")
#req = urllib.request.Request(url,headers=header)
#urllib.request.urlopen(req,json.dumps(datam))
#print(response)


#batch = [{"body":"hii","title":"hello"}]
#batch_dumped = json.dumps(batch)
#token = {"to":"/topics/noti", "data": batch_dumped}
r = requests.post(url, data=json.dumps(datas),headers=headerk)

print (r.text)
