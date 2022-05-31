str1 = "in publishing and graphic design"
while str1 != "":
    str1len1 = len(str1)
    ch = str1[0]
    str1 = str1.replace(ch, "")
    str2len2 = len(str1)
    if str2len2 == str1len1 - 1:
        print("First unique character is: ", ch)
        break
