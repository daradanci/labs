data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

print(sorted((data.copy()),key=abs, reverse=True))
print((lambda x: sorted((x),key=abs, reverse=True))(data.copy()))