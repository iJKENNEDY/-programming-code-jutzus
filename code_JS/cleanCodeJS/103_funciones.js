
const orders = [
	{productTitle: "Product 1", amount: 10},
	{ProductTitle: "Product 2", amount: 30},
	{ProductTitle: "Product 3", amount: 39},
	{ProductTitle: "Product 4", amount: 89}
];

const utilesEscritorio = [
	{productTitle: "Cuaderno atlas", amount: 190},
	{ProductTitle: "Lapicero  vmd", amount: 390},
	{ProductTitle: "reglas collection", amount: 939},
	{ProductTitle: "plumones", amount: 989}
];

function imperative(){
	let totalAmount = 0;

	for (let i=0; i < orders.length; i++){
		totalAmount += orders[i].amount;
	}
	console.log(totalAmount);
}

//..function->declarative
function sumTotalDeclarative () {
	function sum101(currentAmount, utilesc){
		return  currentAmount + utilesc.amount;
	}

	function getTotalAm (utilesEscritorio) {
		return utilesEscritorio.reduce(sum101,0);
	}
	console.log(getTotalAm(utilesEscritorio));
}

function declarative(){
	function sumAmount(currentAmount, order){
		return currentAmount + order.amount;
	}

	function getTotalAmount(orders){
		return orders.reduce(sumAmount, 0);
	}
	console.log(getTotalAmount(orders));
}

imperative();
declarative();
sumTotalDeclarative();