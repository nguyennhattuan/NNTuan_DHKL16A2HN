// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MessageContract {
    string private message;
    
    event MessageUpdated(string newMessage);
    
    constructor() {
        message = "Hello World";
    }
    
    function setMessage(string memory newMessage) public {
        message = newMessage;
        emit MessageUpdated(newMessage);
    }
    
    function getMessage() public view returns (string memory) {
        return message;
    }
} 