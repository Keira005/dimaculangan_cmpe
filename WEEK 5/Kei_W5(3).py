strInput = "G0!G0!PowerRangersDuuuudududududu"

newString = ""
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)