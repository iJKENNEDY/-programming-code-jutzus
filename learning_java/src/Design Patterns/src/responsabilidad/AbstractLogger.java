package responsabilidad;
/*::crea una cadena de objetos receptoes para un solicitud.
 * Este patron desacopla al remitente y al receptor de una 
 * solicitud en funcion del tipo de solicitud
 * 	
 */
public abstract class AbstractLogger {
	
	public static int INFO = 1;
	public static int DEBUG = 2;
	public static int ERROR = 3;
	
	protected int level;
	
	protected AbstractLogger nextLogger;
	
	public void setNextLogger(AbstractLogger nextLogger) {
		this.nextLogger = nextLogger;
	}
	
	public void loggMessage(int level, String message) {
		if (this.level <= level) {
			write(message);
		}
		if (nextLogger != null) {
			nextLogger.loggMessage(level, message);
		}
	}
	
	abstract protected void write(String message);
}

















