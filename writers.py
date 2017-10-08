#must use python2
from ethjsonrpc import EthJsonRpc
<<<<<<< HEAD
contractAddr = u'0x1a4103ce4b02c2799e6c77b5e50c86f592ad3310'
=======

contractAddr = u'0x88f1b3a6161deb8df8d05dfe612130c738bc57f7'
>>>>>>> 99e7791b9af2dfbc29eaa7baa631c65cd5bc2044

c = EthJsonRpc('127.0.0.1',8545)

patient_1 = 0x3a4657f075c19812ab943f91429c6c6a6efafe88
patient_2 = 0xe3938d687831473386eb046fc6c194f7288c74ab
patient_3 = 0x4ad9974ae37ebf733fda2a9e3b994c354581f520
pharma_1 = 0xa190c7ca6d8f875aec1ae27e452ebfbf8c44e254
pharma_2 = 0x15eef446813c1a2b96d56e80143835cfe1f67b54
pharma_3 = 0x92569be733b0b5a94e43dace73c6c1adfe4f956d

def createPrescription(name, doi, capsules, density, patientaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'createPrescription(string,string,uint8,uint8,address)', [name,doi,capsules,density,patientaddr], gas=1000000)
    print tx

def distributePrescription(prescriptionaddr, patientaddr, pharmaaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'distributePrescription(bytes32,address)', [prescriptionaddr,patientaddr], gas=1000000)
    print tx

#createPrescription('Adreal','20/12/2017',35,12,patient_1)
#distributePrescription('4*?\xe2\xfe\xfeJ-\x92\tp\xd4R\xc4\x12>\xddL\xacan\xd2\x93Xk\xef,\x1cL\xdaRA',patient_1,pharma_2)
