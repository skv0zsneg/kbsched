"""
    made by @skvozsneg
"""
DB_FILE = 'scded.db'


def get():
    try:
        rf = open(DB_FILE, 'r')
    except FileNotFoundError:
        with open(DB_FILE, 'w'):
            pass
        rf = open(DB_FILE, 'r')


if __name__ == "__main__":
    get()
