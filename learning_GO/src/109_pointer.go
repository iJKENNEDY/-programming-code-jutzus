package main 
import "fmt"

func zero( x int){
	x = 0
}

func zero_pointer(xPtr *int){
	*xPtr = 0
}

func main() {
	x := 5
	zero(x)
	fmt.Println("no Pointer:: ",x)
	zero_pointer(&x)
	fmt.Println("Con Pointer:: ",x)
}