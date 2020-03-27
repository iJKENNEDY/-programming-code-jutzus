package interpreter_Pattern;

public class InterpreterPatternDemo {
	
	public static Expression getMaleExpression() {
		Expression robert = new TerminalExpression("Robert");
		Expression ariana = new TerminalExpression("Ariana");
		
		return new OrExpression(robert, ariana);
	}
	
	public static Expression getMarriedExpression() {
		Expression julie = new TerminalExpression("Julie");
		Expression married = new TerminalExpression("Married");
		
		return new AndExpression(julie, married);
	}
	
	public static void main(String[] args) {
		Expression isMale = getMaleExpression();
		Expression isMarriedWoman = getMarriedExpression();
		
		System.out.println("Robert is male? " + isMale.interpret("Robert"));
		System.out.println("Julie is a married women? "+ isMarriedWoman.interpret("Married Julie"));
	}
}
