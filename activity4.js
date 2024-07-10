const i = parseInt(prompt('Enter a number: '));
let n = 1;
	console.log('you have input the number', i);
while (n <=10){
	let x = i * n;
	console.log(i, 'x', n, '=', x)
	n++;
}