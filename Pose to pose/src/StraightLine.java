import lejos.hardware.motor.*;
import lejos.hardware.Button;

public class StraightLine {
	
	public static double DEG_TO_DEG = (9+14.5)/(2*5.5);
	public static double DIST_TO_DEG = 360/(Math.PI*5.5);
	public static int SPEED = 200;
	
	public static void turn(double degrees){	
		Motor.C.rotate((int)Math.round(degrees), true);
		Motor.B.rotate((int)Math.round(-degrees));
	}
	
	public static void straight(double degrees){		
		Motor.C.rotate((int)Math.round(degrees), true);
		Motor.B.rotate((int)Math.round(degrees));
	}
	
	public static void pose(double x, double y, double theta){
		double rise = Math.atan2(y, x); 
		turn(rise*DEG_TO_DEG);
		straight(Math.pow((Math.pow(x,  2) + Math.pow(y, 2)), .5)*DIST_TO_DEG);
		turn((theta-rise)*DEG_TO_DEG);
	}
	
	public static void main(String[] args) throws Exception{
		Motor.C.setSpeed(SPEED);
		Motor.B.setSpeed(SPEED);
		
		pose(99, 0, 91);
		pose(0, 100, 99);
		pose(-100, 0, 97.4);
		pose(0, -100, 92);
		
		int i = 0;
		while (!Button.ENTER.isDown()) {
			i++;
		}
		
		pose(200, 50, 135);
	}
	
}
