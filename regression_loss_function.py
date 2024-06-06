import random

# Calculates the regression loss function
def reg_loss_func(num_samples=input("Input number of samples ( integer number ) which are generated :"), loss=input("Input loss name:")):
  """
  Calculates and prints the specified regression loss for a given number of samples.

  Args:
    num_samples: The number of samples to generate.
    loss: The name of the loss function to use (MAE, MSE, or RMSE).

  Returns:
    None
  """
  if not num_samples.isnumeric():
    print("number of samples must be an integer number")
    return
  num_samples = int(num_samples)
  totall_loss = 0  # Initialize totall_loss to 0

  for i in range(num_samples):
    y_hat = random.uniform(0,10)
    y = random.uniform(0,10)
    if loss == "MAE":
      print(f"Loss name: {loss}, sample: {i}, pred: {y_hat}, target: {y}, loss: {abs(y-y_hat)}")
      totall_loss += abs(y-y_hat)
    elif loss == "MSE":
      print(f"Loss name: {loss}, sample: {i}, pred: {y_hat}, target: {y}, loss: {(y-y_hat)**2}")
      totall_loss += (y-y_hat)**2
    elif loss == "RMSE":
      print(f"Loss name: {loss}, sample: {i}, pred: {y_hat}, target: {y}, loss: {(y-y_hat)**2}")
      totall_loss += ((y-y_hat)**2)**0.5
    else:
      print(f"{loss} is not supported")

  final_loss = totall_loss/num_samples
  if loss in ("MAE", "MSE"):
    print(f"Final {loss}: {final_loss}")
  elif loss == "RMSE":
    print(f"Final RMSE: {final_loss**0.5}")
  else:
    print(f"{loss} is not supported")

  print()

#testing
reg_loss_func()