print("\n-------- Application to demonstrate Industrial Programming --------\n")


def Addition(val1, val2):
    # Temporary Typecasting / type-conversion of the varible since input() always gets everything as string
    ans = val1 + val2
    return ans


def main():
    print("Enter First Number : ")
    no1 = int(input())                      # Typecasting right away for input.
    # print(type(no1))                      # input is always stored as string.
    print("Enter Second Number : ")
    no2 = int(input())
    sum = Addition(no1, no2)
    print("Addition is : ", sum)


if __name__ == "__main__":
    # print(__name__)
    main()

print("\n--------------------------- END ------------------------------------\n")
