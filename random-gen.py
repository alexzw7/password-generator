import os, sys, random, string

pass_length = int(sys.argv[1])
pass_type = sys.argv[2]

choices = []
generated_pass = ''

if 'a' in pass_type:
    for x in string.ascii_letters:
        choices.append(x)

if 'd' in pass_type:
    for y in string.digits:
        choices.append(y)

if 's' in pass_type:
    for z in string.punctuation:
        choices.append(z)

for count in range(pass_length):
    generated_pass += random.choice(choices)

print(generated_pass)