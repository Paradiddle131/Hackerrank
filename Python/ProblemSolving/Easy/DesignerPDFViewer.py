import os

def designerPdfViewer(h, word):
    max=0
    for i in range(len(word)):
        if(max < h[ord(word[i])-97]):
            max = h[ord(word[i])-97]
    return max*len(word)

print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc'))

"""

def dict(list):
    for letter in list
    letterDict = {
        "ord('{}').format(letter)": "list",
    }

def designerPdfViewer(h, word):

print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc'))

"""