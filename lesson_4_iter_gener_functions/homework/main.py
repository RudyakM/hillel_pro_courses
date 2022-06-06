filename = "rockyou.txt"
search_keyboard = "user"
result = []


def read_lines() -> list:
    with open(filename, encoding="utf8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if search_keyboard in line:
                user_input = input(
                    f"You want add --> {line}in results (y/n) or (skip all): "
                )
                if user_input == "y":
                    yield line.replace("\n", "")
                elif user_input == "skip all":
                    break
                else:
                    continue


for line in read_lines():
    result.append(line)
print("\n========================================================\n")
print(f"Results: {result}\n\nThe amount of added lines: {len(result)}")
print("\n========================================================\n")
