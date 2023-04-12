import math

print("Welcome to the Social Situation Analyzer System\nPerson One")
p1n = input("   Enter your name: ")
p1p = input("   Enter your position (x y): ")
p1r = float(input("   Enter your personal space radius: "))

x1, y1 = p1p.split(" ")

print("\nPerson Two")
p2n = input("   Enter your name: ")
p2p = input("   Enter your position (x y): ")
p2r = float(input("   Enter your personal space radius: "))

x2, y2 = p2p.split(" ")


# Get distance
distance = math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)

# msg
msg = ("\nSocial Situation Analysis Results:")


# Person Test
if distance < float(p1r):
    pt1 = True
else:
    pt1 = False

if distance < float(p2r):
    pt2 = True
else:
    pt2 = False

msg += ("\n    Person Test: ")

if pt1 and pt2:
    msg += (p1n + " and " + p2n + " are in each other's personal space")
elif pt1:
    msg += (p2n + " is in " + p1n +"'s personal space")
elif pt2:
    msg += (p1n + " is in " + p2n + "'s personal space")
elif not (pt1 and pt2):
    msg += ("Neither " + p1n + " nor " + p2n + " is in the other's personal space")


# Space Test
msg += ("\n    Space Test: ")

if distance <= p1r - p2r:
    msg += (p2n + "'s personal space is entirely inside " + p1n + "'s personal space")
elif distance <= p2r - p1r:
    msg += (p1n + "'s personal space is entirely inside " + p2n + "'s personal space")
elif distance < p1r + p2r:
    msg += (p1n + " and " + p2n + "'s personal spaces overlap")
else:
    msg += (p1n + " and " + p2n + "'s personal spaces do not overlap")

print(msg)