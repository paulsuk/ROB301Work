public class Lab3PI {
	public static void main(String[] args) {
		float speed = 180;
		PIController controller = new PIController(speed*7, speed/2, speed);
		controller.loop();
	}
}
