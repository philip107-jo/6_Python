print(f"'100'--> {int('100')}")
print(f"'3.14'--> {float('3.14')}")
print(f"'3.14'--> {int(float('3.14'))}")

falsy_values = [0, 0.0, "", [], (), {}, set(), None, False]
truthy_values = [1, -1, "0", "False", [0], " "]

print(" == falsy (거짓으로 취급되는 값) == ")
for v in falsy_values:
    print(f"{str(v):<10} -> {bool(v)}")
print("== truthy (참으로 취급되는값)==")
for v in truthy_values:
    print(f"{str(v):<10} -> {bool(v)}")
