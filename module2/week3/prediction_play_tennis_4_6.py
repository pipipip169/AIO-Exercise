from get_index_from_value_4_4 import get_index_from_value
from train_naive_bayes_4_5 import prior_probability, conditional_probability, list_x_name
import numpy as np


def prediction_play_tennis(feature, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(feature[0], list_x_name[0])
    x2 = get_index_from_value(feature[1], list_x_name[1])
    x3 = get_index_from_value(feature[2], list_x_name[2])
    x4 = get_index_from_value(feature[3], list_x_name[3])

    p_yes = prior_probability[1]
    p_no = prior_probability[0]

    p_yes *= conditional_probability[0][1][x1]
    p_yes *= conditional_probability[1][1][x2]
    p_yes *= conditional_probability[2][1][x3]
    p_yes *= conditional_probability[3][1][x4]

    p_no *= conditional_probability[0][0][x1]
    p_no *= conditional_probability[1][0][x2]
    p_no *= conditional_probability[2][0][x3]
    p_no *= conditional_probability[3][0][x4]

    if p_no > p_yes:
        y_pred = "Ad should not go!", p_no
    else:
        y_pred = "Ad should go!", p_yes

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)
print(pred)
