def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:]

    pivot = numbers[0]

    smaller = [n for n in numbers if n < pivot]
    equal = [n for n in numbers if n == pivot]
    bigger = [n for n in numbers if n > pivot]

    return quick_sort(smaller) + equal + quick_sort(bigger)

print(quick_sort([4, 42, 16, 23, 15, 8]))