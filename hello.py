import sys

# Get the comma-separated names from command line argument
if len(sys.argv) > 1 and sys.argv[1]:
    names_str = sys.argv[1]
    names_list = names_str.split(',')

    if len(names_list) == 1:
        print(f"{names_list[0]} good morning.")
    elif len(names_list) == 2:
        print(f"{names_list[0]} and {names_list[1]} good morning.")
    else:
        # For 3 or more names: "John, Jane and Jack good morning."
        all_but_last = ', '.join(names_list[:-1])
        print(f"{all_but_last} and {names_list[-1]} good morning.")
else:
    print("No names selected. Good morning!")
