const sample = [20, 30, 25, 35, -16, 60, -100];
let x = 0;
let i = 0; 
let n = sample.length;
console.log(0)
while (i < n) {
	let y = sample[i];
	x += y;
	i +=1;
	console.log(x);
}
x /= n;
console.log('The average is', x, '.');