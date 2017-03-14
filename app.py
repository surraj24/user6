#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") == "user.id":
        result = req.get("result")
        parameters = result.get("parameters")
        id1 = parameters.get("user-id")
        pass1 = parameters.get("password")
        cost = {'Suraj':100, 'Shubham':200, 'Raju':300, 'Yash':400, 'Ravi':500}
        if(str(cost[id1])==pass1):
            speech = id1 + ". You are Suceesfully login. How can I help you."
        else:
            speech = "Incorrect password."
        print("Response:")
        print(speech)

        return {
            "speech": speech,
            "displayText": speech,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-onlinestore-shipping"
        }
    if req.get("result").get("action") == "user.id2":
        speech = "Right."
        print("Response:")
        print(speech)
        return {
            "speech": speech,
            "displayText": speech,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-onlinestore-shipping"
        }
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
