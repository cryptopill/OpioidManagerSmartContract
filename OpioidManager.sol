pragma solidity ^0.4.2;

contract OpioidManager{

  //structure of an opioid prescription
  struct MedicinePrescription{
    string name;
    string doi;
    uint8 capsules;
    uint8 density;
    address patient;
    bool distributed;
  }

  //presecriptions sill be mapped to addresses
  uint256 public prescription_count = 0;
  mapping (uint256 => bytes32) public prescription_hashes;
  mapping (bytes32 => MedicinePrescription) public prescriptions;

  //should only be callable by the physician
  //DOESN'T ADD TO PATIENT MAPPING
  //WORKS
  function createPrescription(string _name, string _doi, uint8 _capsules, uint8 _density, address _patient){
    prescription_count ++;
    bytes32 _prescription_hash = keccak256(now, _doi, _name, _patient,_capsules,_density);

    prescriptions[_prescription_hash] = MedicinePrescription({name: _name, doi: _doi, capsules: _capsules, density: _density, patient: _patient, distributed: false});

    prescription_hashes[prescription_count] = _prescription_hash;
  }

  //WORKS
  function getLatestPrescription() constant returns (bytes32){
    return prescription_hashes[prescription_count];
  }

  //WORKS
  function getTotalPrescriptionCount() constant returns (uint256){
    return prescription_count;
  }

  //only callable by pharmacists
  function distributePrescription(bytes32 _prescription_addr, address _patient){
    //return true and add the prescription to the patients received prescriptions
    if(prescriptions[_prescription_addr].patient == _patient){
      prescriptions[_prescription_addr].distributed = true;
      patients[_patient].prescription_count++;
      patients[_patient].prescriptions[patients[_patient].prescription_count] = _prescription_addr;
    }
  }

  //get functions for scanning status of the prescription callable by everyone?
  function getCapsules(bytes32 _prescription_addr) constant returns (uint8){
    return prescriptions[_prescription_addr].capsules;
  }

  function getDensity(bytes32 _prescription_addr) constant returns (uint8){
    return prescriptions[_prescription_addr].density;
  }

  function getPatient(bytes32 _prescription_addr) constant returns (address){
    return prescriptions[_prescription_addr].patient;
  }

  function getDistributed(bytes32 _prescription_addr) constant returns (bool){
    return prescriptions[_prescription_addr].distributed;
  }

  struct Patient{
    string name;
    bool registered;
    uint256 prescription_count;
    //maps index to prescription hashes
    mapping(uint256 => bytes32) prescriptions;
  }

  mapping(address => Patient) public patients;

  function registerPatient(address _patientAddress, string _name){
    patients[_patientAddress] = Patient({name: _name, registered: true, prescription_count: 0});
  }

  //WORKS
  function getPatientName(address _address) constant returns(string){
    return patients[_address].name;
  }

  //WORKS
  function getPatientRegistered(address _address) constant returns(bool){
    return patients[_address].registered;
  }

  //Works
  function getPrescriptionCount(address _address) constant returns(uint256){
    return patients[_address].prescription_count;
  }

  //Works
  function getPatientPrescriptionCapsules(address _address, uint256 _num) constant returns(uint8){
    return getCapsules(patients[_address].prescriptions[_num]);
  }

  //Works
  function getPatientPrescriptionDensity(address _address, uint256 _num) constant returns(uint8){
    return getDensity(patients[_address].prescriptions[_num]);
  }

  //Works
  function getPatientLatestPrescriptionHash(address _address) constant returns (bytes32){
    return patients[_address].prescriptions[patients[_address].prescription_count];
  }

}
