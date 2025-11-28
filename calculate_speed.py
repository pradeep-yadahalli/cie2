def calculate_speed(distance, time):
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return distance / time


def get_speed_info(distance, time):
    
    speed = calculate_speed(distance, time)
    return (
        f"Distance: {distance} km\n"
        f"Time: {time} hr\n"
        f"Speed: {speed:.2f} km/hr"
    )


if __name__ == "__main__":
    distance = float(input("Enter distance (in km): "))
    time = float(input("Enter time (in hours): "))

    speed = calculate_speed(distance, time)
    print(f"Speed = {speed} km/hr")
