
public class PIController extends PIDController {
	public PIController(float kP, float kI, float speed) {
		super(kP, kI, 0, speed);
	}
}
