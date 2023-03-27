import math

print("Welcome to the Social Situation Analyzer System\nPerson One")
p1n = input("   Enter your name: ")
p1p = input("   Enter your position (x y): ")
p1r = input("   Enter your personal space radius: ")

#x1, y1 = p1p.split(" ")

print("\nPerson Two")
p2n = input("   Enter your name: ")
p2p = input("   Enter your position (x y): ")
p2r = input("   Enter your personal space radius: ")

#x2, y2 = p2p.split(" ")

def circle_overlap(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)

    if distance <= abs(r1 - r2) or distance <= r1 + r2:
        return True
    else:
        return False

x1 = 10
y1 = 10
p1r = 10
x2 = 10
y2 = 10
p2r= 10

print("\nSocial Situation Analysis Results:")

overlap = circle_overlap(x1, y1, float(p1r), x2, y2, float(p2r))
if overlap:
    print("The Circles overlap")

inside = circle_overlap(x1, y1, float(p1r), x2, y2, float(p2r))
if inside:
    print("The Circle is inside")

no_overlap = circle_overlap(x1, y1, float(p1r), x2, y2, float(p2r))
if no_overlap:
    print("The Circles don't overlap")

"""# Person Test
if distance < p1r:
    print("Person Two is in Person One's personal space")
elif distance < p2r:
    print("Person One is in Person Two's personal space")
elif distance > p1r:
    print("")
elif distance > p2r:
    print("")

# Space Test
if distance < p1r:
    print("Person Two is in Person One's personal space")
elif distance < p2r:
    print("Person One is in Person Two's personal space")
elif distance > p1r:
    print("")
elif distance > p2r:
    print("")

print(distance)"""

"""Person Test: Bob is in Alice's personal space
    Space Test: Alice and Bob's personal spaces overlap"""