import lejos.hardware.Button;

public class BangBang extends FollowLine implements Controller {

	@Override
	public void loop() {
		while (!Button.ENTER.isDown()) {
			float current = getReflectedLight();
			float error = desired - current;
			drive(120, Math.signum(error) * 180);
		}
	}
}
