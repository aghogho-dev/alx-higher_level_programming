#!/usr/bin/node
const oldDict = require('./101-data').dict;
let newDict =  {};
for (let key in oldDict) {
	if (newDict[oldDict[key]] === undefined) {
		newDict[oldDict[key]] = [key];
	} else {
		newDict[oldDict[key]].push(key);
	}
}
console.log(newDict);
