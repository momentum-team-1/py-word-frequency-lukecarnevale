STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

Text = 'seneca_falls.txt'

for char in '-.,/n':
    Text=Text.replace(char,' ')
Text = Text.lower

print(Text)

word_list = Text.split()
print(word_list)

d = {}

for word in word_list:
    d[word] = d.get(word, 0) + 1

# for word in word_list:
#     if word not in d:
#         d[word] = 0
#     d[word] += 1

word_freq = []
for key, value in d.items():
    word_freq.append((value,key))
word_freq

word_freq.sort(reverse = True)
print(word_freq)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
