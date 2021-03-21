
num_input = input("Please enter a number?")

ones = {
    '0': "zero",
    '1': "one",
    '2': "two",
}

n_as_word = ones.get(num_input)
print(n_as_word)