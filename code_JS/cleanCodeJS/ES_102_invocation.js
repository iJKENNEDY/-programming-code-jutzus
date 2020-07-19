
function Employee(name, department, salary){
	this.name = name;
	this.department = department;
	this.salary = salary;

	console.log("welcome "+ this.name +"!!!");

	this.getInfo = function(){
		return ()=>{
			console.log(this.name+" from "+ this.department + " earns "+ this.salary);
		};
	}
}

let jin = new Employee('Jin','sales', 4893);
let kenn = new Employee('Kenned','Finance',9999);
let printInfo = kenn.getInfo();
printInfo()

