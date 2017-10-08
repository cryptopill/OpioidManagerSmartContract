#must use python2
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

def distributePrescription(prescriptionaddr, patientaddr, pharmaaddr):
    tx = c.call_with_transaction(c.eth_coinbase(), contractAddr, 'distributePrescription(bytes32,address)', [prescriptionaddr,patientaddr], gas=1000000)
    print tx

# createPrescription('Literally Methfiafsd','20/12/2017',30,16,patient_3)
distributePrescription('\xfeSsi\xfb\xcb\xbf\x9a\x0c\xa4\xe5\x1c\xfbQM\x94\xb1\x94R\x90\xa7V);G\xf1^\x03\xa9\xc4\xfeQ',patient_3,pharma_2)
