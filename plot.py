import matplotlib.pyplot as plt
from utils import DATA_FILE, THETAS_FILE, estimate_price, load_dataset, load_thetas

mileages, prices = load_dataset(DATA_FILE)
theta_0, theta_1 = load_thetas(THETAS_FILE)

# Data: one dot per car
plt.scatter(mileages, prices, label="Data")

# The regression line: a straight line only needs 2 points
line_x = [0, max(mileages)]
line_y = [estimate_price(km, theta_0, theta_1) for km in line_x]
plt.plot(line_x, line_y, color="red",
        label=f"price = {theta_0:.2f} + ({theta_1:.5f} * km)")
plt.title("Car price vs mileage")
plt.xlabel("Mileage (km)")
plt.ylabel("Price (€)")
plt.legend()
plt.grid(True)
plt.show()