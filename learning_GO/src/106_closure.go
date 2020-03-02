package main
import "fmt"

func main(){
	add := func(x, y int) int {
		return x +y
	}

	resta := func(x, y int) int {
		return x - y
	}

	product := func(a, b int) int {
		return a * b
	}

	divv := func(m, n int) int {
		return m /n 
	}

	fmt.Println("add: ",add(1,1))
	fmt.Println("resta = ",resta(33,9))
	fmt.Println("product = ",product(123,43))
	fmt.Println("div: ",divv(12,6))
	//closure
	nextEven := makeEvenGenerator()
	fmt.Println(nextEven())
	fmt.Println(nextEven())
}

func makeEvenGenerator() func uint{
	i := uint(0)

	return func() (ret uint){
		ret = i
		i+=2
	}
	return
}