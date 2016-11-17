public class Lab3PID2 {
	public static void main(String[] args) {
		float speed = 210;
		PIDController controller = new PIDController(speed*7, speed/2, speed*8, speed);
		controller.loop();
	}
}
