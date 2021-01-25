from flask import Flask
from flask import jsonify
from flask import request
import json
import datetime
from flask import render_template
import socket
from flask_cors import CORS
import sys, getopt
import time

import controller.pypostgresController as pgf

pypostgresControl = pgf.pypostgresController()
app = Flask(__name__)
CORS(app)

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)

@app.route('/', methods=['GET'])
def homeroot():
    return jsonify({"status":"CONNECTED"})



def main(argv):
    ipaddr = IPAddr
    portnum = 20023
    try:
        opts, args = getopt.getopt(argv,"l:p:",["ipchange=","portchange="])
        for opt, arg in opts:
            if opt in ("-l", "--ipchange"):
                ipaddr = arg
            elif opt in ("-p", "--portchange"):
                portnum = arg

        app.run(debug=True, host=ipaddr, port=portnum)
    except Exception as e:
        print(e)
        app.run(debug=True, host=IPAddr, port=20023)


        
