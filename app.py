from flask import Flask, request, make_response, jsonify,Response

import json
import pandas as pd

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/',methods=['POST','GET'])
def index():
    return 'Hello,This is the home page nothing to see here....'



# create a route for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
   
    req_data = request.get_json()
    scenename = req_data['scene']['name']
    ssid = req_data['session']['id']
    nextscene = req_data['scene']['next']['name']
    rollno = req_data['session']['params']['chosenRollno']
    divans = req_data['session']['params']['chosenDivision']
    rollansdivans = 'Rollno:' + rollno + '\nDiv:' + divans
    msg = 'Your attendance is'
    if divans=="A":
       df=pd.read_csv("data/A.csv")
        
    if divans=="B":
       df=pd.read_csv("data/B.csv")
        
    data=df.loc[df["roll_no"]==int(rollno)]




    
      

    a = {'session':{
            'id':ssid,
            'params':{}
        },
        'prompt':{
        'override':False,
        "content": {
        "table": {
          "button": {},
          "columns": [
            {
              "header": "Subject"
            },
            {
              "header": "Present"
            }
            
          ],
          "image": {
            "alt": "SITS logo",
            "height": 0,
            "url": "https://images.shiksha.com/mediadata/images/1571057918phpCdqLqc.png",
            "width": 0
          },
          "rows": [
            {
              "cells": [
                {
                  "text": "TOC"
                },
                {
                  "text": str(data["310241 TOC"].values[0])
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "DBMS"
                },
                {
                  "text": str(data["310242 DBMS"].values[0])
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "CN"
                },
                {
                  "text": str(data["310245 CN"].values[0])
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "SEPM"
                },
                {
                  "text":str(data["310243 SEPM"].values[0])
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "ISEE"
                },
                {
                  "text": str(data["310244 ISEE"].values[0])
                }
              ]
            }
          ],
          "subtitle": str(data["Theory Attendance %"].values[0]),
          "title": str(data["Name "].values[0])
        }
      },

        'firstSimple':{
        'speech':msg,
        'text':msg
        }
        },
        'scene':{
        'name':scenename,
        'slots':{},
        'next':{
        'name':nextscene
        }
        }
        }
    ptoj = json.dumps(a)
    return ptoj
    
# run the app
if __name__ == '__main__':
   app.run(debug=True)




