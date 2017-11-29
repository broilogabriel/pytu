import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("cmd", help="start | stop | status | show")
    args = parser.parse_args()