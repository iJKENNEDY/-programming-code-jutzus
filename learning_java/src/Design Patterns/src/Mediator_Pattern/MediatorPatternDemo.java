package Mediator_Pattern;

public class MediatorPatternDemo {

	public static void main(String[] args) {
		
		User rita = new User("Rita");
		User mar = new User("Maricielo");
		
		rita.sendMessage("Hi! Maricielo!");
		mar.sendMessage("Hello! Rita");
	}

}
