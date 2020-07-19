
function getSum(a,b){
	a = (a != undefined) ? a : 1;
	b = (b != undefined) ? b : 41;
	console.log(a+b);
}
getSum();
getSum(2,3);
getSum(32);
getSum(null, 4);

console.log('....................');

var getSum2 = function(a=1, b=41){
	console.log(a+b);
}

getSum2();
getSum2(1,3);
getSum2(33);
getSum2(null,8);

console.log('...................');

var getNumber = new Function("number= 39", "return number;");
console.log(getNumber());
