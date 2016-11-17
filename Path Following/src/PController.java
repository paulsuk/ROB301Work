
public class PController extends PIDController {
	public PController(float kP, float speed) {
		super(kP, 0, 0, speed);
	}
}
