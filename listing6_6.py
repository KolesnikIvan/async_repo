"""MapReduce technology example"""
import functools

def map_frequency(text: str):
    words_list = text.split()
    frequencies = dict()
    for word in words_list:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

def merge_dicts(first: dict, second: dict):
    merged = first
    for word in second:
        if word in merged:
            merged[word] += second[word]
        else:
            merged[word] = second[word]
    return merged

lines = [
    "I know what I know.",
    "I know that I know.",
    "I don't know that much.",
    "They don't know much."
]

mapped_results = list()
for line in lines:
    mapped_results.append(map_frequency(line))

result = [functools.reduce(merge_dicts, mapped_results)]
print(result)
