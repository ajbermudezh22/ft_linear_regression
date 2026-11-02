import sys
from utils import DATA_FILE, THETAS_FILE, estimate_price, load_dataset

# hyperparameters
learning_rate = 0.1
iterations = 5000

# load dataset
mileages, prices = load_dataset(DATA_FILE)
m = len(mileages)  # number of training examples

if m < 2:
    sys.exit("Error: need at least 2 data points to train")

# Normalize mileage to [0,1]
# Raw values are huge (up to 240000) which makes gradient descent
# overshoot and blow up to nan, scaling keeps them small
km_min = min(mileages)
km_max = max(mileages)

if km_max == km_min:
    sys.exit("Error: all mileages are the same, cannot fit a line")

scaled_mileages = [(km - km_min) / (km_max - km_min) for km in mileages]

# Gradient descent
theta_0 = 0.0
theta_1 = 0.0

for iteration in range(iterations):
    # Error of the current line on each data point: estimatePrice - price
    errors = []
    for i in range(m):
        estimated_price = estimate_price(scaled_mileages[i], theta_0, theta_1)
        errors.append(estimated_price - prices[i])

    # Compute both tmp values before updating anything
    tmp_theta_0 = learning_rate * (1 / m) * sum(errors)
    tmp_theta_1 = learning_rate * (1 / m) * sum(errors[i] * scaled_mileages[i] for i in range(m))

    # simultaneous update
    theta_0 -= tmp_theta_0
    theta_1 -= tmp_theta_1


# convert back to km
unscaled_theta_0 = theta_0 - theta_1 * km_min / (km_max - km_min)
unscaled_theta_1 = theta_1 / (km_max - km_min)

print(f"Unscaled thetas: {unscaled_theta_0} {unscaled_theta_1}")

# store thetas in a file
try:
    with open(THETAS_FILE, "w") as file:
        file.write(f"{unscaled_theta_0} {unscaled_theta_1}\n")
except OSError:
    sys.exit(f"Error: could not write {THETAS_FILE}")
