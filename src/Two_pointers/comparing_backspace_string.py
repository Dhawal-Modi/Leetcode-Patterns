def compare(str1, str2):
    # TODO: Write your code here

    idx1, idx2 = len(str1) - 1, len(str2) - 1
    while idx1 >= 0 or idx2 >= 0:
        i1 = backspace(str1, idx1)
        i2 = backspace(str2, idx2)
        if i1 < 0 and i2 < 0:
            return True
        elif i1 < 0 or i2 < 0:
            return False
        elif str1[i1] != str2[i2]:
            return False

        idx1 = i1 - 1
        idx2 = i2 - 1
    return True
def backspace(s, idx):

    count = 0
    while idx >= 0:
        if s[idx] == "#":
            count += 1
        elif count > 0:
            count -= 1
        else:
            break

        idx -= 1
    return idx

if __name__ == "__main__":
    #print(compare("xp#","xzy##"))
    #print(compare("xywrrmp", "xywrrmu#p"))
    #print(compare("a##c", "#a#c"))
    #print(compare("ab##", "c#d#"))
    #print(compare("ab#c", "ad#c"))
    print(compare("bbbextm", "bbb#extm"))



