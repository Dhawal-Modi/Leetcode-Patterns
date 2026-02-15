def isAnagram(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}

    for i in s:
        if i not in s_dict:
            s_dict[i] = 0
        s_dict[i] += 1

    for k in t:
        if k not in t_dict:
            t_dict[k] = 0
        t_dict[k] += 1

    if t_dict == s_dict:
        return True
    return False



if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat","car"))