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

contractAddr = u'0x9ff504e9f773c57cd7cf602752bd8bbb83b77c6f'

c = EthJsonRpc('127.0.0.1',8545)

patient_1 = 0xb872047bb1763414f63f577590ed75565f368ddd
patient_2 = 0x30aeca74198075c69dd8e54bad929d9eb6725536
patient_3 = 0xf348a8ba3475edd24531c077320559645c1fb019
pharma_1 = 0xb791bd701dcc9ca36658f978adc9dd1a8fc1b133
pharma_2 = 0xae7f58377b9a1f81b41b6efcf25099c6678be3a9
pharma_3 = 0xc1af3283bddd6b8685e404bb5b6efadeeacd1d25

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

def getPatientPrescriptionName(patientaddr, num):
    results = c.call(contractAddr, 'getPatientPrescriptionName(address,uint256)', [patientaddr, num], ['string'])
    return results

def getPatientPrescriptionDOI(patientaddr, num):
    results = c.call(contractAddr, 'getPatientPrescriptionDOI(address,uint256)', [patientaddr, num], ['string'])
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
    Patients =  [{'address' : str(patient_1),
                'name': str(getPatientName(patient_1)),
                'num_prescriptions': str(getPrescriptionCount(patient_1)),
                'medicines': [
                        {
                        'name': str(getPatientPrescriptionName(patient_1,1)),
                        'patientAddress': str(patient_1),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_1,1)),
                        'density': str(getPatientPrescriptionDensity(patient_1,1)),
                        'doi': str(getPatientPrescriptionDOI(patient_1,1)),

                        },
                        {
                        'name': "Opioid",
                        'patientAddress': str(patient_1),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_1,1)),
                        'density': str(getPatientPrescriptionDensity(patient_1,1))
                        }
                            ]
                },
                {'address' : str(patient_2),
                'name': str(getPatientName(patient_2)),
                'num_prescriptions': str(getPrescriptionCount(patient_2)),
                'medicines': [
                        {
                        'name': str(getPatientPrescriptionName(patient_2,1)),
                        'patientAddress': str(patient_2),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_2,1)),
                        'density': str(getPatientPrescriptionDensity(patient_2,1)),
                        'doi': str(getPatientPrescriptionDOI(patient_2,1)),

                        },
                        {
                        'name': "Opioid",
                        'patientAddress': str(patient_2),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_2,1)),
                        'density': str(getPatientPrescriptionDensity(patient_2,1))
                        }
                        ]
                },
                {'address' : str(patient_3),
                'name': str(getPatientName(patient_3)),
                'num_prescriptions': str(getPrescriptionCount(patient_3)),
                'medicines': [
                        {
                        'name': str(getPatientPrescriptionName(patient_3,1)),
                        'patientAddress': str(patient_3),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_3,1)),
                        'density': str(getPatientPrescriptionDensity(patient_3,1)),
                        'doi': str(getPatientPrescriptionDOI(patient_3,1)),

                        },
                        {
                        'name': "Opioid",
                        'patientAddress': str(patient_3),
                        'medAddress': repr(getLatestPrescription()),
                        'capsules': str(getPatientPrescriptionCapsules(patient_3,1)),
                        'density': str(getPatientPrescriptionDensity(patient_3,1))
                        }
                        ]
                }
                ]
# print(Patients);
# json_data = json.dumps(Patients);
# print(json_data);
        # Patient2 =  {}
# data = []
    sio.emit('patientlists', Patients)

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
