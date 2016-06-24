import sys
import requests
import json
import pprint

def main():
    myheaders={'content-type':'application/json'}
    payload={
    "ins_api": {
    "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "sh int br",
        "output_format": "json"
        }
    }
    response = requests.post('http://172.31.216.26/ins',data=json.dumps(payload), headers=myheaders,auth=('admin','Insieme123')).json()
        pprint.pprint(response)
    
        
if __name__ == '__main__':
    main()