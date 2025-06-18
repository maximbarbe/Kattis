from collections import defaultdict
from string import ascii_letters
translation = defaultdict(lambda el: el)
translation["Á"] = "a"
translation["á"] = "a"
translation["Ð"] = "d"
translation["ð"] = "d"
translation["É"] = "e"
translation["é"] = "e"
translation["Í"] = "i"
translation["í"] = "i"
translation["Ó"] = "o"
translation["ó"] = "o"
translation["Ú"] = "u"
translation["ú"] = "u"
translation["Ý"] = "y"
translation["ý"] = "y"
translation["Þ"] = "th"
translation["þ"] = "th"
translation["Æ"] = "ae"
translation["æ"] = "ae"
translation["Ö"] = "o"
translation["ö"] = "o"
s = input()
res = ""
for char in s:
    if char in ascii_letters or char in "0123456789":
        res += char.lower()
    else:
        if char in translation.keys():
            res += translation[char]
print(res +".is")