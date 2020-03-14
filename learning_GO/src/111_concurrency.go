package main 
import (
	"fmt"
	"time"
)

func pinger(c chain string) {
	for i := 0; i++ {
		c <- "ping"		
	}
}

func printer(c chain string) {
	for{
		msg:= <-c
		fmt.Println(msg)
		time.Sleep(time.Second * 1)
	}
}

func ponger(c chain string){
	for i := 0; i++ {
		c <- "pong"
	}
}

func main() {
	
}