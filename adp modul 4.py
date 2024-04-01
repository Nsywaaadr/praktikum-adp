print('Nama: Nasywa Adila Rahma')
print('Nim: 2310433022')
print('SHIFT-2')
print('-------------------------------')
lyric = "To make, to make sure you never left"

lyric = lyric.lower()

vowels = 'aeiou'
for vowel in vowels:
    lyric = lyric.replace(vowel, 'i')

print(lyric)