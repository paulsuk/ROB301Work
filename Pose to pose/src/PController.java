import lejos.hardware.Button;
import lejos.hardware.lcd.LCD;

public class PController extends FollowLine {
	private float kP;
	private float speed;
	
	public PController(float kP, float speed) {
		this.kP = kP;
		this.speed = speed;
	}
	
	public void loop(int distance, int desired) {
		int traveled = 0;
		float dx = 5;
		while (!Button.ENTER.isDown() && traveled < distance) {
			
			LCD.clear();
			float current = getDistance();
			float error = (desired - current);

			float correction = kP*error;
			
			System.out.printf("Correction: %f\n", correction);
			System.out.printf("P: %f\n", error);

			drive(speed, correction, dx);
			traveled += dx;
		}
	}
}