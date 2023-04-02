import pandas as pd
import numpy as np


chat_id = 1121374935 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    time = 74 # По условию задачи 
    return np.mean(x)*2/time**2 # Ответ
