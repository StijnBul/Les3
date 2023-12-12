import webbrowser

personage=str(input("Welke personnage wil je zien?"))
url = "https://rickandmortyapi.com/api/character/?name=" + personage

webbrowser.open(url)
