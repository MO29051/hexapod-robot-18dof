import serial
import time
import math

# Serial connection (adjust port!)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)

# 18 servos
angles = [90.0] * 18

def tripod_gait(t):
    """Simple sinusoidal gait"""
    for i in range(18):
        if i % 2 == 0:
            angles[i] = 90 + 20 * math.sin(t)
        else:
            angles[i] = 90 + 20 * math.sin(t + math.pi)

def send_angles():
    data = ",".join([str(a) for a in angles]) + "\n"
    ser.write(data.encode())

def main():
    t = 0
    while True:
        tripod_gait(t)
        send_angles()
        t += 0.1
        time.sleep(0.05)

if __name__ == "__main__":
    main()