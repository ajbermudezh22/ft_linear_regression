# ft_linear_regression

A 42 project introducing machine learning: predict the price of a car from its mileage using a linear function trained with gradient descent, implemented from scratch in Python.

```
estimatePrice(mileage) = θ0 + (θ1 * mileage)
```

## Files

| File | Description |
|---|---|
| `train.py` | Reads `data.csv`, trains θ0 and θ1 with gradient descent and saves them to `thetas.txt` |
| `predict.py` | Asks for a mileage and prints the estimated price (θ0 = θ1 = 0 before training) |
| `precision.py` | Bonus: measures the model's accuracy (MAE, MSE, RMSE, R²) |
| `plot.py` | Bonus: plots the data and the regression line |
| `utils.py` | Shared helpers: the hypothesis and file loading |
| `data.csv` | Dataset: mileage (km) and price |

## Requirements

- Python 3
- `matplotlib`, only for `plot.py`

The mandatory part (`train.py`, `predict.py`) uses only the standard library.

## Usage

```bash
# 1. Train the model
python3 train.py

# 2. Predict a price
python3 predict.py
Enter a mileage: 100000
Estimated price: 6354.70

# 3. Check the precision (bonus)
python3 precision.py

# 4. Plot the data and the regression line (bonus)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 plot.py
```

Running `predict.py` before `train.py` returns 0, as the model is not trained yet.

## How it works

- Mileages are normalized to `[0, 1]` (min-max scaling) before training, so gradient descent converges instead of diverging on large km values.
- θ0 and θ1 are updated simultaneously using the formulas from the subject, for 5000 iterations with a learning rate of 0.1.
- After training, the thetas are converted back to real km units, so `predict.py` works directly with raw mileage.

Result on `data.csv`: θ0 ≈ 8499.60, θ1 ≈ -0.02145, R² ≈ 0.733.

## Author

Alberto Bermudez ([@ajbermudezh22](https://github.com/ajbermudezh22))
