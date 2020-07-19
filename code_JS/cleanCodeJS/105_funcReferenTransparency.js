
//..bad
function withoutReferentialTransparency(){
	let counter = 1;

	function increaseCounter(value){
		counter = value + 1;
	}

	increaseCounter(counter);
	console.log(counter);
}

// better
function withReferentialTransparency(){
	let counter = 1;

	function increaseCounter(value){
		return value + 1;
	}

	console.log(increaseCounter(counter));
	console.log(counter);
}

withoutReferentialTransparency();
withReferentialTransparency();
