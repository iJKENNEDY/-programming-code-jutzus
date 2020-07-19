var http = require("http");
/*
http.createServer(function(request, response){
    response.writeHead(200, {"Content-Type":"text/html"});
    response.write("enigma-hello");
    response.end();
}).listen(8888);
*/

//forma 22
/*
function onRequest(request, response) {
    response.writeHead(200,{"Content-Type": "text/html"});
    response.write("enigma-goel");
    response.end();
}

http.createServer(onRequest).listen(9999);
*/
var url = require("url");

function iniciar(route, handle){

function onRequest(request, response){
    var pathname = url.parse(request.url).pathname;
    console.log("peticion para "+ pathname+ " recibida");
    route(handle,pathname);
    response.writeHead(200, {"content-type":"text/html"});
    response.write("hola enigma");
    response.end();
}
    
http.createServer(onRequest).listen(8888);
console.log("servidor iniciado.");
}

exports.iniciar = iniciar

