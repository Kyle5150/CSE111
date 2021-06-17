print()
import math

num_items = int(input("Enter the number of items: "))
num_items_box = int(input("Enter the number of items per box: "))

num_boxes = num_items / num_items_box
round_boxes = math.ceil(num_boxes)

print(f"For {num_items} items, packing {num_items_box} items in each box, you will need {round_boxes} boxes.")
print()