package null_pattern;

public class RealCustomer extends AbstractCustomer 
{
	public RealCustomer(String name) {
		this.name = name;
	}
	
	@Override
	public String getName() {
		// TODO Auto-generated method stub
		return name;
	}
	
	@Override
	public boolean isNil() {
		// TODO Auto-generated method stub
		return false;
	}
}
