n, q = map(int, input().split())
books = []
conversion = {}
for i in range(n):
    book, author = input().split(", ")
    books.append((author, book))
books.sort(key=lambda el: (el[0],el[1]))
for i in range(len(books)):
    conversion[books[i][1]] = i + 1
    
for i in range(q):
    print(conversion.get(input(), -1))