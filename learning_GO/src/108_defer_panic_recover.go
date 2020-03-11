package main 
import "fmt"

func first() {
	fmt.Println("1er")
}

func second(){
	fmt.Println("2do")
}

func main() {
	// ___defer___
	defer second()
	first()

	//____panic_recover___
	panic("PANIC")
	str := recover()
	fmt.Println(str)

	//____defer___
	defer func(){
		str := recover()
		fmt.Println(str)
	}()
	panic("PANIC")
}