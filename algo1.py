def algo1():
    storage = []
    for i in range(1, 1000):
        convertToString = str(i)
        if i < 100:
            convertToString = convertToString.zfill(3)
        array = list(map(int, list(convertToString)))
        sortedArray = sorted(array)
        if sortedArray not in storage:
            storage.append(sortedArray)
            print("".join(list(map(str, sortedArray))))

algo1()
