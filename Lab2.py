def display_main_menu():
    print("display_main_menu")
def get_user_input():
    print("Enter Temperature readings separated by commas (e.g: 5, 67, 32)")
    num_list = []
    total = 0
    str = input()
    num_list = str.split(",")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def calc_average_temperature(num_list):
    total = 0
    for i in range(len(num_list)):
     total=total+num_list[i]
     avg=total/(i+1)

    print(avg)
    return num_list

def calc_min_max_temperature(num_list):
    max = num_list[0]
    min = num_list[0]
    for i in range(len(num_list)):
        if (max<num_list[i]):
            max=num_list[i]
    for i in range(len(num_list)):
        if (min>num_list[i]):
            min=num_list[i]
    print(max)
    print(min)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)
    print(num_list)


if __name__ == "__main__":
    main()


