colors = ["red", "green", "yellow", "blue", "green"]
numbers = [45, 98, 75, 65, 24, 88, 74, 56, 75]

set123 = {"a", "b", "a"}


def loops():
    for i in range(1, 10, 2):
        print(i)
    for j in range(0, len(colors)):
        print(colors[j])
    for k in range(0, len(numbers)):
        if numbers[k] <= 50:
            print(numbers[k])
    print(type(set123))
    print(set123)
    for n in range(0, len(set123)):
        print(set123[n])
