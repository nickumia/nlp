# Random statistics functions

import math


def mean(val_list):
    '''
    IN: val_list, list(int)
    OUT: mean
    '''
    return sum(val_list)/len(val_list)


def standard_deviation(val_list):
    '''
    IN: val_list, list(int)
    OUT: avg
    OUT: standard deviation
    '''
    sd = 0
    avg = mean(val_list)

    for val in val_list:
        sd += math.pow((val - avg), 2)

    sd /= len(val_list)
    return avg, math.sqrt(sd)


def s_range(val_list):
    '''
    IN: val_list, list(int)
    OUT: range
    '''
    return max(val_list) - min(val_list)


def list_add(list1, list2):
    '''
    IN: list1, list, [1,2,3]
    IN: list2, list, [2,3,4]
    OUT: sum, list,  [3,5,7]
    '''
    return [a + b for a, b in zip(list1, list2)]


def confidence_level(x, mu, sd):
    '''
    IN: x, float, data point
    IN: mu, float, mean
    IN: sd, float, standard deviation
    '''
    try:
        position = (x - mu) / sd
    except ZeroDivisionError:
        position = 4
    if abs(position) <= 1:
        return (lambda x: x*(68-50) + 50 if x > 0
                else 50.0 - x*(32-50))(position)
    elif abs(position) <= 2:
        return (lambda x: (x % 1)*(95-68) + 68 if x > 0
                else 32.0 - (x % -1)*(5-32))(position)
    elif abs(position) <= 3:
        return (lambda x: (x % 1)*(99-95) + 95 if x > 0
                else 5.0 - (x % -1)*(1-5))(position)
    else:
        return (lambda x: (x % 1)*(100-99) + 99 if x > 0
                else 1.0 - (x % -1)*(0-1))(position)
