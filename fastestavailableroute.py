h,w,s=map(int,input().split());c=s
for i in range(h):c+=input().count('.')*s
print(f"Your destination will arrive in {c} meters")