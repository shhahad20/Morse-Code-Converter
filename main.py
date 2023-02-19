# The length of a dot is one unit.
# A dash is three units.
# The space between parts of the same letter is one unit.
# The space between letters is three units.
# The space between words is seven units.
from dict import Alpha

SPACE7 = "      " # 6 units

# print(Alpha)
# t = Alpha.keys()
# print(t)
# g = Alpha.values()
# print(g)
# l = Alpha.items()
# print(l)


def replacer(x,z):
    for k, v in z.items():
        x = x.replace(k,v)
    return x

user_msg = input("Write your message here:").upper()
user_m = user_msg.split()
user = ' '.join(user_m)
user = user.replace(' ', SPACE7)
print(user)
print("Message after Coding:")
new_msg = replacer(user_msg , Alpha)
print(new_msg)

# ------------------------Experience--------------------------------
# Total Time = 3 hours and half.
# I found a struggle firstly with looping through the dictionary values.
# secondly, with replacing every letter in the msg.
# Lessons Learned:
# 1: Using new keywords: replace / join .
# 2: Splitting the problem into small pieces.
# 3: Smart search.
# Date: 19/2/2023
# ------------------------Experience--------------------------------
# Failed CODES
# for letter in Alpha:
#     new_letter = Alpha[letter]
#
# for user_letter in user_m:
#     res.append(Alpha[letter].get(user_letter,user_letter))
# res = ' '.join(res)
# print(res)
#     # print(new_letter)
#     x = "H"
#     y = "I"
#     if userl == lett:
#         # print(lett + " || " + new_letter)
#         m = userl.replace(userl , Alpha[letter])
#         print(m)
    # elif userl == lett:
    #     # print(lett + " || " + new_letter)
    #     mm = y.replace(y, Alpha[letter])
    #     print(mm)
    # for user_letter in user_msg:
    #     z = user_letter.replace(user_letter,Alpha[letter])
    #     print(z)

