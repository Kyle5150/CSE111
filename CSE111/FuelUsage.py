print()
def main():
    start_miles = int(input("Enter the first odometer reading (in miles): "))
    end_miles = int(input("Enter the second odometer reading (in miles): "))
    amount_gallons = float(input("Enter the amount of fuel used (in gallons): "))
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)
    mpg = round(mpg, 1)
    lp100k = round(lp100k, 2)
    print(f"{mpg} miles per gallon\n{lp100k} liters per 100 kilometers")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    miles_gallon = (end_miles - start_miles) / amount_gallons
    return miles_gallon

def lp100k_from_mpg(mpg):
    kilo = 235.215 / mpg
    return kilo

main()
print()