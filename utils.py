import sys
import csv

DATA_FILE = "data.csv"
THETAS_FILE = "thetas.txt"

def estimate_price(mileage, theta_0, theta_1):
    """Hypothesis from the subject: estimatePrice = theta0 + theta1 * mileage"""
    return theta_0 + theta_1 * mileage

def load_dataset(filename):
    """Read a km, price in CSV file and return two lists: mileages and prices """
    mileages = []
    prices = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                if not row:  # ignore blank lines
                    continue
                mileages.append(float(row[0]))
                prices.append(float(row[1]))
    except FileNotFoundError:
        sys.exit(f"Error: {filename} not found")
    except StopIteration:
        sys.exit(f"Error: {filename} is empty")
    except (ValueError, IndexError):
        sys.exit(f"Error: {filename} contains an invalid row")
    return mileages, prices


def load_thetas(filename):
    """Return (theta_0, theta_1). Both are 0 if the model hasn't been trained yet."""
    try:
        with open(filename, "r") as file:
            thetas = file.read().split()
            return float(thetas[0]), float(thetas[1])
    except FileNotFoundError:
        return 0.0, 0.0
    except (ValueError, IndexError):
        sys.exit(f"Error: {filename} is invalid, run train.py again")


