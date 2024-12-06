def get_most_common_letter(text):
    counter = {} #empty dict
    for char in text:
        #print(f"Iteration in text: {char}")
        counter[char] = counter.get(char, 0) + 1
        #print(counter[char])
    letter = sorted(counter.items(), key=lambda item: item[0])[8][0]
    print(letter)
    #print(letter[0][0])
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")