import random
import art

choice = input("Do you want to play a game of BLACKJACK? Type 'Y' or 'N': ").lower()

if choice == 'y':
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user1 = random.choice(cards)
    user2 = random.choice(cards)
    u = [user1, user2]

    comp1 = random.choice(cards)
    comp2 = random.choice(cards)
    c = [comp1, comp2]

    cond = True
    while cond:
        # Check for user's Blackjack
        if 10 in u and 11 in u and len(u) == 2:
            print(f"Your final hand: {u}, final score: {sum(u)}")
            print(f"Computer's final hand: {c}, final score: {sum(c)}")
            print("YOU WIN!!! You have a BLACKJACK")
            break

        # Check for computer's Blackjack
        if 10 in c and 11 in c and len(c) == 2:
            print(f"Your final hand: {u}, final score: {sum(u)}")
            print(f"Computer's final hand: {c}, final score: {sum(c)}")
            print("YOU LOSE!!!")
            break

        # Handle user going over 21
        if sum(u) > 21:
            if 11 in u:
                u[u.index(11)] = 1
            else:
                print(f"Your final hand: {u}, final score: {sum(u)}")
                print(f"Computer's final hand: {c}, final score: {sum(c)}")
                print("YOU LOSE!!!")
                break

        else:
            choose = input(
                f"Your cards: {u}, current score: {sum(u)}\n"
                f"Computer's first card: {c[0]}\n"
                "Do you want another card? Type 'Y' or 'N': "
            ).lower()

            if choose == 'y':
                u.append(random.choice(cards))

            elif choose == 'n':
                while sum(c) < 17:
                    c.append(random.choice(cards))

                while 11 in c and sum(c) > 21:
                    c[c.index(11)] = 1

                print(f"Your final hand: {u}, final score: {sum(u)}")
                print(f"Computer's final hand: {c}, final score: {sum(c)}")

                if sum(c) > 21:
                    print("YOU WIN")
                elif sum(c) > sum(u):
                    print("YOU LOSE")
                elif sum(u) > sum(c):
                    print("YOU WIN")
                else:
                    print("DRAW")
                break

elif choice == 'n':
    print(art.bye)

else:
    print("WRONG INPUT!")
