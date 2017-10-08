#must use python2
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

def distributePrescription(prescriptionaddr, patientaddr, pharmaaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'distributePrescription(bytes32,address)', [prescriptionaddr,patientaddr], gas=1000000)
    print tx


# createPrescription('One Punch Man','20/12/2017',45,23,patient_3)
distributePrescription('\xbb\xee\xa1;^\xaa\xafb\tS\xbf\xe5\xd1\xc5g\xb9\xb8(,$\x86\x0b\x8a\xc2\x05\x164\t\xedE$"',patient_3,pharma_2)
