#must use python2
from ethjsonrpc import EthJsonRpc
import pprint

contractAddr = u'0x9ff504e9f773c57cd7cf602752bd8bbb83b77c6f'


c = EthJsonRpc('127.0.0.1',8545)

patient_1 = 0xb872047bb1763414f63f577590ed75565f368ddd
patient_2 = 0x30aeca74198075c69dd8e54bad929d9eb6725536
patient_3 = 0xf348a8ba3475edd24531c077320559645c1fb019
pharma_1 = 0xb791bd701dcc9ca36658f978adc9dd1a8fc1b133
pharma_2 = 0xae7f58377b9a1f81b41b6efcf25099c6678be3a9
pharma_3 = 0xc1af3283bddd6b8685e404bb5b6efadeeacd1d25

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
