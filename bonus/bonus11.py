def get_average():
    with open("files/data.txt", 'r') as file:
        # [1, 2, 3][1:] -> [2, 3]
        data = file.readlines()[1:]

    values = [float(i) for i in data]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)