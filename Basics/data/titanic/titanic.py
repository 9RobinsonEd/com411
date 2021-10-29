#titanic database
import csv

records[]

headings[]

def load_data(file_path):
    print("loading data...", end="")
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)


def run()
    load_data("titanic.csv")
if __name__ == "__main__":
    run()