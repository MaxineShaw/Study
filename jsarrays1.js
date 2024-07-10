const sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let x = 0;
let i = 0
while (i < sample.length) {
	x += sample[i];
	i += 1;
}
console.log(`The sum is ${x}.`);