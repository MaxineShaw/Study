let n = 2
let y = 0
let z = 0
let prime = function(a){
	if(a < 0){ 
	console.log(a, "is not a prime number");
	} 
	while (n != a){
		if (a % n == 0){
			console.log(a, "is not a prime number");
			n = a;
			z = 1;
		}
		n += 1;
	} 
	if (z == 0) {
		console.log(a, "is a prime number!");
	}
}
const a = parseInt(prompt('Enter a number: '));
prime(a);