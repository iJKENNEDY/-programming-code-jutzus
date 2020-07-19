
var details = {
	number: 43,
	operation: function() {
		return ()=> console.log(this.number);
	}
};

var details2 = {
	number: 95
};

details.operation().bind(details2)();

//... bind...call...apply
var product= (x,y)=> x*y;

console.log(product.call(null, 2,4));
console.log(product.apply(null, [2,4]));

var multiply =product.bind(null, 2,3);
console.log(multiply());
