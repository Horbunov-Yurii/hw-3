import random
import timeit


def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def python_sort(arr):
    return sorted(arr)


def measure_time(function, data, number=1):
    timer = timeit.Timer(lambda: function(data))
    results = timer.repeat(repeat=3, number=number)

    return min(results) / number


def main():
    random.seed(42)

    sizes = [100, 1000, 3000]
    # sizes = [100, 500, 1000]

    for size in sizes:
        random_data = [
            random.randint(0, 10000)
            for _ in range(size)
        ]

        sorted_data = sorted(random_data)

        reversed_data = sorted_data[::-1]

        datasets = {
            "Випадкові": random_data,
            "Відсортовані": sorted_data,
            "У зворотному порядку": reversed_data,
        }

        print(f"\nКІЛЬКІСТЬ ЕЛЕМЕНТІВ: {size}")
        print("-" * 75)

        for dataset_name, data in datasets.items():
            print(f"\nНабір даних: {dataset_name}")

            for function in [
                insertion_sort,
                merge_sort,
                python_sort,
            ]:
                elapsed = measure_time(function, data)

                print(
                    f"{function.__name__:15} "
                    f"{elapsed:.6f} секунд"
                )


if __name__ == "__main__":
    main()
