package state_pattern;

public class StartState implements State{
	
	public void doAction(Context context) {
		System.out.println("Player is in start state");
		context.setState(this);
	}
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "Start state";
	}
}
