package main
import "fmt"

func main() {
	fmt.Println()
	fmt.Println("____if____")
	for i := 0; i < 9; i++ {
		if i % 2 == 0 {
			fmt.Println(i, "000")
		}else{
			fmt.Println(i, "111")
		}
	}

	fmt.Println()

	// 1)..for..
	fmt.Println("____FOR____")
	i := 1
	for i <= 10{
		fmt.Println(i)
		i = i + 1
	}

	fmt.Println()

	//.............
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	fmt.Println()

	//---switch----
	
	fmt.Println("____switch____")
	fmt.Println()

	var q int = 3
	switch q {
		case 0: fmt.Println("aaa")
		case 1: fmt.Println("bbb")
		case 3: fmt.Println("ccc")
		case 4: fmt.Println("ddd")
		default: fmt.Println("Unknown number")
	}
}

