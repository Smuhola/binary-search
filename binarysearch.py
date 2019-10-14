import random
import math
import time

def binary_search(array, n, target):
    L = 0
    R = n - 1

    while L <= R:
        m = math.floor((L + R) / 2)
        if array[m] < target:
            L = m + 1
        elif array[m] > target:
            R = m - 1
        else:
            return m


def create_sorted_array(length):
    array = []
    start_array = time.time()
    for i in range(0, length):
        array.insert(0, i)
    end_array = time.time()


    start_sorting = time.time()
    array.sort()
    end_sorting = time.time()

    print(array)

    print_separator()

    print("Creating time: {} seconds".format(end_array - start_array))
    print("Sorting time: {} seconds".format(end_sorting - start_sorting))

    print_separator()

    return array

def write_to_file(array):
    with open("array.txt", "w") as txt_file:
        for element in array:
            txt_file.write(str(element) + "\n")

def get_from_file(filename):
    array = []
    with open(filename, "r") as txt_file:
        for line in txt_file:
            array.append(int(line))
            
    return array

def print_separator():
    print("-----------------------------")

def process_choice(choice):
    if choice == 1:
        length = int(input("Array length: "))
        array = create_sorted_array(length)
        target = random.choice(array)
        print("Searching for randomized value {} from array...".format(target))
    if choice == 2:
        filename = str(input("Enter file name including .txt \n> "))
        array = get_from_file(filename)
        length = len(array)
        target = int(input("Enter target value \n> "))
        print("Searching for {}...".format(target))
    if choice == 3:
        exit()

    start_search = time.time()
    index = binary_search(array, length, target)
    end_search = time.time()
    print_separator()

    if index == None:
        print("Target not in array")
    else:
        print("Target value at index {}".format(index))
        print("Searching time: {} seconds".format(end_search - start_search))

        


def main():

    valid_choices = [1, 2, 3]

    while True:
        try:
            choice = int(input("1: Create array \n2: Read from file \n3: Exit program \n>"))
            
            if choice not in valid_choices:
                print ("Wrong input")
                continue
            else:
                break
        except:
            print ("Wrong input")
            continue
        
    process_choice(choice)

if __name__ == "__main__":
    main()