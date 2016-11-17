import lejos.hardware.Button;
import lejos.hardware.lcd.*;
import lejos.hardware.motor.*;
import lejos.hardware.port.SensorPort;
import lejos.hardware.sensor.EV3ColorSensor;

public abstract class FollowLine {
	
	private static final float ALPHA = 30;
	static NXTRegulatedMotor leftMotor = Motor.B;
	static NXTRegulatedMotor rightMotor = Motor.C;
	static EV3ColorSensor color = new EV3ColorSensor(SensorPort.S3);
	
	static float desired = 0.12f;
	
	protected void drive(float speed, float correction) {
		//correction = correction*(Math.signum(rightMotor.getSpeed() - leftMotor.getSpeed()));
		leftMotor.setSpeed(Math.round(speed + correction/2.0));
		leftMotor.forward();
		rightMotor.setSpeed(Math.round(speed - correction/2.0));
		rightMotor.forward();
		System.out.println("Left motor speed: " + Integer.toString(leftMotor.getRotationSpeed()));
	}

	protected float getReflectedLight() {
		int sampleSize = color.sampleSize();
		float[] redsample = new float[sampleSize];
		color.getRedMode().fetchSample(redsample, 0);
		return redsample[0];
	}
}
