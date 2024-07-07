Result = [(i,j, i**3 + j**3) for i in range(1, 101) for j in range(1, 101)]

Result_dict = {}
for i in Result:
    Result_dict.setdefault(i[2], set([i[0], i[1]]))
    Result_dict[i[2]].add(i[0])
    Result_dict[i[2]].add(i[1])
    
[Result_dict.pop(key) for key in list(Result_dict.keys()) if len(Result_dict[key]) < 4]

print(sorted(Result_dict)[:5])