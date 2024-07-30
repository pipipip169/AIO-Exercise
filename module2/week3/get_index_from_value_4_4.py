from compute_conditional_probability_4_3 import list_x_name
import numpy as np

def get_index_from_value(feature_name, list_features):
    list_features_array = np.array(list_features)  # Chuyển đổi list_features sang dạng mảng Numpy
    return np.nonzero(list_features_array == feature_name)[0][0]

outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
