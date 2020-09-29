def algo1():
    tab = []
    for i in range(1, 1000):
        convertToString = str(i)
        if i < 100:
            convertToString = convertToString.zfill(3)
        array = list(map(int, list(convertToString)))
        sortedTab = sorted(array)
        if sortedTab not in tab:
            tab.append(sortedTab)
            print("".join(list(map(str, sortedTab))))

algo1()
