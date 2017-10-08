import socketio
import eventlet
import eventlet.wsgi
from sympy import *
import numpy as np
import random
from json import JSONEncoder
import json
from flask import Flask, render_template
from ethjsonrpc import EthJsonRpc

contractAddr = u'0x8ba7313949d56480dca42d9058066bcd76646c0b'

c = EthJsonRpc('127.0.0.1',8545)

patient_1 = 0x3a4657f075c19812ab943f91429c6c6a6efafe88
patient_2 = 0xe3938d687831473386eb046fc6c194f7288c74ab
patient_3 = 0x4ad9974ae37ebf733fda2a9e3b994c354581f520

def createPrescription(name, doi, capsules, density, patientaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'createPrescription(string,string,uint8,uint8,address)', [name,doi,capsules,density,patientaddr], gas=1000000)
    print tx

def distributePrescription(prescriptionaddr, patientaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'distributePrescription(bytes32,address)', [prescriptionaddr,patientaddr], gas=1000000)
    print tx

sio = socketio.Server()
app = Flask(__name__)

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)


# @sio.on('clientQ', namespace='/')
# def connect(sid, environ):
#     print(sid)
#     print(environ)
    # sio.emit('reply', generateDerivativeQuestion())

@sio.on('createPre', namespace='/')
def connect(sid, environ):
    hex_str = environ["patientAddress"]
    hex_int =  int(hex_str, 16)
    new_int = hex_int + 0x200
    print(hex(new_int))

    createPrescription(environ["name"], environ["doi"], environ["capsules"], environ["density"], new_int)
    # temp = generateDerivativeQuestion()
    # print(temp)
    # sio.emit('reply', "temp")

@sio.on('registerPre', namespace='/')
def connect(sid, environ):

    # print('here')
    # temp1 = generateIntegralQuestion()
    # print(temp1)
    sio.emit('reply2', "temp1")
#
@sio.on('questions3', namespace='/')
def connect(sid, environ):
    # print('here')
    # temp2 = generateAlgebraQuestion()
    # print(temp2)
    sio.emit('reply3', "temp2")

    # print("connect ", sid)
    # print("environ ", environ);
    # print environ[0]

# @sio.on('chat message', namespace='/chat')
# def message(sid, data):
#     print("message ", data)
#     sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
