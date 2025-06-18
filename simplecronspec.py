n = int(input())
times = [0 for i in range(86400)]
for i in range(n):
    data = input().split(" ")
    h = data[0]
    m = data[1]
    s = data[2]
    if h == "*":
        hours = [j for j in range(0, 24)]
    else:
        if "," in h:
            hours = []
            data = h.split(",")
            for t in data:
                if "-" in t:
                    start, end = map(int, t.split("-"))
                    hours += [j for j in range(start, end + 1)]
                else:
                    hours.append(int(t))
        else:
            if "-" in h:
                start, end = map(int, h.split("-"))
                hours = [j for j in range(start, end + 1)]
            else:
                hours = [int(h)]
    if m == "*":
        minutes = [j for j in range(0, 60)]
    else:
        if "," in m:
            minutes = []
            data = m.split(",")
            for t in data:
                if "-" in t:
                    start, end = map(int, t.split("-"))
                    minutes += [j for j in range(start, end + 1)]
                else:
                    minutes.append(int(t))
        else:
            if "-" in m:
                start, end = map(int, m.split("-"))
                minutes = [j for j in range(start, end + 1)]
            else:
                minutes = [int(m)]
    if s == "*":
        seconds = [j for j in range(0, 60)]
    else:
        if "," in s:
            seconds = []
            data = s.split(",")
            for t in data:
                if "-" in t:
                    start, end = map(int, t.split("-"))
                    seconds += [j for j in range(start, end + 1)]
                else:
                    seconds.append(int(t))
        else:
            if "-" in s:
                start, end = map(int, s.split("-"))
                seconds = [j for j in range(start, end + 1)]
            else:
                seconds = [int(s)]
    for h in hours:
        for m in minutes:
            for s in seconds:
                times[3600*h + 60*m + s] += 1
starts = 0
total = 0
for i in range(86400):
    if times[i] != 0:
        starts += 1
        total += times[i]
print(starts, total)