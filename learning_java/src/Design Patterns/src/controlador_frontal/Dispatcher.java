package controlador_frontal;

public class Dispatcher {
	
	private StudentView studentView;
	private HomeView homeview;
	
	public Dispatcher() {
		studentView = new StudentView();
		homeview = new HomeView();
	}
	
	public void dispatch(String request) {
		if (request.equalsIgnoreCase("STUDENT")) {
			studentView.show();
		}else {
			homeview.show();
		}
	}
}
