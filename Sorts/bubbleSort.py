def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] =  collection[j + 1],  collection[j]
        if not swapped:
            break
    return collection


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*bubble_sort(unsorted), sep=",")