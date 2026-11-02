import sys
import math
from utils import THETAS_FILE, estimate_price, load_thetas

# load thetas
theta_0, theta_1 = load_thetas(THETAS_FILE)

# Ask for a mileage until we get a valid one
while True:
    try:
        mileage = float(input("Enter a mileage: "))
    except ValueError:
        print("Mileage needs to be a number")
        continue
    except (EOFError, KeyboardInterrupt):
        print() # move to new line
        sys.exit("Exiting.")

    if mileage < 0:
        print("Mileage cannot be negative")
        continue
    if not math.isfinite(mileage):
        print("Mileage needs to be a finite number")
        continue
    break

# Give prediction
price = estimate_price(mileage, theta_0, theta_1)
print(f"Estimated price: {price:.2f}")


