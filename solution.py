import pandas as pd
import numpy as np
import scipy.stats as stats


chat_id = 1372197133 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.04
    conv_x = x_success/x_cnt #p246
    conv_y = y_success/y_cnt #p247
 
    # Пропорция успехов в комбинированном датасете:
    conv_combined = (x_success + y_success)/(x_cnt + y_cnt)
 
    # Разница конверсий/# разница пропорций в датасетах
    p_diff = conv_x - conv_y
 
    # считаем статистику в ст.отклонениях стандартного нормального распределения
    z_value = p_diff / np.sqrt(conv_combined * (1 - conv_combined) * (1/x_cnt + 1/y_cnt))
 
    # задаем стандартное нормальное распределение (среднее 0, ст.отклонение 1)
    distr = stats.norm(0, 1)
 
    p_value = (1 - distr.cdf(abs(z_value))) * 2
 
 
 
    if (p_value < alpha):
        a = False
    else:
        a = True
    return a # Ваш ответ, True или False
