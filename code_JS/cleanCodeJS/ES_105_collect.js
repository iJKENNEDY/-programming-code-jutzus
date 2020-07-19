
var showCollections = function (id, ...collection){
	console.log(collection instanceof Array);
};

showCollections(12, 'python','go','rust');

var showCollections2 = function(id, ...collection){
	console.log(collection);
};

showCollections2(33, 'adf','qwerty');

