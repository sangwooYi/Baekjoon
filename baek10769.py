S = list(input())

happy = 0
sad = 0

ptr = 0

while ptr < len(S):

    if S[ptr] == ":" and ptr < len(S)-2:
        if S[ptr+1] == "-" and S[ptr+2] == ")":
            happy += 1
            ptr += 3
            continue
        if S[ptr+1] == "-" and S[ptr+2] == "(":
            sad += 1
            ptr += 1
            continue
    ptr += 1

if happy == 0 and sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif happy == sad:
    print("unsure")
else:
    print("sad")