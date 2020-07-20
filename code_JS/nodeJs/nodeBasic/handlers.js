// manipuladores de peticion llave/valor

var exec = require("child_process").exec;


function iniciar() {
    console.log("Manipulador de peticion 'iniciar' fue llamado.");

    exec("ls -lah", function(error, stdout, stderr) {
    	response.writeHead(200, {"Content-Type":"text/html"});
    	response.write(stdout);
    	response.end();
    });
   }
 
function subir(response){
	console.log("Manipulador de peticion 'subir'  fue llamdo");
	response.writeHead(200,{"Content-Type":"text/html"});
	response.write("Hola subir");
	response.end();
}

exports.iniciar = iniciar;
exports.subir = subir;