import java.util.ArrayList;

import lejos.hardware.Button;
import lejos.hardware.lcd.LCD;

public class PIDController extends FollowLine {
	private float integral = 0;
	private float derivative = 0;
	
	private ArrayList<Float> lastErrors = new ArrayList<Float>();
	
	private float kP;
	private float kI;
	private float kD;
	private float speed;
	
	public PIDController(float kP, float kI, float kD, float speed) {
		super();
		this.kP = kP;
		this.kI = kI;
		this.kD = kD;
		this.speed = speed;
		lastErrors.add(0f);
	}
	
	public void loop(int distance, int desired) {
		int traveled = 0;
		float dx = 5;
		while (!Button.ENTER.isDown() && traveled < distance) {
			
			LCD.clear();
			float current = getDistance();
			float error = (desired - current);
			integral += error;
			derivative = error - lastErrors.get(lastErrors.size() - 1);
			
			lastErrors.add(error);
			if (lastErrors.size() > 20) {
				lastErrors.remove(0);
			}
			
			if (Math.abs(kI * integral) > 0.2*Math.abs(kP * error)) {
				integral = 0;
			}
			
			if (derivativeStable(desired)) {
				System.out.println("Stable!");
				integral = 0;
			}
			
			float correction = kP*error + kI*integral + kD*derivative;
			
			System.out.printf("Correction: %f\n", correction);
			System.out.printf("P: %f\n", error);
			System.out.printf("I: %f\n", integral);
			System.out.printf("D: %f\n", derivative);

			drive(speed, correction, dx);
			traveled += dx;
		}
	}

	private boolean derivativeStable(float desired) {
		float sum = 0;
		for (int i = 0; i < lastErrors.size() - 1; i++) {
			sum += lastErrors.get(i + 1) - lastErrors.get(i);
		}
		
		sum = sum / lastErrors.size();
		
		return Math.abs(sum) < (desired / 3);
	}
}
