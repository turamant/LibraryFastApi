from matplotlib import pyplot as plt

data = {'Smartphon': 251, 'Computer': 340, 'Laptop': 36, 'TV': 10}

def test_arr(arr):
    return list(arr.keys()), list(arr.values())

def table(arr):
    index, values = test_arr(arr)

    plt.title("Analitics")
    plt.xlabel("Modul")
    plt.ylabel("Показатель в шт")
    plt.bar(index, values)
    plt.show()

if __name__== '__main__':
    table(data)