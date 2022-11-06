def dash_reader(file_name):
    total_pages = 0
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in enumerate(lines):
            sub_lines = line[1].split("--")
            print(sub_lines)

            total_pages += len(sub_lines)
            print(sub_lines[0].strip())
            print("Total Pages", total_pages)
            print("[enter - read more or put a number, press q to quit]")
            n = input()
            if n == "q":
                break
            else:
                current_page = 0
                while (True):
                    if current_page == total_pages - 1:
                        break
                    else:
                        if (len(n) == 0):  # if enter is pressed
                            current_page += 1
                            print(sub_lines[current_page].strip())
                        else:
                            num = int(n)
                            if num < 0:
                                current_page = (current_page - abs(num)) - 1
                            else:
                                current_page = current_page + num
                            if current_page < 0:
                                current_page = 0
                            if current_page >= len(sub_lines):
                                current_page = len(sub_lines) - 1
                            print(sub_lines[current_page].strip())
                        print(
                            "[enter - read more or put a number, press q to quit]"
                        )

                        n = input()
                        if n == "q":
                            break