-- mongoDB
>mongod --version
--ejecutar 
>mongo
--muestra la base de datos
>show dbs
--consulta en que base de datos estoy
>db
-- para usar la base de datos
> use mydatabase
--para crear un usuario
>db.createUser({
	user: 'Mendax',
	pwd: 'qwerty',
	roles: ['readWrite','dbAdmin']
})

--___dividir colecciones
--db.collection.insertOne()	===>Inserts a single document into a collection.
--db.collection.insertMany()===>db.collection.insertMany() inserts multiple documents into a collection.
--db.collection.insert()===>db.collection.insert() inserts a single document or multiple documents into a collection.
--Additional Methods for Inserts
--The following methods can also add new documents to a collection:

--db.collection.update() when used with the upsert: true option.
--db.collection.updateOne() when used with the upsert: true option.
--db.collection.updateMany() when used with the upsert: true option.
--db.collection.findAndModify() when used with the upsert: true option.
--db.collection.findOneAndUpdate() when used with the upsert: true option.
--db.collection.findOneAndReplace() when used with the upsert: true option.
--db.collection.save().
--db.collection.bulkWrite().

>db.clientes.insert({firstName: 'Lara',
	lastName: 'Martinez'
});
-- insertar varias colecciones:
db.inventory.insertMany([
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);

-- find():: muestra los datos de la colecion
>db.clientes.find()
-- insertando multiples datos
>db.clientes.insert([
	{firstName: 'Paolo', lastName: 'Guerrero'},
	{firsName: 'Lucia', lastName: 'Wollm'},
	{firstName: 'Remi', lastName: 'Reguiardo'}
]);
-- resultado de los datos
-- especificamos solo aquellos que coinciden
>db.clientes.find({firstName: 'Paolo'});

-- cuando se escribe un error en la insercion
-- error al escribir firsName(sin t)
>db.clientes.update(
	{firsName: 'Lucia'},-- escribe como estaba el erro
	{
		firstName: 'Marta',
		lastName: 'Delgado',
		age : '34' --un dato mas
	}
);
--
-- muestra un formato mas ordenado
>db.clientes.find().pretty()

-- actualizando por su ID si los nombres son iguales
--buscaamos por su id
db.clientes.find({_id: objectId("fsdaf435kh3k45h3sd"})
-- actualizamos
db.clientes.update(
	{_id: objectId("fsdaf435kh3k45h3sd")},
	{ firstName: 'Remi',
	lastName : 'Delgado',
	gender : 'male'
	 }
	);

--para agregar datos
>db.clientes.update(
	{_id: objectId("fsdaf435kh3k45h3sd")},
	{ 
	$set : {age: 43}
	}
	);
-- se equivoca en edad supone 48
-- incrementamos $inc 
>db.clientes.update(
	{_id: objectId("fsdaf435kh3k45h3sd")},
	{ 
	$inc : {age: 5}
	}
	);

-- quita datos
db.clientes.update(
	{_id: objectId("fsdaf435kh3k45h3sd")},
	{ 
	$unset : {age: 1}-- 1 == true
	}
	);

--actualizando datos
>db.clientes.update({firstName: 'Lucho'},{firstName:'Lucho',
	lastName: "Orosco"}, {upset:true});

-- renombrar:::
>db.clientes.update(
	{firstName: "Lucho"},
	{
	$rename: {"firstName": "primerNombre"}
	}
);

-- eliminar un dato
db.clientes.remove(
	{primerNombre: "Lucho"}
)

-- cuando se elimina algunos datos coinciden
-- utiliza el id
--cas0 1::

>db.clientes.remove(
	{firstName: 'Remi'},
	{justOne: true}
);

-- buscando por varias formas
>db.clientes.find({$or:[{firstName: 'Lucho'}, {firstName: "Remi"}]})

>db.clientes.find(
	{gender: 'male'}
);

-- insertando datos
>db.clientes.insert(
	[
		{name: "Boris", age: 43},
		{name: "Danny", age: 27},
		{name: "Rosangela", age: 19}
	]
	);

--buscando con condiciones mayores que 30
>db.clientes.find({age: {$gt: 30}})

--buscando con condiciones menores que 30
>db.clientes.find({age: {$lt: 30}})

--buscando con condiciones men-may entre
>db.clientes.find({age: {$gt: 30, $lt: 50}})


-- accediendo a sub datos:::
--insert
>db.clientes.insert({firstName: 'Remi'},
	addres: {city: 'London'}
	);

db.clientes.find({"addres.city": "London"})

--- buscando con expresiones regulares
db.clientes.find({name: {$regex: 'jandro'}})

--ordenando datos
db.clientes.find().sort({lastName: 1})--desc(1).. asc(-1)

-- numero de datos
 db.clientes.count()

--encadenado datos-- mayores a 18 cuantos lo tienen
db.clientes.find({age: {$gt: 18}}).count()


-- numero de datos
db.clientes.find().limit(4)

--agregando mas meetodos
db.clientes.find().limit(4).sort({name: -1})

--usando js
db.clientes.find().forEach(function(doc){ print(doc.name)})
