
import requests
import json

controller='https://sandboxapic.cisco.com/'


class Network: 
    template_name = "networkdevices.html"

    def getTicket(self):
        url = "https://" + controller + "/api/v1/ticket"
        payload = {username:" " , password: " "}
        header = {"content-type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
        r_json = response.json()
        ticket = r_json["response"]["serviceTicket"]
        return ticket


    def getNetworkcount(self,ticket):
        url = "https://" + controller + "/api/v1/network-device"
        header = {"content-type": "application/json", "X-Auth-Token": ticket}
        response = requests.get(url, headers=header, verify=False)
        r_json = response.json() 
        print("The counts of network devices is :")
        print(len(r_json('response')))
        
        for item in r_json('response'):
            print("the ip address of this host is %s " % item,'hostIp')
            print("the mac address of this host is %s " % item,'hostMac')
            

a = Network()
ticket = a.getTicket()
a.gethost(ticket)
a.getNetworkcount(ticket)

