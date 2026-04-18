import math

def inverse_kinematics(x, y, z, L1=5, L2=10, L3=10):
    # Base rotation
    theta1 = math.atan2(y, x)

    # Planar distance
    r = math.sqrt(x**2 + y**2) - L1
    d = math.sqrt(r**2 + z**2)

    # Law of cosines
    theta3 = math.acos((L2**2 + L3**2 - d**2) / (2 * L2 * L3))
    theta2 = math.atan2(z, r) + math.acos((L2**2 + d**2 - L3**2) / (2 * L2 * d))

    return math.degrees(theta1), math.degrees(theta2), math.degrees(theta3)