
import java.awt.*;
import javax.swing.*;

class JMandelbrot extends JFrame {

	final int RES = 600;  //resolucion
	final int ITERACIONES = 255; //iteraciones

	//porcion del conjunto de Mandelbrot a mostrar
	final double XPOS = -2.0;
	final double YPOS = -1.5;
	final double LADO = 3;

	public JMandelbrot(){
		super("Manderbrot");
		setBounds(0,0,RES,RES);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container con = this.getContentPane();
		con.setBackground(Color.white);
		GCanvas canvas = new GCanvas(RES, XPOS, YPOS, LADO, ITERACIONES);

		con.add(canvas);
		setVisible(true);

	}

	public static void main(String[] args) {
		new JMandelbrot();
	}
}

class GCanvas extends Canvas {

	int res, iteraciones;
	double xpos, ypos, lado, delta;

	public GCanvas(int res, double xpos, double ypos, double lado, int iteraciones){
		this.res = res;
		this.xpos = xpos;
		this.ypos = ypos;
		this.lado = lado;
		this.delta = lado / res;
		this.iteraciones = iteraciones;
	}

	double c_real, c_imaginaria, z_real, z_imaginaria, zr, zi, modulo;
	int cont, color;

	public void paint(Graphics g){
		for (int i=0; i<res; i++ ) {
			for (int j=0;j<res; j++) {
				//calculo del numero complejo C correspondiente
				//aal pixel actual
				c_real = xpos + (i*delta);
				c_imaginaria = ypos + (j*delta);

				//inicializamos Z
				z_real = 0.0;
				z_imaginaria = 0.0;
				cont = 0;

				//calcular si el punto pertenece al conjunto de Mandelbrot
				do{
					zr = ((z_real * z_real)- (z_imaginaria*z_imaginaria) + c_real);
					zi = 2 * (z_real * z_imaginaria)+ c_imaginaria;
					z_real = zr;
					z_imaginaria = zi;
					cont++;
					modulo = Math.sqrt((z_real*z_real)+ (z_imaginaria*z_imaginaria));

				}while(cont <= iteraciones && modulo < 2);

				//transformacion el valor a escala de grises
				if (cont< iteraciones){
					color = ((iteraciones-cont)* 255)/iteraciones;
				}else{
					color = 0;
				}
				//dibujar el pixel
				g.setColor(new Color(color, color, color));

				g.drawLine(i,j,i,j);
			}
		}
	}
}	