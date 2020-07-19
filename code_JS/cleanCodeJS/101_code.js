var variable = 32;
{
	console.log('inside', variable);
	var variable = 32;
}
console.log('outside', variable);
variable = variable * 2;
console.log('changed', variable);
