let x = 1
let sum = 1
let factorial = function(a){
	while (x <= a){
		sum = x * sum;
		x += 1;
	}
	console.log(a, "factorial is", sum);
}
const a = parseInt(prompt('Enter a number: '));
factorial(a);