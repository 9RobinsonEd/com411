#Simple List

def directions(file_name):
    print("these are the directions")
    with open(file_name) as file:
       for location in file:
            print(f"Looked in {location.strip()} ")

def run():
    search("directions.txt")

if __name__ == "__main__":
    run()
