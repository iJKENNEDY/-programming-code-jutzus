package businessDelegatePattern;

public class BusinessDelegatePatternDemo {
	public static void main(String[] arg) {
		BusinessDelegate businessDelegate = new BusinessDelegate();
		businessDelegate.setServiceType("EJB");
		
		Client client = new Client(businessDelegate);
		client.doTask();

		businessDelegate.setServiceType("JMS");
		client.doTask();	
	}
}
