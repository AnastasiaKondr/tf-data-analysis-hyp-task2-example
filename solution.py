import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
chat_id = 483660375 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.05
    # применяем критерий Колмогорова-Смирнова
    stat, p_value = ks_2samp(x, y)
    # сравниваем p-value с уровнем значимости
    return p_value < alpha
