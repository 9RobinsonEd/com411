#index list

def movements():
    path = ["Move Forward ",10,"Move Backward",5,"Move left",3,"Move Right",1]
    return path
def run():
    print("Moving...")
    path = movements()
    print()
if __name__ == "__main__":
    run()
