#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Servo parameters
#define SERVOMIN 150
#define SERVOMAX 600

// Store 18 servo angles
float servoAngles[18];

// Convert angle (0–180) to PWM
int angleToPulse(float angle) {
  return map(angle, 0, 180, SERVOMIN, SERVOMAX);
}

void setup() {
  Serial.begin(115200);
  pwm.begin();
  pwm.setPWMFreq(50); // Standard servo frequency
  delay(10);

  // Initialize all servos to 90°
  for (int i = 0; i < 18; i++) {
    servoAngles[i] = 90;
    pwm.setPWM(i, 0, angleToPulse(servoAngles[i]));
  }
}

void loop() {
  // Expecting 18 comma-separated values from ROS
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');

    int index = 0;
    char *token = strtok((char*)data.c_str(), ",");

    while (token != NULL && index < 18) {
      servoAngles[index] = atof(token);
      pwm.setPWM(index, 0, angleToPulse(servoAngles[index]));
      token = strtok(NULL, ",");
      index++;
    }
  }
}