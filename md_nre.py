# Calculate Mean Difference of nth Root Error
def md_nre(y, y_hat, n, p):
  """
  Calculates the Mean Difference of nth Root Error (MDnRE) between the true values (y) and the predicted values (y_hat).

  Args:
    n: nth root.
    p: nth of loss function.

  Returns:
    The Mean Difference of nth Root Error value.
  """
  if not isinstance(y, (int, float)) or not isinstance(y_hat, (int, float)) or not isinstance(n, (int, float)) or not isinstance(p, (int, float)):
    print("y, y_hat, n, p  must be a number")
    return
  else:
    return (y**(1/n) - y_hat**(1/n))**p
  
#testing

print(md_nre(y=50, y_hat=49.5, n=2, p=1))
