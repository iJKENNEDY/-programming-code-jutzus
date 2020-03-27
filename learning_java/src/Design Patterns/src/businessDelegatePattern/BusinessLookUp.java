package businessDelegatePattern;

public class BusinessLookUp {
	public BusinessService getBusinessService(String serviceType){
		if(serviceType.equalsIgnoreCase("EBJ")){
			return new EJBService();
		}else{
			return new JMSService();
		}
	}
}
