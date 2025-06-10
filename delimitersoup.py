s=[];p=lambda *x:print(*x);o=lambda:input();n=int(o());_=o();e=lambda:exit();m=lambda:s.pop()
for i in range(n):
    if _[i]==" ":continue
    if _[i] in "([{":s.append(_[i])
    else:
        if not s:p(_[i], i);e();
        else: 
            if _[i]=="}":
                if s[-1]!="{":p(_[i], i);e()
                else:m()
            elif _[i]=="]":
                if s[-1]!="[":p(_[i], i);e()
                else:m()
            else:
                if s[-1]!="(":print(f"{_[i]} {i}");e();
                else:m()
else:p('ok so far')