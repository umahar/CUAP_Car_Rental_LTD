"""can take any menu with any headings and get a valid user option"""

from data import prompts


def get_user_option(menu, heading):
    """gets the correct option"""
    while True:
        print(heading + ". Press '0' to Exit menu.\n")
        for index, item in enumerate(menu):
            print(f"{index+1}. {item}")
        opt = input("\nOPTION = ")
        if not opt.isdigit():
            print(prompts.INVALID_INPUT)
            continue
        if int(opt) == 0:
            return 0
        if int(opt) < 0 or int(opt) > len(menu):
            print(prompts.INVALID_INPUT)
            continue
        return int(opt) - 1
