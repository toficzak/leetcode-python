def numberOfWays(corridor: str) -> int:
    MOD = 10**9 + 7

    seats = []
    for i,c in enumerate(corridor):
        if c == "S":
            seats.append(i)

    if len(seats) % 2 != 0 or len(seats) == 0:
        return 0

    if len(seats) == 2:
        return 1

    num_of_ways = 1
    counter = 2

    while counter < len(seats):
        plants = seats[counter] - seats[counter  - 1] - 1
        num_of_ways = (num_of_ways * (plants + 1))
        counter += 2

    return num_of_ways % MOD
    #
    #
    # counter = 0
    # seats = []
    #
    # while counter < len(corridor):
    #     # print(corridor[counter])
    #     if corridor[counter] == "S":
    #         seats.append(counter)
    #
    #     # print(f"Seats: {seats}")
    #     counter += 1
    #
    # if len(seats) % 2 != 0:
    #     return 0
    #
    # counter = 2
    # choices = []
    #
    # while counter < len(seats):
    #     choices.append(seats[counter] - seats[counter - 1] - 1)
    #     counter += 2
    #
    # if len(choices) == 0 and len(seats) == 2:
    #     return 1
    #
    # num_of_ways = 1
    # for choice in choices:
    #     num_of_ways *= choice
    #
    # return num_of_ways % (10 ** 9 + 7)


if __name__ == '__main__':
    examples = [
        "PPSPSP"
        # "SSPPSPS",
        # "PPSPSP",
        # "S",
        # "P",
        # "PPPSPPPSPSSPPSPSSPSSPPPPSSPSSPPSPPPSSSPSSSPSSSSPSSSSSPSSPSPPSSPSSPPSSSPSPPPSSSSSPSSPPPSSPPSSPSSSPPSP"
    ]

    for example in examples:
        result = numberOfWays(example)
        print(str(result))
