def vowel_count(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def main():
    print("Test -> ", vowel_count(text='Test'))
    print("Python ->", vowel_count(text='Python'))
    print("Kvaratskhelia ->", vowel_count(text='Kvaratskhelia'))


if __name__ == "__main__":
    main()
