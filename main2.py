user_prompt = "Enter a todo:"

todos = []

while True:
    todo = input(user_prompt)
    # we can use the Console and type dir() to know the methods of the object
    # ex: dir(str) or dir("hello") output the methods of String
    # ex: dir(list) or dir([]) output the methods of List
    # and if we would like to know the specific meaning of one method of the object, we can type help() in Console
    # ex: help(str.capitalize) output the specific meaning of the capitalize method of String
    # ex: help(list.append) output the specific meaning of the append method of List
    print(todo.capitalize())
    todos.append(todo)
    print(todos)