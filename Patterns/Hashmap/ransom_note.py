def ransom_note(note, magazine):

    magazine_letters = {}

    if len(magazine) < len(note):
        return False

    for j in magazine:
        if j not in magazine_letters:
            magazine_letters[j] = 0
        magazine_letters[j] += 1

    for i in note:
        if i in magazine_letters:
            magazine_letters[i] -= 1
            if magazine_letters[i] < 0:
                return False
    return True




if __name__ == "__main__":
    print(ransom_note("hello", "hellworld"))
    print(ransom_note("notes", "stoned"))
    print(ransom_note("apple", "pale"))