import sys

unique = {"A", "B", "C", "D", "E", "F", "G"}
conversion = {
    "A#": "Bb",
    "C#": "Db",
    "D#": "Eb",
    "F#": "Gb",
    "G#": "Ab"
    }
reverse = {value:key for key, value in conversion.items()}
case = 0
for line in sys.stdin:
    case += 1
    data= line.strip("\n").split(" ")
    if data[0] in unique:
        print(f"Case {case}: UNIQUE")
    else:
        if data[0] in conversion.keys():
            opposite = conversion[data[0]]
        else:
            opposite = reverse[data[0]]
        print(f"Case {case}: {opposite} {data[1]}")