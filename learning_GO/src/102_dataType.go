package main 
import "fmt"

//Numbers::
/*=> Integers:::> uint8, uint16,uint32,uint64
			 :::> int8, int16, int32, int64
  => Floating:::> float32, float64
  			 :::> complex64, complex128

  #> operating::> (+,-,*,/,%)
  #> String  :::> string, "", ''
  #> Booleans:::> && => and
  				  || => or
  				  !  => not
  				  true 
  				  false
  # Constants :::> const
*/

 func main() {
 	//Booleans
 	fmt.Println(true && true)

 	var numInt8 int8 = 123 
	fmt.Println("Int8:: ",numInt8)

	var cadena = "coding-go"
	fmt.Println("cadena:: ", cadena)

 	//multiple variable declaration
 	var  numWidth, numHeight int = 100, 50
	fmt.Println("width is", numWidth, "height is", numHeight)
	
 	//date  others
	var(
		id int
		name = "Enigmaq"
		age = 33
		height  = 177
	 )
	
	fmt.Println("id", id, " my name is", name,",age is", age,"and height is", height, "cm")

	// short hand declaration
	name101, age := "Qwerty", 45
	fmt.Println("My name is", name101, "age is", age)

	// const 
	const xconst string = "go..."
	fmt.Println(xconst)

	// definition multiple variables
	var(
		a = 43
		b = 54
		c = 99
	)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)

	//--------input-----------
	fmt.Println("...................")
	var input float64
	fmt.Println("ingrese un numero:: ")
	fmt.Scanf("%f", &input)
	output := input * 2
	fmt.Println("::> ",input, "* 2"," = ", output)
 	
 }