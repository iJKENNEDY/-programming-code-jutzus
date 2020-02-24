package conexion_;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ConnectURL {
	
	private static Connection cn;
	
	public static Connection getConnection() {
		try {
			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
			cn = DriverManager.getConnection("jdbc:sqlserver://localhost:1433;databaseName=_tablas","username","password" );
		}catch (Exception e) {
			cn = null;
		}
		return cn;
	}
	
	public static void main(String[] args) {
		Connection pruebaCn = ConnectURL.getConnection();
		if(pruebaCn != null) {
			System.out.println("Connection");
			System.out.println(""+pruebaCn);
		}else {
			System.out.println("Desconectado");
		}
	}
}
