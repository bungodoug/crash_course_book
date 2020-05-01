# simple loop that gets some input from a user & uses try/except/else structure
# to prevent and control exceptions being raised and script crashing

print ("give me 2 numbers and I'll try to divide them")
print (" enter q at any time to quit")
while True:
    first_number = input("1st number :")
    if first_number.lower() == "q":
        break
    second_number = input("2nd number :")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print ("cant divide by 0")
    except ValueError:
        print ("cant input a character ... this isn't algebra")
    else:
        print(answer)