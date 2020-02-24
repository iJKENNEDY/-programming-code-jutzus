package main

import "fmt"

func main() {

	//____arrays_____
	fmt.Println("____arrays_____")
	fmt.Println("_______________")

	var x[4] float64
	x[0] = 233
	x[1] = 432
	x[2] = 444
	x[3] = 909

	fmt.Println()
	fmt.Println("values of x :",x)

	var total float64 = 0
	for i := 0; i < len(x); i++ {
		total += x[i]
	}

	fmt.Println("result1 = ",float64(total))

	fmt.Println("...............")
	var total2 float64 = 0
	 
	for _, value := range x {
		total2 += value
	}

	fmt.Println("foreach-total: ", total2)

	var y2 = [3]float64{23,44,55}
	fmt.Println(y2)
	fmt.Println("... print value y2....")
	for _, value := range y2{
		fmt.Println(value)
	}

	fmt.Println()
	//______ Slices______
	fmt.Println("....._____slices_____......")
	fmt.Println("---------------------------")

	/*
	var x3[]float64

	x3 := make([] float64, 5)
	a := make([] float64, 5, 10)

	arr:= [5]float64{11,22,33,44,55}
	x3 := arr[0:5]
	fmt.Println(x3)
	*/
	slice1 := []int{2,4,5}
	slice2 := append(slice1, 6,7)
	fmt.Println(slice1, slice2)

	fmt.Println()

	//______ Maps ______
	fmt.Println("....._____Maps_____......")
	fmt.Println("---------------------------")

	xxx := make(map [string] int)
	xxx["key"] = 20
	fmt.Println(xxx["key"])

	yyy:= make(map [int] int)
	yyy[12] = 2019
	fmt.Println(yyy[12])

	fmt.Println()
	langCode := make(map[string] string)
	langCode["A"]= "Ada"
	langCode["B"] = "Bat"
	langCode["C"] = "C"
	langCode["D"] = "Delphi"
	langCode["E"] = "Erlang"

	fmt.Println(langCode["D"])

	name, ok := langCode["E"]
	fmt.Println(name, ok)

	coding:= map[string] string{
		"J": "Java",
		"K": "Kotlin",
		"M": "Markdown",
	}
	fmt.Println(coding["K"])

	code := map[string]map[string] string{
		"R":map[string]string{
			"name":"Rust",
			"paradign":"Functional",
		},
		"D":map[string]string{
			"name":"Dart",
			"paradign":"multiprograming",
		},
	}

	if el, ok:= code["R"]; ok{
		fmt.Println("name:: ",el["name"],"paradign:: ",el["paradign"])
	}
}