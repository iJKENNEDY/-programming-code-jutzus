package template_pattern;

public class TemplatePatternDemo {
	
	public static void main(String[] args) {
		Game game = new Cricket();
		game.play();
		
		System.out.println();
		
		game = new Football();
		game.play();
	}
}
