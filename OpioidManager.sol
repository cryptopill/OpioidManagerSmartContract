pragma solidity ^0.4.2;

contract OpioidManager{

  //structure of an opioid prescription
  struct OpioidPrescription{
    uint8 capsules;
    uint8 density;
    address patient;
    bool distributed;
  }
  //presecriptions sill be mapped to addresses
  mapping (bytes32 => OpioidPrescription) public prescriptions;

  //should only be callable by the physician
  //DOESN'T ADD TO PATIENT MAPPING
  function createPrescription(uint8 _capsules, uint8 _density, address _patient) returns (bytes32){
    bytes32 prescription_addr = keccak256(now,_patient,_capsules,_density);
    prescriptions[prescription_addr] = OpioidPrescription({capsules: _capsules, density: _density, patient: _patient, distributed: false});
    return prescription_addr;
  }

  //only callable by pharmacists
  function distributePrescription(bytes32 _prescription_addr, address _patient) returns (bool){
    //return true and add the prescription to the patients received prescriptions
    if(prescriptions[_prescription_addr].patient == _patient){
      prescriptions[_prescription_addr].distributed = true;
      patients[_patient].prescription_count ++;
      patients[_patient].patient_prescriptions[patients[_patient].prescription_count] = _prescription_addr;
      return true;
    }

    return false;     //return false if the patient's address and the prescription do not match up
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
    mapping(uint256 => bytes32) patient_prescriptions;
  }

  mapping(address => Patient) public patients;

  function registerPatient(address _patientAddress, string _name){
    patients[_patientAddress] = Patient({name: _name, registered: true, prescription_count: 0});
  }

  function getName(address _address) constant returns(string){
    return patients[_address].name;
  }

  function getRegistered(address _address) constant returns(bool){
    return patients[_address].registered;
  }

  function getPrescriptionCount(address _address) constant returns(uint256){
    return patients[_address].prescription_count;
  }

  function getPatientPrescriptionCapsules(address _address, uint256 _num) constant returns(uint8){
    return getCapsules(patients[_address].patient_prescriptions[_num]);
  }

  function getPatientPrescriptionDensity(address _address, uint256 _num) constant returns(uint8){
    return getDensity(patients[_address].patient_prescriptions[_num]);
  }

}
