package iterator_pattern;

public class NameRepository implements Container 
{
	public String names[] = {"Kebby", "Homero", "Lania", "Fatima"};
	
	public Iterator getIterator() {
		// TODO Auto-generated method stub
		return new NameIterator();
	}
	
	private class NameIterator implements Iterator{
		int index;
		
		public boolean hasnNext() {
			
			if (index < names.length) {
				return true;
			}
			return false;
		}
		
		public Object next() {
			
			if (this.hasnNext()) {
				return names[index++];
			}
			return null;
		}
	}
}
