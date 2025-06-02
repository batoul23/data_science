import matplotlib.pyplot as plt

def mergeSort(list):
    """
    Sortiert die übergebene Liste in-place mit dem Merge-Sort-Algorithmus.
    
    Merge Sort ist ein Divide-and-Conquer-Algorithmus, der die Liste rekursiv
    in kleinere Teillisten aufteilt, sortiert und dann zusammenführt.

    Parameter:
        array (list): Die zu sortierende Liste von vergleichbaren Elementen.
    """
    if len(list) <= 1:
        return  # Basisfall: Liste ist bereits sortiert
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    mergeSort(left)
    mergeSort(right)

    left_index = 0
    right_index = 0
    i = 0

    # Zusammenführen der sortierten Hälften
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            list[i] = left[left_index]
            left_index += 1
        else:
            list[i] = right[right_index]
            right_index += 1
        i += 1

    # Reste aus der linken Hälfte einfügen    
    while left_index < len(left):
        list[i] = left[left_index]
        left_index += 1
        i += 1

    # Reste aus der rechten Hälfte einfügen
    while right_index < len(right):
        list[i] = right[right_index]
        right_index += 1
        i += 1    

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Vor dem Sortieren
plt.plot(range(len(data)), data, label="Unsortiert")
plt.title("Vor dem Sortieren")
plt.show()

mergeSort(data)

# Nach dem Sortieren
plt.plot(range(len(data)), data, label="Sortiert", color="green")
plt.title("Nach dem Sortieren")
plt.show()
