import lejos.hardware.motor.*;
import lejos.hardware.port.SensorPort;
import lejos.hardware.sensor.EV3UltrasonicSensor;

public abstract class FollowLine {
	
	private static final double DISTANCE_PER_DEGREE = Math.PI*5.5;
	static NXTRegulatedMotor leftMotor = Motor.B;
	static NXTRegulatedMotor rightMotor = Motor.C;
	static EV3UltrasonicSensor ultrasonic = new EV3UltrasonicSensor(SensorPort.S3);
	
	protected void drive(float speed, float correction, float distance) {
		int rotation = (int) Math.round(distance / DISTANCE_PER_DEGREE);
		leftMotor.setSpeed(Math.round(speed + correction/2.0));
		leftMotor.rotate(rotation, true);
		rightMotor.setSpeed(Math.round(speed - correction/2.0));
		leftMotor.rotate(rotation, true);
	}

	protected float getDistance() {
		int sampleSize = ultrasonic.sampleSize();
		float[] distance = new float[sampleSize];
		ultrasonic.getDistanceMode().fetchSample(distance, 0);
		return distance[0];
	}
}
