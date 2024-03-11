waiting_list = ["sen", "ben", "john"]
# this method returns null, the sort is IN-PLACE
waiting_list.sort()
# waiting_list.sort(reverse=True) -> sort list in reverse alphabetic order

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)