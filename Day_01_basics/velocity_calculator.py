def calculate_velocity(distance, time):
    velocity = distance / time
    return velocity

def calculate_acceleration(distance, time):
    acceleration = distance / (time ** 2)
    return acceleration

def distance_conversion(distance_unit):
    if distance_unit == "cm":
        distance = float(input("Enter the distance of the robot in cm: "))
        return distance / 100
    elif distance_unit == "m":
        distance = float(input("Enter the distance of the robot in m: "))
        return distance
    elif distance_unit == "km":
        distance = float(input("Enter the distance of the robot in km: "))
        return distance * 1000
    else:
        print("❌ Invalid unit. Please enter cm, m, or km.")
        return None

def main():
    distance_unit = input("Enter the unit of distance (cm/km/m): ").lower()
    distance = distance_conversion(distance_unit)

    if distance is None:
        return  # exit if unit was invalid

    time = float(input("Enter the time of the robot in seconds: "))

    if time == 0:
        print("❌ Time cannot be zero.")
        return

    velocity = calculate_velocity(distance, time)
    acceleration = calculate_acceleration(distance, time)

    print(f"✅ Velocity: {velocity:.2f} m/s")
    print(f"✅ Acceleration: {acceleration:.2f} m/s²")

if __name__ == "__main__":
    main()
