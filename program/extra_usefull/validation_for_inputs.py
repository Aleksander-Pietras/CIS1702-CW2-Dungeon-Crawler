''' This program can be used to make validation functions if you need a few of them
'''

def valid_bool(question: str) -> bool:
    ''' Ask a yes/no question and return True or False.
    '''
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Please answer 'yes' or 'no'.")

def valid_int(question: str) -> int:
    ''' Ask for an integer and keep asking until valid.
    '''
    while True:
        try:
            value = input(f"{question}: ").strip()
            value = int(value)
            return value
        except ValueError:
            print("Please enter a valid integer.")