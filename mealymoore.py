class MealyState:
    def __init__(self, name):
        self.name = name
        self.transitions = {}  # diri nato ibutang ang possible transitions (input → next_state, output)

    def add_transition(self, input_symbol, next_state, output):
        # mag-add ta og transition para sa usa ka input
        self.transitions[input_symbol] = (next_state, output)


class MealyMachine:
    def __init__(self):
        # States:
        # A = wala pa'y previous nga 1
        # B = previous input kay 1
        self.states = {
            'A': MealyState('A'),
            'B': MealyState('B')
        }

        # Transitions: (state, input) → (next_state, output)
        # Kung naa ta sa state A unya input 0, balik ra sa A, output b
        self.states['A'].add_transition('0', 'A', 'b')
        self.states['A'].add_transition('1', 'B', 'b')

        # Kung naa ta sa B unya input 1, mao na ang pattern "11", so output a
        self.states['B'].add_transition('0', 'A', 'b')
        self.states['B'].add_transition('1', 'B', 'a')

        # magsugod ta sa state A
        self.current_state = self.states['A']

    def process_input(self, input_string):
        print("\n===================")
        print("MEALY MACHINE (11)")
        print("===================")
        print(f"{'Input':<6}{'State':<6}{'Output'}")

        output = ''
        self.current_state = self.states['A']  # reset state kada run

        for symbol in input_string:
            # kuhaa ang next state ug output base sa input
            next_state, out = self.current_state.transitions[symbol]
            print(f"{symbol:<6}{self.current_state.name:<6}{out}")
            output += out
            self.current_state = self.states[next_state]  # move to next state

        print(f"\nFinal Output: {output}")
        return output


class MooreState:
    def __init__(self, name, output):
        self.name = name
        self.output = output  # fixed output per state (mao ni difference sa Mealy)
        self.transitions = {}  # input → next_state

    def add_transition(self, input_symbol, next_state):
        # mag-set sa transition para sa usa ka input
        self.transitions[input_symbol] = next_state


class MooreMachine:
    def __init__(self):
        # States:
        # A = wala pa’y 1
        # B = previous kay 1
        # C = detected na ang “11”
        self.states = {
            'A': MooreState('A', 'b'),
            'B': MooreState('B', 'b'),
            'C': MooreState('C', 'a')
        }

        # Transitions
        # gikan sa A, kung 1 → B; kung 0 → A ra gihapon
        self.states['A'].add_transition('0', 'A')
        self.states['A'].add_transition('1', 'B')

        # gikan sa B, kung 1 → C (kay “11”), kung 0 → A
        self.states['B'].add_transition('0', 'A')
        self.states['B'].add_transition('1', 'C')

        # gikan sa C, kung 1 → C gihapon (continuous 1’s), kung 0 → A
        self.states['C'].add_transition('0', 'A')
        self.states['C'].add_transition('1', 'C')

        # start sa A
        self.current_state = self.states['A']

    def process_input(self, input_string):
        print("\n========================")
        print("MOORE MACHINE (11)")
        print("========================")
        print(f"{'Input':<6}{'State':<6}{'Output'}")

        output = ''
        self.current_state = self.states['A']  # reset kada run

        # una, i-print ang initial state output (Moore machine always outputs first)
        print(f"{'':<6}{self.current_state.name:<6}{self.current_state.output}")
        output += self.current_state.output

        for symbol in input_string:
            # move to next state depende sa input
            self.current_state = self.states[self.current_state.transitions[symbol]]
            print(f"{symbol:<6}{self.current_state.name:<6}{self.current_state.output}")
            output += self.current_state.output

        print(f"\nFinal Output: {output}")
        return output


# ===============================
# MAIN PROGRAM
# ===============================
if __name__ == "__main__":
    print("=== Finite State Machine Simulator ===")
    
    while True:
        user_input = input("Enter binary string (e.g. 1101): ").strip()

        # basic validation - dapat 0 or 1 ra
        if not all(ch in '01' for ch in user_input):
            print("Invalid input (program only accepts Binary)!.\n")
            continue

        # Run Moore Machine
        moore = MooreMachine()
        moore.process_input(user_input)

        # Run Mealy Machine
        mealy = MealyMachine()
        mealy.process_input(user_input)

        # ask if magpadayon pa
        choice = input("\nDo you want to try another input? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nProgram terminated.!")
            break

        print("\n-----------------------------------\n")
