from calc_func import do_addition , do_subtraction

def main():
    print("Welcome to the calculator app !!")
    print("""\nSelect the function from the given options
          1.Add
          2.Subtract
          """)
    
    user_input = input("Select the function")

    a = int(input("Vale of A "))
    b = int(input("Vale of B "))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result = do_subtraction(a,b)

    print('Result :', result)

if __name__ == "__main__":
    main()


