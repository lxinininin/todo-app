import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

# ex: if we would like to search python website
# the URL is "https://google.com/search?q=python+website"
webbrowser.open("https://google.com/search?q=" + user_term)