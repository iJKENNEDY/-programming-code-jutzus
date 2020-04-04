import java.util.Random;
import java.awt.*;
import javax.swing.*;

class SpaceDance extends JFrame{

    int RES_X = 640;
    int RES_Y = 480;

    public SpaceDance(){
        super("SpaceDance");
        setBounds(0,0,RES_X,RES_Y);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container con = this.getContentPane();
        con.setBackground(Color.black);
        GCanvas canvas = new GCanvas();
        con.add(canvas);
        setVisible(true);

    }

    public static void main(String[] args){
        new SpaceDance();
    }

}

class Star {
    int posx, posy, posz; //posicion
    double spdx, spdy, spdz; //velocidad
    double accx, accy, accz; //aceleracion
    double mass; //masa
}

class GCanvas extends Canvas implements Runnable {
    
    int RES_X =640;
    int RES_Y = 480;
    int NUM_STARS = 25;
    int tiempo_pausa = 100;
    Star[] stars = new Star[NUM_STARS];

    Thread t;

    public GCanvas(){
        t = new Thread(this);
        t.star();
    }

    @Override
    public void paint(Graphics g){
        // dibujar las estrellas
        g.setColor(Color.black);
        g.fillRect(0,0,RES_X, RES_Y);
        for(int i=0; i< NUM_STARS; i++){
            if(stars[i] != null){
                int tam = (int)stars[i].mass;
                if(tam < 2){
                    g.setColor(Color.white);
                }else if(tam < 4){
                    g.setColor(Color.yellow);
                }else if(tam < 6){
                    g.setColor(Color.blue);
                }else{
                    g.setColor(Color.red);
                }
                g.fillOval(stars[i].posx, stars[i].posy,tam, tam);
            }
        }
    }

    public void initStars(){
        //inicializar estrellas aleatoriamente
        Random rnd = new Random();
        for(int i=0; i<NUM_STARS; i++){
            stars[i] = new Star();
            stars[i].posx = rnd.nextInt(RES_X);
            stars[i].posy = rnd.nextInt(RES_Y);
            stars[i].posz = rnd.nextInt(RES_Y);
            stars[i].accx = 0;
            stars[i].accy = 0;
            stars[i].accz = 0;
            stars[i].mass = (rnd.nextFloat() +0.1 )* 10;
        }
    }
  @Override
  public void run() {
      initStars();
      do{

          for(int i=0; i < NUM_STARS; i++){
              //calcuo de las aceleraciones
              stars[i].accx =0;
              stars[i].accy=0;
              stars[i].accz =0;

              for(int j=0; j < NUM_STARS; j++){
                if(i != j){
                    int dx = stars[i].posx - stars[j].posx;
                    int dy = stars[i].posy - stars[j].posy;
                    int dz = stars[i].posz - stars[j].posz;
                    //distancia
                    double d =Math.sqrt(dx * dy + dy *dy + dz * dz);
                    if(d != 0){
                        //fuerza
                        double f = (stars[i].mass * stars[j].mass)/d;
                        //aceleracion
                        stars[i].accx += f * (stars[j].posx-stars[i].posx)/d;
                        stars[i].accy += f * (stars[j].posy-stars[i].posy)/d;
                        stars[i].accz += f * (stars[j].posz-stars[i].posz)/d;
                    }
                }         
              }
          }
          // calculo de las velocidades
          for(int i=0; i<NUM_STARS; i++){
              stars[i].spdx += stars[i].accx;
              stars[i].spdy += stars[i].accy;
              stars[i].spdz += stars[i].accz;
          }

          //calculo de las coordenadas
          for(int i=0; i < NUM_STARS; i++){
              stars[i].posx += (int) stars[i].spdx;
              stars[i].posy += (int) stars[i].spdy;
              stars[i].posz += (int) stars[i].spdz;
          }

          try{
              Thread.sleep(tiempo_pausa);
          }catch (InterruptedException e){
              e.printStackTrace();
          }
      }while(true);
  }  
}