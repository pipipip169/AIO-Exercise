import math


class Softmax:
    def __init__(self):
        # No initialization required for this class
        pass

    def softmax(self, x):
        exp_x = [math.exp(i) for i in x]  # Apply exp to each element
        sum_exp_x = sum(exp_x)            # Sum of all exp values
        return [i / sum_exp_x for i in exp_x]  # Normalize each exp value


class SoftmaxStable(Softmax):
    def __init__(self):
        super().__init__()

    def softmax_stable(self, x):
        max_x = max(x)  # Find the maximum value in x
        exp_x = [math.exp(i - max_x) for i in x]  # Apply exp to each element after subtracting max_x
        sum_exp_x = sum(exp_x)            # Sum of all exp values
        return [i / sum_exp_x for i in exp_x]  # Normalize each exp value

# Test case
x = [1, 2, 3]
softmax_result1 = SoftmaxStable().softmax(x)
softmax_result2 = SoftmaxStable().softmax_stable(x)
print(f"tensor ({softmax_result1})")
print(f"tensor ({softmax_result2})")