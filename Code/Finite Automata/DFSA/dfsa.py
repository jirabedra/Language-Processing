import pandas as pd

class State:
    def __init__(self, name):
        self.name = name

class Action:
    def __init__(self, name):
        self.name = name

class NFSAutomaton:
    def __init__(self):
        self.lkuptable = {}
        
    def add_transition(self, current_state, action, new_state):
        self.lkuptable[(current_state, action)] = new_state


# Lookup table can be filled by reading a .csv with pandas using the following format
# current_state action new_state
def main():
    print("Please enter the lookup table .csv file name. The file should be located within this same folder.")
    valid = False
    while(not valid):
        name = input()
        try:
            path = f".\\{name}"
            print(path)
            data = pd.read_csv(path, sep=" ", header=None)
            data.columns = ["current","symbol","state"]
            break
        except Exception:
            print("Such file could not be found. Please try again.")
            break
        finally:
            valid = True
            break
    print(data.head())

main()

