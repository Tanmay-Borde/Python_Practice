import MarvellousModeule
print("\n-------- Application to demonstrate Industrial Programming --------\n")


def main():
    print("Value of __name__ from main is: ",__name__)
    print("Enter First Number : ")
    no1 = int(input())                      # Typecasting right away for input.
    # print(type(no1))                      # input is always stored as string.
    print("Enter Second Number : ")
    no2 = int(input())
    sum = MarvellousModeule.Addition(no1, no2)
    print("Value of __name__ from main is: ",__name__)
    print("Addition is : ", sum)


if __name__ == "__main__":
    # print(__name__)
    main()

print("\n--------------------------- END ------------------------------------\n")
