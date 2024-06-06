# Calculates the F1-score
def f1_score(tp, fp, fn):
  """
  Calculates the F1-score, a measure of the accuracy of a classification model.

  Args:
    tp: The number of true positives (correctly predicted positive cases).
    fp: The number of false positives (incorrectly predicted positive cases).
    fn: The number of false negatives (incorrectly predicted negative cases).

  Returns:
    The F1-score, a value between 0 and 1.
  """
  if not isinstance(tp, int):
      print("tp must be integers")
  elif not isinstance(fp, int):
      print("fp must be integers")
  elif not isinstance(fn, int):
      print("fn must be integers")
  elif tp <= 0 or fp <= 0 or fn <= 0:
      print("tp and fp and fn must be greater than zero")
  else:
      precision = tp / (tp + fp)
      recall = tp / (tp + fn)
      f1 = 2 * (precision * recall) / (precision + recall)
      print("Precision is:", precision)
      print("Recall is:", recall)
      print("F1-score is:", f1)
# Test
f1_score(tp=2, fp=3, fn=4)

f1_score(tp="a", fp=3, fn=4)

f1_score(tp=2, fp="a", fn=4)

f1_score(tp=2, fp=3, fn="a")

f1_score(tp=2, fp=3, fn=0)

f1_score(tp=2.1, fp=3, fn=0)