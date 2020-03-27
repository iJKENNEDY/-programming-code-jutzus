package responsabilidad;

public class ChainPatternDemo {
	
	private static AbstractLogger getChainOfLoggers() {
		
		AbstractLogger errorLogger = new ErrorLogger(AbstractLogger.ERROR);
		AbstractLogger fileLogger  = new FileLogger( AbstractLogger.DEBUG);
		AbstractLogger consoleLogger = new ConsoleLogger(AbstractLogger.INFO);
		
		errorLogger.setNextLogger(fileLogger);
		fileLogger.setNextLogger(consoleLogger);
		
		return errorLogger;		
	}
	
	public static void main(String[] args) {
		AbstractLogger loggerChain = getChainOfLoggers();
		
		loggerChain.loggMessage(AbstractLogger.INFO, "this is an informattion");
		loggerChain.loggMessage(AbstractLogger.DEBUG, "this is an debug level information");
		loggerChain.loggMessage(AbstractLogger.ERROR, "this is an error information");
	}
}
