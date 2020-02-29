package main
import "fmt"
/*
func average(xs []float) float64{
	panic("Not implemented")
}
*/
func average222(xs[] float64) float64{
	total:= 0.0
	for _, v:= range xs{
		total += v
	}
	return total/float64(len(xs))
}

var x int= 23
func ff(){
	fmt.Println(x)
}

func f2()(r int){
	r = 1
	return
}

//returning multiple values
func f3 (int, int){
	return 5, 3
}

func main()  {
	someOfName := []float64{98,43,52,99,12,34,52,4}
	fmt.Println(average222(someOfName))
	ff()
	fmt.Println(f2())
	x,y := f3() 
}