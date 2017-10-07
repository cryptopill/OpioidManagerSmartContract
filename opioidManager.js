var opioidOutput={"contracts":{"OpioidManager.sol:OpioidManager":{"abi":"[{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"address\"}],\"name\":\"patients\",\"outputs\":[{\"name\":\"name\",\"type\":\"string\"},{\"name\":\"registered\",\"type\":\"bool\"},{\"name\":\"prescription_count\",\"type\":\"uint256\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_prescription_addr\",\"type\":\"bytes32\"}],\"name\":\"getDensity\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_address\",\"type\":\"address\"}],\"name\":\"getName\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_address\",\"type\":\"address\"}],\"name\":\"getRegistered\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_address\",\"type\":\"address\"},{\"name\":\"_num\",\"type\":\"uint256\"}],\"name\":\"getPatientPrescriptionCapsules\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_prescription_addr\",\"type\":\"bytes32\"}],\"name\":\"getPatient\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"_capsules\",\"type\":\"uint8\"},{\"name\":\"_density\",\"type\":\"uint8\"},{\"name\":\"_patient\",\"type\":\"address\"}],\"name\":\"createPrescription\",\"outputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"prescriptions\",\"outputs\":[{\"name\":\"capsules\",\"type\":\"uint8\"},{\"name\":\"density\",\"type\":\"uint8\"},{\"name\":\"patient\",\"type\":\"address\"},{\"name\":\"distributed\",\"type\":\"bool\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"_patientAddress\",\"type\":\"address\"},{\"name\":\"_name\",\"type\":\"string\"}],\"name\":\"registerPatient\",\"outputs\":[],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_prescription_addr\",\"type\":\"bytes32\"}],\"name\":\"getCapsules\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"_prescription_addr\",\"type\":\"bytes32\"},{\"name\":\"_patient\",\"type\":\"address\"}],\"name\":\"distributePrescription\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_address\",\"type\":\"address\"}],\"name\":\"getPrescriptionCount\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_address\",\"type\":\"address\"},{\"name\":\"_num\",\"type\":\"uint256\"}],\"name\":\"getPatientPrescriptionDensity\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"_prescription_addr\",\"type\":\"bytes32\"}],\"name\":\"getDistributed\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"type\":\"function\"}]","bin":"6060604052341561000f57600080fd5b5b610a5c8061001f6000396000f300606060405236156100cd5763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416630869cfbc81146100d257806333abd5531461018a5780635fd4b08a146101b65780636bfa4e791461024d57806371beed1f146102805780637899a34e146102b85780637b2cda17146102ea5780637b464e93146103275780638048c2f014610375578063868d02ad146103d6578063af6f2b3b14610402578063d3c9acc114610438578063da3d6aa614610469578063f259f844146104a1575b600080fd5b34156100dd57600080fd5b6100f1600160a060020a03600435166104cb565b604051821515602082015260408101829052606080825284546002600019610100600184161502019091160490820181905281906080820190869080156101795780601f1061014e57610100808354040283529160200191610179565b820191906000526020600020905b81548152906001019060200180831161015c57829003601f168201915b505094505050505060405180910390f35b341561019557600080fd5b6101a06004356104ee565b60405160ff909116815260200160405180910390f35b34156101c157600080fd5b6101d5600160a060020a036004351661050b565b60405160208082528190810183818151815260200191508051906020019080838360005b838110156102125780820151818401525b6020016101f9565b50505050905090810190601f16801561023f5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561025857600080fd5b61026c600160a060020a03600435166105dc565b604051901515815260200160405180910390f35b341561028b57600080fd5b6101a0600160a060020a0360043516602435610602565b60405160ff909116815260200160405180910390f35b34156102c357600080fd5b6102ce60043561063b565b604051600160a060020a03909116815260200160405180910390f35b34156102f557600080fd5b61031560ff60043581169060243516600160a060020a036044351661065f565b60405190815260200160405180910390f35b341561033257600080fd5b61033d6004356107ab565b60405160ff9485168152929093166020830152600160a060020a03166040808301919091529115156060820152608001905180910390f35b341561038057600080fd5b6103d460048035600160a060020a03169060446024803590810190830135806020601f820181900481020160405190810160405281815292919060208401838380828437509496506107e395505050505050565b005b34156103e157600080fd5b6101a0600435610853565b60405160ff909116815260200160405180910390f35b341561040d57600080fd5b61026c600435600160a060020a036024351661086b565b604051901515815260200160405180910390f35b341561044357600080fd5b610315600160a060020a0360043516610904565b60405190815260200160405180910390f35b341561047457600080fd5b6101a0600160a060020a0360043516602435610926565b60405160ff909116815260200160405180910390f35b34156104ac57600080fd5b61026c60043561095f565b604051901515815260200160405180910390f35b600160208190526000918252604090912090810154600282015460ff9091169083565b600081815260208190526040902054610100900460ff165b919050565b61051361097e565b6001600083600160a060020a0316600160a060020a031681526020019081526020016000206000018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156105cf5780601f106105a4576101008083540402835291602001916105cf565b820191906000526020600020905b8154815290600101906020018083116105b257829003601f168201915b505050505090505b919050565b600160a060020a0381166000908152600160208190526040909120015460ff165b919050565b600160a060020a038216600090815260016020908152604080832084845260030190915281205461063290610853565b90505b92915050565b600081815260208190526040902054620100009004600160a060020a03165b919050565b60008042838686604051938452600160a060020a03929092166c0100000000000000000000000002602084015260ff9081167f010000000000000000000000000000000000000000000000000000000000000090810260348501529116026035820152603601604051809103902090506080604051908101604090815260ff80881683528616602080840191909152600160a060020a0386168284015260006060840181905284815290819052208151815460ff191660ff919091161781556020820151815460ff919091166101000261ff001990911617815560408201518154600160a060020a0391909116620100000275ffffffffffffffffffffffffffffffffffffffff0000199091161781556060820151815490151560b060020a0276ff0000000000000000000000000000000000000000000019909116179055509050805b509392505050565b60006020819052908152604090205460ff808216916101008104821691600160a060020a03620100008304169160b060020a90041684565b60606040519081016040908152828252600160208084018290526000838501819052600160a060020a038716815291905220815181908051610829929160200190610990565b50602082015160018201805460ff19169115159190911790556040820151600290910155505b5050565b60008181526020819052604090205460ff165b919050565b600082815260208190526040812054600160a060020a03838116620100009092041614156108fa5750600082815260208181526040808320805476ff00000000000000000000000000000000000000000000191660b060020a179055600160a060020a038416835260018083528184206002810180548301908190558552600301909252909120839055610635565b5060005b92915050565b600160a060020a0381166000908152600160205260409020600201545b919050565b600160a060020a0382166000908152600160209081526040808320848452600301909152812054610632906104ee565b90505b92915050565b60008181526020819052604090205460b060020a900460ff165b919050565b60206040519081016040526000815290565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106109d157805160ff19168380011785556109fe565b828001600101855582156109fe579182015b828111156109fe5782518255916020019190600101906109e3565b5b50610a0b929150610a0f565b5090565b610a2d91905b80821115610a0b5760008155600101610a15565b5090565b905600a165627a7a72305820b6676e308a643f3aeebc8c41e80bf686237c9821aa579e2608b9cb6f42ec550d0029"}},"version":"0.4.14+commit.c2215d46.Linux.g++"}