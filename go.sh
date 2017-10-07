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

EOF

