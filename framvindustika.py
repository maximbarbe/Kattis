from math import floor
import decimal
percent, w=  map(int, input().split())

completed_squares = floor((decimal.Decimal(percent)/100)*w)
print(f"[{'#' * completed_squares}{'-'*(w-completed_squares)}] |{' '*(4-len(str(percent)))}{percent}%")