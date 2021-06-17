print()
with open("/Users/kylejohnson/Documents/Python/CSE111/volumes.txt", "at") as volume_file:
    import math
    w = int(float(input("Enter the width of the tire in mm (ex 205): ")))
    a = int(float(input("Enter the aspect ratio of the tire (ex 60): ")))
    d = int(float(input("Enter the diameter of the wheel in inches (ex 15): ")))

    v = (math.pi * w ** 2 * a * (w * a + 2540 * d)) / 10000000
    liters = v / 1000
    print()
    print(f"The approximate volume is {v:.1f} milliliters\nor\n{liters:.1f} liters")
    print()

    from datetime import datetime
    current_date_time = datetime.now()

    buy_tires = input("Would you like to buy tires (yes/no)? ")

    if buy_tires == "yes":
        phone_number = input("Please enter your phone number ((555)555-5555): ")
        print(f"{current_date_time}, {w}, {a}, {d}, {v:.1f}, {phone_number}", file = volume_file)
        print("Thank you for your time.")
    else:
        print(f"{current_date_time}, {w}, {a}, {d}, {v:.1f}", file = volume_file)
        print("Thank you for your time.")

print()