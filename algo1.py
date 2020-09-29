def algo1():
    tab = []
    for i in range(1, 999):
        convertToString = str(i)
        if i < 100:
            convertToString = convertToString.zfill(3)
        array = list(map(int, list(convertToString)))
        sortedTab = sorted(array)
        if sortedTab not in tab:
            tab.append(sortedTab)
            if array[0] != array[1] and array[1] != array[2] and array[2] != array[0] :
                print("".join(list(map(str, sortedTab))))


algo1()
