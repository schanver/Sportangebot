import bot  
tage = ["montag","dienstag","mittwoch","donnerstag","freitag"]
def main():
    print("Für welchen Tag möchten Sie eine Reservation machen?")
    print("1. Montag")
    print("2. Dienstag")
    print("3. Mittwoch")
    print("4. Donnerstag")
    print("5. Freitag")

    while True:
        choice = str(input("Bitte geben Sie Ihre Auswahl ein: "))
    
        if choice.lower() in tage:
            print("Danke für Ihre Auswahl...")
            bot.book_a_reservation(choice.lower())
            break
        else:
            return "Bitte geben Sie den Tag, an denen Sie eine Reservation machen wollen!"
main()
