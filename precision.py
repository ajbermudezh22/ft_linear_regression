import sys
from utils import DATA_FILE, THETAS_FILE, estimate_price, load_dataset, load_thetas

mileages, prices = load_dataset(DATA_FILE)
theta_0, theta_1 = load_thetas(THETAS_FILE)

m = len(mileages)
if m == 0:
    sys.exit(f"Error: {DATA_FILE} has no data")

if theta_0 == 0 and theta_1 == 0:
    print("Warning: model is not trained yet (thetas are 0), run train.py first\n")

# Prediction error for every car: estimatePrice - real price
errors = []
for i in range(m):
    estimated = estimate_price(mileages[i], theta_0, theta_1)
    errors.append(estimated - prices[i])

# MAE: on average, how many euros the prediction is off
mae = sum(abs(e) for e in errors) / m

# MSE / RMSE: squaring makes big errors count more, root brings it back to euros
mse = sum(e ** 2 for e in errors) / m
rmse = mse ** 0.5

# R²: compare our error to the error of always guessing the mean price
mean_price = sum(prices) / m
ss_res = sum(e ** 2 for e in errors)
ss_tot = sum((p - mean_price) ** 2 for p in prices)

print(f"MAE  (mean absolute error):      {mae:.2f}")
print(f"MSE  (mean squared error):       {mse:.2f}")
print(f"RMSE (root mean squared error):  {rmse:.2f}")
if ss_tot == 0:
    print("R²   (coef. of determination):  undefined (all prices are the same)")
else:
    r2 = 1 - ss_res / ss_tot
    print(f"R²   (coef. of determination):  {r2:.4f}")
