def metr_myle(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result * 0.000621371
        return result
    return wrapper


@metr_myle
def add(x, y):
    return x+y

if __name__=='__main__':
    result_metr = add(12, 12)
    print(result_metr,j)