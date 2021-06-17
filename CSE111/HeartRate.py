age = float(input("Please enter your age: "))
heart_max = 220 - age
heart_max_low = heart_max * 0.65
heart_max_high = heart_max * 0.85
print(f"When you exercise to strengthen your heart, you should\nkeep your heart rate between {int(heart_max_low)} and {int(heart_max_high)} beats per minute.")