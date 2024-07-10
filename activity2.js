const a = Number(window.prompt("Type a number", ""));
const b = Number(window.prompt("Type a second number", ""));
const c = Number(window.prompt("Type a third number", ""));
if (a < b < c) {
	alert("Increasing order");
	} else if ( a > b > c) {
		alert("Decreasing order");
	} else { alert( "Neither increasing or decreasing order");
	}