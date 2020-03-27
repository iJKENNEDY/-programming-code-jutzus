package command_pattern;

public class BuyStock implements Order{
	
	private Stock abcStock;

	public BuyStock(Stock abcStock) {
		super();
		this.abcStock = abcStock;
	}
	
	public void execute() {
		// TODO Auto-generated method stub
		abcStock.buy();
	}
	
}
