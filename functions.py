from random import randint

def random_list(size: int) -> int:
    """Function used to generate a list of random numbers"""
    num_list = []
    for i in range(0, size):
        random_number = randint(1, 1000)
        num_list.append(random_number)
    return num_list

def info(string: str, data: float) -> str:
    """Function used for formatting information"""
    with open(r"C:\Users\cmitc\OneDrive\Documents\CS Classes\CS317\Sorts Project\sorts.txt", 'a') as f:
        if string == "Size of List:":
            f.write('\n\n\n')
            f.write(string + " ")
            f.write(data)
            f.write('\n\n')
        else:
            f.write(string + "(Elapsed Time):\n")
            f.write(data)
            f.write(" seconds.\n")