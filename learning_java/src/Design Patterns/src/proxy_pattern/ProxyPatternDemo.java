package proxy_pattern;

public class ProxyPatternDemo {
	
	public static void main(String[] args) {
		Image image = new ProxyImage("test_2mb");
		
		image.display();
		System.out.println("");
		image.display();
	}
}
