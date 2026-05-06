whatgame = input("what game do you wanna play colorgame,madlib,number game,number game on steroids,semester calculator,the date,jojo guessing game,game,guess game")
q = ("colorgame")
w = ("madlib")
e = ("number game")
r = ("number game on steroids")
t = ("semester calculator")
y = ("the date")
u = ("jojo guessing game")
i = ("game")
o = ("guess game")
p = ("repair game")
##############################################
if whatgame == q:
    print("odkod")
    col = input(print("what is my coulour")).lower()
    q = ("red")
    w = ("orange")
    e = ("yellow")
    r = ("green")
    t = ("blue")
    y = ("pink")
    u = ("purple")
    i = ("brown")
    o = ("black")
    p = ("white")
    import random
    x = random.choice([q, w, e, r, t, y, u, i, o, p])
    if col == x:
        print(" noice")
    else:
        print("wrong it was" + x)
############################################
if whatgame == w:
    print("odkod")
    a1 = input("enter a random funny name ")
    print("one day me and my friend " + a1)
    a2 = input("enter a random funny name")
    print("one day me and my friend " + a1 + "went to the restaunt called " +
          a2)
    a3 = input("enter a random funny name ")
    print("one day me and my friend " + a1 + "went to the restaunt called " +
          a2 + "and ate a thing called" + a3)
    a4 = input("enter a random funny name ")
    print("             one day me and my friend " + a1 +
          " went to the restaunt called " + a2 + " and ate a thing called " +
          a3 + " it was so bad so we went back home and went to sleep")
##############################################
if whatgame == e:
    x = input("what number am i thinking of")

    q = (1)
    w = (2)
    e = (3)
    r = (4)
    t = (5)
    y = (6)
    u = (7)
    i = (8)
    o = (9)
    p = (10)
    import random
    zz = random.choice([q, w, e, r, t, y, u, i, o, p])
    if x == zz:
        print("you got it right u had a 1/10 chance")
    else:
        print("you got it wrong it was")
        print(zz)
##############################################

if whatgame == r:
    x6 = ""
    x6 = (input("what is the numer i am thinking of "))

    q = (1)
    w = (2)
    e = (3)
    r = (4)
    t = (5)
    y = (6)
    u = (7)
    i = (8)
    o = (9)
    p = (10)
    a = (11)
    s = (12)
    d = (13)
    f = (14)
    g = (15)
    h = (16)
    j = (17)
    k = (18)
    l = (19)
    z = (20)
    x = (21)
    c = (22)
    v = (23)
    b = (24)
    n = (25)
    m = (26)
    q1 = (27)
    w1 = (28)
    e1 = (29)
    r1 = (30)
    t1 = (31)
    y1 = (32)
    u1 = (33)
    i1 = (34)
    o1 = (35)
    p1 = (36)
    a1 = (37)
    s1 = (38)
    d1 = (39)
    f1 = (40)
    g1 = (41)
    h1 = (42)
    j1 = (43)
    k1 = (44)
    l1 = (45)
    z1 = (46)
    x1 = (47)
    c1 = (48)
    v1 = (49)
    b1 = (50)
    import random
    zzz = random.choice([
        q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b,
        n, m, q1, w1, e1, r1, t1, y1, u1, i1, o1, p1, a1, s1, d1, f1, g1, h1,
        j1, k1, l1, z1, x1, c1, v1, b1
    ])
    if x6 == zzz:
        print("you got it right u had a 1/50 chance")
    else:
        print("you got it wrong it was")
    print(zzz)
    ######################################################
if whatgame == t:
    sem1 = ""
    sem2 = ""
    sem3 = ""
    sem4 = ""
    y = "yes"
    n = "no"

    user_name = input(print("what is your name"))
    yesorno = input("hi " + user_name +
                    " i am a semester calculator would you like to continue")
    if yesorno == y:
        sem1 = int(input("what is ur semester 1 grades"))
        sem2 = int(input("what is ur semester 2 grades"))
        sem3 = int(input("what is ur semester 3 grades"))
        sem4 = int(input("what is ur semester 4 grades"))
        x = (sem1 + sem2 + sem3 + sem4)
        print(x / 4)
    else:
        print("ok have a nice day")
#################################################

#################################################
if whatgame == u:
    print(
        "here is your word bank Jonathan,Jolyne,Jotaro,Josuke,Giorno,Joseph,Josuke,Johnny"
    )

    def check_guess(guess, answer):
        global score
        still_guessing = True
        attempt = 0
        while still_guessing and attempt < 3:
            if guess.lower() == answer.lower():
                print("Correct Answer")
                score = score + 1
                still_guessing = False
            else:
                if attempt < 2:
                    guess = input("Sorry Wrong Answer, try again")
                attempt = attempt + 1
        if attempt == 3:
            print("The Correct answer is ", answer)

    score = 0
    print("Guess the jojo")
    guess1 = input("Who is the main jojo of part 1 ")
    check_guess(guess1, "Jonathan")

    guess2 = input("who is the jojo of part 2 ")
    check_guess(guess2, "Joseph")

    guess3 = input("who is the jojo of part 3 ")
    check_guess(guess3, "Jotaro")

    guess4 = input("Who is the best Jojo of part 4 ")
    check_guess(guess4, "Josuke")

    guess5 = input("Who is the best Jojo of part 5 ")
    check_guess(guess1, "Giorno")

    guess6 = input("Who is the best Jojo of part 6 ")
    check_guess(guess1, "Jolyne")

    guess7 = input("Who is the best Jojo of part  7 ")
    check_guess(guess1, "Johnny")

    guess8 = input("Who is the best Jojo of part 8 ")
    check_guess(guess1, "Josuke")

    print("Your Score is " + str(score))
################################################
if whatgame == y:
    import datetime
    x = datetime.datetime.now()
    print(x.year)
    print(x.strftime("%A"))
    print(x.month)
#################################################
if whatgame == i:
    answer_yes = ["Yes", "Y", "yes", "y"]
    answer_no = ["No", "N", "no", "n"]

    print("""
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shelter to him. (Yes / No)
""")

    ans1 = input(">>")

    if ans1 in answer_yes:
        print(
            "\nAfter 2 minutes, the Police came to your house, and ask you that whether the thief is in your house or not. Will you say (Yes / No)\n"
        )

        ans2 = input(">>")

        if ans2 in answer_yes:
            print(
                "\nYou are an honest person. He was a thief & You won the Game"
            )

        elif ans2 in answer_no:
            print("\nYou helped a thief. Now, go to Jail. GAME OVER")

        else:
            print("\nYou typed the wrong input. GOODBYE!")

    elif ans1 in answer_no:
        print(
            "\nNow, he is trying to kill you. Will, you knock him down? (Yes / No)\n"
        )

        ans3 = input(">>")

        if ans3 in answer_yes:
            print(
                "\nCongrats! He was a thief & You helped the police to catch him with your bravery."
            )

        elif ans3 in answer_no:
            print(
                "\nSorry! You are dead. He was a thief & He killed you. GAME OVER"
            )

        else:
            print("\nYou typed the wrong input. GOODBYE!")

    else:
        print("\nYou typed the wrong input. GOODBYE!")
########################################################
if whatgame == o:

    def check_guess(guess, answer):
        global score
        still_guessing = True
        attempt = 0
        while still_guessing and attempt < 3:
            if guess.lower() == answer.lower():
                print("Correct Answer")
                score = score + 1
                still_guessing = False
            else:
                if attempt < 2:
                    guess = input("Sorry Wrong Answer, try again")
                attempt = attempt + 1
        if attempt == 3:
            print("The Correct answer is ", answer)

    score = 0
    print("Guess the Animal")
    guess1 = input("Which bear lives at the North Pole? ")
    check_guess(guess1, "polar bear")
    guess2 = input("Which is the fastest land animal? ")
    check_guess(guess2, "Cheetah")
    guess3 = input("Which is the largest animal? ")
    check_guess(guess3, "Blue Whale")
    print("Your Score is " + str(score))
    ########################################################
if whatgame == p:
 print ("")
i

