import math

PANDEMIC_PROB = .9
DEADLY_PROB = .7

no_pandemic = "no pandemic"
non_deadly_pandemic = "non-deadly pandemic"
deadly_pandemic = "deadly pandemic"
STATES = [no_pandemic, non_deadly_pandemic, deadly_pandemic]

mandate = "mandate"
no_mandate = "no mandate"
ACTIONS = [mandate, no_mandate]

probability_table = {
    no_pandemic : 1 - PANDEMIC_PROB,
    non_deadly_pandemic : 1 - DEADLY_PROB,
    deadly_pandemic : DEADLY_PROB
}

death_table = {}
sickness_table = {}
freedom_table = {
    mandate : -100,
    no_mandate : 100
}

def init():
    for action in ACTIONS:
        for state in STATES:

            if state == no_pandemic:
                death_table[(state, action)] = 2
                sickness_table[(state, action)] = 5

            if state == non_deadly_pandemic:
                death_table[(state, action)] = 3

                if action == mandate:
                    sickness_table[(state, action)] = 70
                if action == no_mandate:
                    sickness_table[(state, action)] = 100


            if state == deadly_pandemic:
                if action == mandate:
                    death_table[(state, action)] = 5
                if action == no_mandate:
                    death_table[(state, action)] = 25

                if action == mandate:
                    sickness_table[(state, action)] = 70
                if action == no_mandate:
                    sickness_table[(state, action)] = 100

    print("death_table: ", death_table)
    print("sickness_table: ", sickness_table)
    print("freedom_table: ", freedom_table)

def utility(deaths, sicknesses, freedom):
    return deaths*(-200) + sicknesses*(-10) + freedom

def main():
    utility_table = {}
    max_utility = -math.inf
    max_utility_action = None

    init()

    for state in STATES:
        for action in ACTIONS:
            deaths = death_table[(state, action)]
            sicknesses = sickness_table[(state, action)]
            freedom = freedom_table[action]

            probability = probability_table[state]

            utility_table[(state, action)] = utility(deaths, sicknesses, freedom) / probability

            if utility_table[(state, action)] > max_utility:
                max_utility = utility_table[(state, action)]
                max_utility_action = action

    print("utility_table: ", utility_table)
    print("Action to take: ", max_utility_action)




if __name__ == "__main__":
    main()
