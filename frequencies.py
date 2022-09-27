"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    newItems=[str(x) for x in items]
    frequencies = {}
    for x in newItems:
        frequencies[x]=newItems.count(x)
    # Your code goes here
    return frequencies