 package main
 import "fmt"

 func main(){
 	var x[5] int
 	x[2] = 342
 	x[4] = 949
 	fmt.Println(x)
 	fmt.Println()

 	var y[3] float64
 	y[0] = 23
 	y[1] = 44
 	y[2] = 92

 	var total float64 = 0
 	for i := 0; i < 3; i++ {
 		total += y[i]
 	}
 	fmt.Println("Promedio = ",total/3)
 	fmt.Println()

 	//length-> len(y)
 	var total2 float64 = 0
 	for _,value:=range y {
 		total2 += value
 	}
 	fmt.Println("promd2 = ",total2/float64(len(y)))
 	fmt.Println()

 	//creando arrays
 	//x := [3] float64 {32,55,90}

 }