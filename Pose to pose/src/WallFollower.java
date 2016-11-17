public class WallFollower {
	public static void main(String[] args) {
		PController controller = new PController(1800, 300);
		controller.loop(100, 20);
		controller.loop(100, 30);
		controller.loop(100, 20);
	}
}
