def counter(word):
    count = {}
    for char in word:
        count[char] = word.count(char)
    return count

print(counter("pythonpractice"))
