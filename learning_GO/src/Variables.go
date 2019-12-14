
//variables

package main

import "fmt"

func main() {
	// variable declaration
	var number_ int
	fmt.Println("My number favorite is: ", number_)
	
	// assignment variables
	number_ = 777
	fmt.Println("My number favorite is:  ", number_)
	
	// new  var
	number_ = 1010
	fmt.Println("My new number favorite is: ", number_)
	
	// multiple varible declaration
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
}
