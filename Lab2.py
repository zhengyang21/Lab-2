def display_main_menu():
    print("Enter Temperature readings separated by commas (e.g: 5, 67, 32)")
def calc_average_temperature():
    num_list =[]
    str = input()
    num_list = str.split(",")

    num_list = [int (i) for i in num_list]
    sum = sum(num_list)
    average = sum/ len(num_list)
    return average


def get_user_input() :
    num_list =[]
    str = input()
    num_list = str.split(",")

    num_list = [int (i) for i in num_list]
    return num_list

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average_temperature()
    print(num_list)
    print(str(type(num_list[0])))
    print (average)


if __name__ == "__main__":
    main()