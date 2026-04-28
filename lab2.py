def main():
    print ("ET0735 (Devops for AIoT)- lab 2 - introduction to python")
    display_main_menu()
    x = get_user_input()
    calc_average(x)
    find_min_max(x)
    print (find_min_max(x))
    sort_temperature(x)
    calc_median_temperature(x)

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
def get_user_input():
    print("get_user_input")
    temps = input()
    x = temps.split(",")
    float_temp = []
    for num_str in x :
        float_temp.append(float(num_str))
    return float_temp
def calc_average(x):
    total = sum(x)
    length = len(x)
    average = total/length
    print("calc_average")
    print("average temp = " +str(average))
def sort_temperature(x):
    print("sort_temperature")
    sorted_list = sorted(x)
    return sorted_list 
def calc_median_temperature(x):
    print("calc_median_temperature")
    sorted_list = sort_temperature(x)
    print('sorted_list', sorted_list)
    length = len(sorted_list)
    if length % 2 == 0: 
        mid1 = (length//2)-1
        mid2 = (length//2)
        median = (sorted_list[mid1]+sorted_list[mid2])/2
    else:
        mid = length//2 
        median = (sorted_list[mid])
    print("median = " +str(median))

def find_min_max(x):
    print("find_min_max")
    return[min(x),max(x)]


if __name__ == "__main__":
    main()
