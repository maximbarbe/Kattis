from collections import defaultdict
n, m = map(int, input().split())

# vertex: [out_deg, in_deg]
vertices = defaultdict(lambda: [0, 0])
for i in range(m):
    src, dest = map(int, input().split())
    vertices[src][0] += 1
    vertices[dest][1] += 1

start_vertex, end_vertex = None, None

for key, val in vertices.items():
    if val[0] != val[1]:
        if abs(val[0] - val[1]) > 1:
            print("no")
            exit()
        else:
            if val[0] > val[1]:
                if start_vertex == None:
                    start_vertex = key
                else:
                    print("no")
                    exit()
            else:
                if end_vertex == None:
                    end_vertex = key
                else:
                    print("no")
                    exit()
if not start_vertex and not end_vertex:
    print("anywhere")
else:
    print(start_vertex, end_vertex)