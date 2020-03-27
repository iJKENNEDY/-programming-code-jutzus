package Builder_Pattern;

public abstract class Burger implements Item{
	
	public Packing packing() {
		// TODO Auto-generated method stub
		return new P_Wrapper();  
	}
	
	public abstract float price();
}
