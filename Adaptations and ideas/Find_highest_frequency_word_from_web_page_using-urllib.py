import urllib.request, urllib.parse, urllib.error

webhandle = urllib.request.urlopen('http://python.org')

counts = dict()
for line in webhandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
print(counts)
