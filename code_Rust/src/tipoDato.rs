
main(){
	println!(".... TIPO DE DATOS .....");
	println!("........................");
	
	let lenguajeCode_string = "Rust_code";
	let years_int = 2019;
	let pi_float = 3.1415;
	let isBool = true;
	let icono_char = '♣♣♣';
	
	println!("lenguaje favorito {} :-)",lenguajeCode_string);
	println!("visto el {}", years_int);
	println!("valor de pi {}", pi_float);
	println!("todo es {}", isBool);
	println!("suerte {}", icono_char);
	
	//entero
	let result = 10;    // i32 by default
   let age:u32 = 20;
   let sum:i32 = 5-15;
   let mark:isize = 10;
   let count:usize = 30;
   println!("result value is {}",result);
   println!("sum is {} and age is {}",sum,age);
   println!("mark is {} and count is {}",mark,count);
   
   // flotantes
   let result = 10.00;        //f64 by default
   let interest:f32 = 8.35;
   let cost:f64 = 15000.600;  //double precision
   
   println!("result value is {}",result);
   println!("interest is {}",interest);
   println!("cost is {}",cost);
   
   //separador de numeros
   let float_with_separator = 11_000.555_001;
   println!("float value {}",float_with_separator);
   
   let int_with_separator = 50_000;
   println!("int value {}",int_with_separator);
   
   //boolenos
   let isfun:bool = true;
   println!("Is Rust Programming Fun ? {}",isfun);
   
   //caracteres
   let special_character = '@'; //default
   let alphabet:char = 'A';
   let emoji:char = '☻';
   
   println!("special character is {}",special_character);
   println!("alphabet is {}",alphabet);
   println!("emoji is {}",emoji);
}