import matplotlib.pyplot as plt


def merge_sort(values):
    """
    Sort a list in place using the merge sort algorithm.
    """
    if len(values) <= 1:
        return

    middle_index = len(values) // 2
    left_half = values[:middle_index]
    right_half = values[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)
    merge_sorted_halves(values, left_half, right_half)


def merge_sorted_halves(values, left_half, right_half):
    """
    Merge two sorted halves back into the original list.
    """
    left_index = 0
    right_index = 0
    target_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            values[target_index] = left_half[left_index]
            left_index += 1
        else:
            values[target_index] = right_half[right_index]
            right_index += 1

        target_index += 1

    while left_index < len(left_half):
        values[target_index] = left_half[left_index]
        left_index += 1
        target_index += 1

    while right_index < len(right_half):
        values[target_index] = right_half[right_index]
        right_index += 1
        target_index += 1


def plot_values(values):
    """
    Plot the values of a list.
    """
    x_values = range(len(values))
    plt.plot(x_values, values)
    plt.show()


def main():
    values = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_values(values)
    merge_sort(values)
    plot_values(values)


if __name__ == "__main__":
    main()
