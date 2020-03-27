package command_pattern;

public class SellStock implements Order{
	
	private Stock abcStock;

	public SellStock(Stock abcStock) {
		super();
		this.abcStock = abcStock;
	}
	
	public void execute() {
		// TODO Auto-generated method stub
		abcStock.sell();
	}
}
