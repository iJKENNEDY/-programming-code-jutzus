
import java.security.SecureRandom;
import java.util.Random;
import java.util.Scanner;

public class RandomLottery {

	int  a, b, c, d, e, f;
	SecureRandom rn = new SecureRandom();
	
	public void Juego_1()
	{
		int rango [] = new int[100];
		int t = 40;
		
		System.out.println("------------ JUEGO_1 ----------");
		
		for (int i = 0; i < rango.length; i++) {
			
			a = 1 + rn.nextInt(t);
			b = 1 + rn.nextInt(t);
			c = 1 + rn.nextInt(t);
			d = 1 + rn.nextInt(t);
			e = 1 + rn.nextInt(t);
			f = 1 + rn.nextInt(t);
			
			if ( a != b && b != c && c != d && d != e && e != f && e != a && f != a)
			{
				if ( b != d && b != e && b != f )
				{
					if ( c != a && c != e && c != f )
					{
						if ( d != a && d != b && d != f)
						{
							System.out.printf("    %2d %2d %2d %2d %2d %2d\n",a,b,c,d,e,f);
						}
					}
				}
			}							
		}
	}

	public void Juego_2()
	{
		int rango [] = new int[50];
		int t = 35;
		
		System.out.println("------------ juego_2 ----------");
		
		for (int i = 0; i < rango.length; i++) {
			
			a = 1 + rn.nextInt(t);
			b = 1 + rn.nextInt(t);
			c = 1 + rn.nextInt(t);
			d = 1 + rn.nextInt(t);
			e = 1 + rn.nextInt(t);
	
			
			if ( a != b && b != c && c != d && d != e  && e != a)
			{
				if ( b != d && b != e )
				{
					if ( c != a && c != e)
					{
						if ( d != a && d != b)
						{
							System.out.printf("    %2d %2d %2d %2d %2d\n",a,b,c,d,e);
						}
					}
				}
			}							
		}		
	}

		
	public void seleccionar()
	{
		Scanner leer = new Scanner(System.in);
		int opcion;
		System.out.printf("%s\n %s\n %s\n %s","Ingresa las siguientes opciones",
		"1.-Juego_1(5)", "2.-Juego_2(6)", " :: ");
		opcion = leer.nextInt();
		
		switch (opcion)
		{
			case 1:
				Juego_1();
				break;
			case 2:
				Juego_2();
							
		}
	}
	
	
	
	public static void main(String[] args) {
		RandomLottery rl = new RandomLottery();
		rl.seleccionar();
	}

}
