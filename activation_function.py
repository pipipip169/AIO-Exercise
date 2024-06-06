# Checks if a given value is a number
import math

def is_number(s):
    """Checks if a given value is a number.

  Args:
    n: The value to check.

  Returns:
    True if n is a number, False otherwise."""
    try:
        float(s)
        return True
    except ValueError:
        return False
# Calculates the specified activation function for a given input value
def activation_function(act_fn = input("Enter the activation function (sigmoid, relu, elu): ").lower(),x = input("Input x=")):
    """Calculates the specified activation function for a given input value.

  Args:
    act_fn: The name of the activation function (sigmoid, relu, or elu).
    x: The input value.

  Returns:
    The activation function applied to the input value."""
    if not is_number(x):
        print("x must be a number")
        return

    x = float(x)

    if act_fn == "sigmoid":
        print(f'Sigmoid: f({x}) =', 1 / (1 + math.exp(-x)))
    elif act_fn == "relu":
        print(f'ReLU: f({x}) =', max(0, x))
    elif act_fn == "elu":
        print(f'ELU: f({x}) =', 0.01 * (math.exp(x) - 1) if x < 0 else x)
    else:
        print(f"{act_fn} is not supported")

# testing
activation_function()