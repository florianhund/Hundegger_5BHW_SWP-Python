import random


def generate_unique_numbers(num_picks=6):
    # arr = list(range(45))

    arr = [i*i for i in range(45) if i % 2 == 0]

    # numbers = []
    length = len(arr)

    for _ in range(num_picks):
        random_index = random.randint(0, length - 1)

        # picked_number = arr[random_index]
        # numbers.append(picked_number)

        arr[random_index], arr[length - 1] = arr[length - 1], arr[random_index]
        length -= 1

    # return numbers[]
    return arr[-6:]


def count_number_occurrences(num_trials=1000):
    count = {}

    for _ in range(num_trials):
        unique_numbers = generate_unique_numbers(6)
        for number in unique_numbers:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1

    return count


def main():
    occurrences = count_number_occurrences(1000)

    for number in range(45):
        print(f"Number {number + 1} was chosen {occurrences[number]} times")


if __name__ == "__main__":
    main()
