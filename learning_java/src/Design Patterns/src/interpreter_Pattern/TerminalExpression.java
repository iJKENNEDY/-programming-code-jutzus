package interpreter_Pattern;

public class TerminalExpression implements Expression{
	
	private String data;

	public TerminalExpression(String data) {
		super();
		this.data = data;
	}
	
	public boolean interpret(String context) {
		// TODO Auto-generated method stub
		if (context.contains(data)) {
			return true;
		}
		return false;
	}
	
}
