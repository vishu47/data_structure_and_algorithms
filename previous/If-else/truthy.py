# making conversion with int or forcefully conversion will comes under explicit
# automatic conversion will be implicit
#

a = int("100")  # explicit

""""
1,2,4,,5,-1 -> truthy
0 -> Falsy
"adsadas", "dwd", ".", " " -> Truthy
"""

# name = " "
# name = "0"
# name = 90
name = 0

if name:
    print(True)
else:
    print(False)
