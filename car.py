from operator import itemgetter


def file_to_list(file):
    cars_data = []
    with open(file, "r") as cars:
        formatted_file = [line.rstrip("\n") for line in cars]
        for line in formatted_file:
            word = line.split(",")
            cars_data.append(word)
    return cars_data


def average(cars_data, origin):
    sum_hp = 0
    count = 0
    for car in cars_data:
        if car[1] == origin:
            sum_hp += float(car[2])
            count += 1
    if count == 0:
        return 0
    return sum_hp / count


def greater_than_average(n, origin, cars_data, avg):
    m = 0
    cars_data = sorted(cars_data, key=itemgetter(2), reverse=True)
    for car in cars_data:
        if car[1] == origin and float(car[2]) > avg:
            print(car)
            m += 1
        if m == n:
            break


if __name__ == "__main__":
    n, origin = input().split()
    n = int(n)
    file = "cars_input1.txt"
    cars_data = file_to_list(file)
    avg = average(cars_data, origin)
    greater_than_average(n, origin, cars_data, avg)