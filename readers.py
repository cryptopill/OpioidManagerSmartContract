#must use python2
from ethjsonrpc import EthJsonRpc
import pprint
<<<<<<< HEAD

contractAddr = u'0x5a40cd0d658c1faf21c360fc28d1e05b3b965df1'

=======
<<<<<<< HEAD
contractAddr = u'0x1a4103ce4b02c2799e6c77b5e50c86f592ad3310'
=======
<<<<<<< HEAD
contractAddr = u'0x66f619c637074b34449a095fa0177f29828c228c'
=======
contractAddr = u'0x88f1b3a6161deb8df8d05dfe612130c738bc57f7'
>>>>>>> d534c49249aa1217add99369fd3264a49c1991f0
>>>>>>> 99e7791b9af2dfbc29eaa7baa631c65cd5bc2044
>>>>>>> f35dca715bde000ee2c70ca2a42f10989cdb5d06

c = EthJsonRpc('127.0.0.1',8545)

patient_1 = 0x5344371f4112044b1569aa27cc2dc16907ed13e2
patient_2 = 0x20de0ee3af7f1518a8ea5a70245d4d3e4b35ea18
patient_3 = 0xc8ae542b18d1b30485de68864198ea70069869ec
pharma_1 = 0x39eabe3b2546a00ff3f3f1014c73e7a3deef0030
pharma_2 = 0x030d092ab95c2557192706aa093019e9c81be0cf
pharma_3 = 0x93015b135470a3d5c5e840b2822753fde7424918

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

#NEW
def getPatientPrescriptionName(patientaddr, num):
    results = c.call(contractAddr, 'getPatientPrescriptionName(address,uint256)', [patientaddr, num], ['string'])
    return results

#NEW
def getPatientPrescriptionDOI(patientaddr, num):
    results = c.call(contractAddr, 'getPatientPrescriptionDOI(address,uint256)', [patientaddr, num], ['string'])
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

<<<<<<< HEAD

=======
<<<<<<< HEAD
"""
Patient_1 = {}
Patient_1["address"] = patient_1
Patient_1["name"] = getPatientName(patient_1)
Patient_1["num-prescriptions"] = getPrescriptionCount(patient_1)
Patient_1["medicines"] = [];


Patient_2 = {}
Patient_2["address"] = patient_2
Patient_2["name"] = getPatientName(patient_2)
Patient_2["num-prescriptions"] = getPrescriptionCount(patient_2)

Patient_3 = {}
Patient_3["address"] = patient_3
Patient_3["name"] = getPatientName(patient_3)
Patient_3["num-prescriptions"] = getPrescriptionCount(patient_3)

Patients = [Patient_1, Patient_2, Patient_3]

print Patients




=======
<<<<<<< HEAD

=======
>>>>>>> d534c49249aa1217add99369fd3264a49c1991f0
>>>>>>> 99e7791b9af2dfbc29eaa7baa631c65cd5bc2044
>>>>>>> f35dca715bde000ee2c70ca2a42f10989cdb5d06
print "name: " + str(getPatientName(patient_1))
print "number of prescriptions: " + str(getPrescriptionCount(patient_1))
print "registered?: " + str(getPatientRegistered(patient_1))
print "last prescription" + str(getPatientLatestPrescriptionHash(patient_1))
print "prescription 1 name: " + str(getPatientPrescriptionName(patient_1, 1))
print "prescription 1 doi: " + str(getPatientPrescriptionDOI(patient_1, 1))
print "prescription 1 density: " + str(getPatientPrescriptionDensity(patient_1, 1))
print "prescription 1 capsules: " + str(getPatientPrescriptionCapsules(patient_1, 1))
print'\n'

print "name: " + str(getPatientName(patient_2))
print "number of prescriptions: " + str(getPrescriptionCount(patient_2))
print "registered?: " + str(getPatientRegistered(patient_2))
print "last prescription" + str(getPatientLatestPrescriptionHash(patient_2))
print "prescription 1 name: " + str(getPatientPrescriptionName(patient_2, 1))
print "prescription 1 doi: " + str(getPatientPrescriptionDOI(patient_2, 1))
print "prescription 1 density: " + str(getPatientPrescriptionDensity(patient_2, 1))
print "prescription 1 capsules: " + str(getPatientPrescriptionCapsules(patient_2, 1))
print'\n'

print "name: " + str(getPatientName(patient_3))
print "number of prescriptions: " + str(getPrescriptionCount(patient_3))
print "registered?: " + str(getPatientRegistered(patient_3))
print "last prescription" + str(getPatientLatestPrescriptionHash(patient_3))
print "prescription 1 name: " + str(getPatientPrescriptionName(patient_3, 1))
print "prescription 1 doi: " + str(getPatientPrescriptionDOI(patient_3, 1))
print "prescription 1 density: " + str(getPatientPrescriptionDensity(patient_3, 1))
print "prescription 1 capsules: " + str(getPatientPrescriptionCapsules(patient_3, 1))
print'\n'

print "latest prescription: " + str(getLatestPrescription())
print "total prescriptions: " + str(getTotalPrescriptionCount())
"""
