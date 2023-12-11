#!/usr/bin/node
function factorial (x) {
	if (isNaN(x)) {
		return 1;
	}
	else {
		let result = 1;
		for (let i = 1; i === x; i++) {
			result *= i;
		}
		return result;
}

console.log(factorial(Number(process.argv[2])));
