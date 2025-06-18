notes = {
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "A#": ["A#", "C", "D", "D#", "F", "G", "A"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "C#": ["C#", "D#", "F", "F#", "G#", "A#", "C"],
    "D": ["D", "E", "F#", "G",  "A", "B", "C#"],
    "D#": ["D#", "F", "G", "G#", "A#", "C", "D"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "F": ["F", "G", "A", "A#", "C", "D", "E"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "F"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    "G#": ["G#", "A#", "C", "C#", "D#", "F", "G"]
}
n = int(input())
letters = input().rstrip(" ").split(" ")
res = []
for key, val in notes.items():
    for i in range(len(letters)):
        if letters[i] not in val:
            break
    else:
        res.append(key)
print("none" if len(res) == 0 else " ".join(res))