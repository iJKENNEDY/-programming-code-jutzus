package state_pattern;

public class StopState implements State{
	
	public void doAction(Context context) 
	{
		System.out.println("player is in stop state");
		context.setState(this);
	}
	
	public String toString() {
		return "Stop state";
	}
}
