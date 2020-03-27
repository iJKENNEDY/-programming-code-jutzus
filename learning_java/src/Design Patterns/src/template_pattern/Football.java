package template_pattern;

public class Football extends Game{
	
	@Override
	void endPlay() {
		System.out.println("Football Game Finished!");	
	}
	
	@Override
	void initialize() {
		System.out.println("Football Game Initialized! start playing.");	
	}
	
	@Override
	void startPlay() {
		System.out.println("Football Game started. Enjoy the game!");	
	}
}
