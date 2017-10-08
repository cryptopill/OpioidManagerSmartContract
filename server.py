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

contractAddr = u'0x5a40cd0d658c1faf21c360fc28d1e05b3b965df1'

c = EthJsonRpc('127.0.0.1',8545)

patient_1 = 0x5344371f4112044b1569aa27cc2dc16907ed13e2
patient_2 = 0x20de0ee3af7f1518a8ea5a70245d4d3e4b35ea18
patient_3 = 0xc8ae542b18d1b30485de68864198ea70069869ec
pharma_1 = 0x39eabe3b2546a00ff3f3f1014c73e7a3deef0030
pharma_2 = 0x030d092ab95c2557192706aa093019e9c81be0cf
pharma_3 = 0x93015b135470a3d5c5e840b2822753fde7424918

def createPrescription(name, doi, capsules, density, patientaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'createPrescription(string,string,uint8,uint8,address)', [name,doi,capsules,density,patientaddr], gas=1000000)
    print tx

def distributePrescription(prescriptionaddr, patientaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'distributePrescription(bytes32,address)', [prescriptionaddr,patientaddr], gas=1000000)
    print tx

def bytes32tostring(results):
    s = pprint.pformat(results)

    chars = ['\\', 'x', '(', ')', '[', ']', '\'', ';', ',']

    for c in chars:
        s = s.replace(c, '')

    return '0x'+s


def getPatientName(patientaddr):
    results = c.call(contractAddr, 'getPatientName(address)', [patientaddr], ['string'])
    return results

def getPrescriptionCount(patientaddr):
    results = c.call(contractAddr, 'getPrescriptionCount(address)', [patientaddr], ['uint256'])
    return results


def getPatientPrescriptionCapsules(patientaddr, num):
    results = c.call(contractAddr, 'getPatientPrescriptionCapsules(address,uint256)', [patientaddr, num], ['uint8'])
    return results

def getPatientPrescriptionDensity(patientaddr, num):
    results = c.call(contractAddr, 'getPatientPrescriptionDensity(address,uint256)', [patientaddr, num], ['uint8'])
    return results

def getLatestPrescription():
    results = c.call(contractAddr, 'getLatestPrescription()', [], ['bytes32'])
    return results

def getTotalPrescriptionCount():
    results = c.call(contractAddr, 'getTotalPrescriptionCount()', [], ['uint256'])
    return results

def getPatientRegistered(patientaddr):
    results = c.call(contractAddr, 'getPatientRegistered(address)', [patientaddr], ['bool'])
    return results

def getPatientLatestPrescriptionHash(patientaddr):
    results = c.call(contractAddr, 'getPatientLatestPrescriptionHash(address)', [patientaddr], ['bytes32'])
    return results

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
@sio.on('getAllUsers', namespace='/')
def connect(sid, environ):
    # print('here')
    # temp2 = generateAlgebraQuestion()
    # print(temp2)
    print('get req');
    Patient1 = {'address' : str(patient_1),
                'name': str(getPatientName(patient_1)),
                'num_prescriptions': str(getPrescriptionCount(patient_1)),
                'medicines': [
                        {
                        'name': "Opioid",
                        'patientAddress': str(patient_1),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_1,1)),
                        'density': str(getPatientPrescriptionDensity(patient_1,1))
                        },
                        {
                        'name': "Opioid",
                        'patientAddress': str(patient_1),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_1,1)),
                        'density': str(getPatientPrescriptionDensity(patient_1,1))
                        }
                            ]
                }
    print(Patient1);
    json_data = json.dumps(Patient1);
    print(json_data);
        # Patient2 =  {}
    data = []
    sio.emit('', "temp2")

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
