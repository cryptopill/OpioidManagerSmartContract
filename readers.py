#must use python2
from ethjsonrpc import EthJsonRpc
import pprint
contractAddr = u'0x88f1b3a6161deb8df8d05dfe612130c738bc57f7'

c = EthJsonRpc('127.0.0.1',8545)

patient_1 = 0x3a4657f075c19812ab943f91429c6c6a6efafe88
patient_2 = 0xe3938d687831473386eb046fc6c194f7288c74ab
patient_3 = 0x4ad9974ae37ebf733fda2a9e3b994c354581f520
pharma_1 = 0xa190c7ca6d8f875aec1ae27e452ebfbf8c44e254
pharma_2 = 0x15eef446813c1a2b96d56e80143835cfe1f67b54
pharma_3 = 0x92569be733b0b5a94e43dace73c6c1adfe4f956d

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

print "name: " + str(getPatientName(patient_1))
print "number of prescriptions: " + str(getPrescriptionCount(patient_1))
print "registered?: " + str(getPatientRegistered(patient_1))
print "last prescription" + str(getPatientLatestPrescriptionHash(patient_1))
print "prescription 1 density: " + str(getPatientPrescriptionDensity(patient_1, 1))
print "prescription 1 capsules: " + str(getPatientPrescriptionCapsules(patient_1, 1))
print'\n'

print "name: " + str(getPatientName(patient_2))
print "number of prescriptions: " + str(getPrescriptionCount(patient_2))
print "registered?: " + str(getPatientRegistered(patient_2))
print "last prescription" + str(getPatientLatestPrescriptionHash(patient_2))
print "prescription 1 density: " + str(getPatientPrescriptionDensity(patient_2, 1))
print "prescription 1 capsules: " + str(getPatientPrescriptionCapsules(patient_2, 1))
print'\n'

print "name: " + str(getPatientName(patient_3))
print "number of prescriptions: " + str(getPrescriptionCount(patient_3))
print "registered?: " + str(getPatientRegistered(patient_3))
print "last prescription" + str(getPatientLatestPrescriptionHash(patient_3))
print "prescription 1 density: " + str(getPatientPrescriptionDensity(patient_3, 1))
print "prescription 1 capsules: " + str(getPatientPrescriptionCapsules(patient_3, 1))
print'\n'

print "latest prescription: " + str(getLatestPrescription())
print "total prescriptions: " + str(getTotalPrescriptionCount())
