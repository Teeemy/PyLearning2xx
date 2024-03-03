def make_piadina(*onions, base="wheat"):  # calling function with base
    print(onions, base)
    for onion in onions:  # printing as for loop
        print(onion)  # printing as for loop
        return onions


mariam = make_piadina("cabbage", "tomato", "meat", base="thin")
ray = make_piadina("cabbage", "tomato", "meat")

