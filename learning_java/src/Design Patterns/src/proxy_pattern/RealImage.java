package proxy_pattern;

public class RealImage implements Image 
{
	private String fileName;
	
		
	public RealImage(String fileName) {
		
		this.fileName = fileName;
		loadFromDisk(fileName);
	}

	public void display() {
		System.out.println("Displaying "+ fileName);		
	}
	
	public void loadFromDisk( String fileName) {
		System.out.println("Loading "+ fileName);
	}
	
}
