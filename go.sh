#!/bin/bash

#SHOULD BE RUNNING TESTRPC IN BACKGROUND

echo "var opioidOutput=`solc --optimize --combined-json abi,bin,interface OpioidManager.sol`" > opioidManager.js

geth attach rpc:http://127.0.0.1:8545 << EOF


loadScript('opioidManager.js')     //load the abi and bytecode

var opioidContractAbi = opioidOutput.contracts['OpioidManager.sol:OpioidManager'].abi     //get just the abi

var opioidContract = eth.contract(JSON.parse(opioidContractAbi))


var opioidCode = "0x" + opioidOutput.contracts['OpioidManager.sol:OpioidManager'].bin

var deployOpioidContract = {from: eth.accounts[0], data: opioidCode, gas: 1000000}

var opioidInstance = opioidContract.new(deployOpioidContract)

eth.getTransactionReceipt(opioidInstance.transactionHash)

var opioidAddress = eth.getTransactionReceipt(opioidInstance.transactionHash).contractAddress

opioidAddress

//now register 3 patients accounts 1,2,3


var opioidManagerContract = eth.contract(JSON.parse(opioidContractAbi))

var opioidManager = opioidManagerContract.at(opioidAddress)

opioidManager.registerPatient.sendTransaction(eth.accounts[1], "Carlo Supina",{from: eth.accounts[0], gas: 1000000})

opioidManager.registerPatient.sendTransaction(eth.accounts[2], "Nathaniel Young",{from: eth.accounts[0], gas: 1000000})

opioidManager.registerPatient.sendTransaction(eth.accounts[3], "AungKaung Myat",{from: eth.accounts[0], gas: 1000000})

opioidManager.getPatientName.call(eth.accounts[1])

EOF

