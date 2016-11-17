import lejos.hardware.motor.Motor;

public class CurvedPath extends StraightLine{
	public static double TURN_RATIO = 1.61438;
	public static double ALPHA = 2.3;
	public static double BETA = 132.7;
	public static double DELTA = 182.472;

	public static void main(String[] args) {
		CurvedPath.turn(ALPHA*DEG_TO_DEG);
		straight(DELTA*DIST_TO_DEG);
		CurvedPath.turn(BETA*DEG_TO_DEG);
	}
	
	public static void turn(double degrees){
		//Turns Left
		Motor.B.setSpeed(SPEED);
		Motor.C.setSpeed(Math.round(SPEED*TURN_RATIO));
		
		Motor.B.rotate((int)Math.round(degrees), true);
		Motor.C.rotate((int)Math.round(degrees*TURN_RATIO));
		
		Motor.C.setSpeed(SPEED);
		Motor.B.setSpeed(SPEED);
	}

}
