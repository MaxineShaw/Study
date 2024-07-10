let big = 0
let x = function (a, b , c, d, e){
	if (big < a) {
		big = a;
	}
	if (big < b) {
		big = b;
	}
	if (big < c) {
		big = c;
	}
	if (big < d) {
		big = d;
	}
	if (big < e) {
		big = e;
	}
	return console.log(big)
}
