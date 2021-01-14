#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for 2D list


import random


def average_of_numbers(passed_in_2D_list, rows_int, columns_int):
    # this function adds up all the elements in  a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element
    average = total/(rows_int * columns_int)

    return average


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = input("How many row would you like: ")
    columns = input("How many columns would you like: ")

    try:
        rows_int = int(rows)
        try:
            columns_int = int(columns)
            if rows_int > 0 and columns_int > 0:
                for loop_counter_rows in range(0, rows_int):
                    temp_column = []
                    for loop_counter_columns in range(0, columns_int):
                        a_random_number = random.randint(0, 50)
                        temp_column.append(a_random_number)
                        print("{0} ".format(a_random_number), end="")
                    a_2d_list.append(temp_column)
                    print("")
                average = average_of_numbers(a_2d_list, rows_int, columns_int)
                print("The average of all the numbers is: {0:,.3f} "
                      .format(average))
            else:
                print("It's not a positive numbers")
        except Exception:
            print("The columns is not a integer")
    except Exception:
        print("The rows is not a integer")


if __name__ == "__main__":
    main()
