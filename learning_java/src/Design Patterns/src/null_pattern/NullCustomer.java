package null_pattern;

public class NullCustomer extends AbstractCustomer{
	
	@Override
	public String getName() {
		// TODO Auto-generated method stub
		return "Not availble in customer database";
	}
	
	@Override
	public boolean isNil() {
		// TODO Auto-generated method stub
		return true;
	}
}
