def vacuum_cleaner():
    rooms = {
        "A": "Dirty",
        "B": "Dirty"
    }

    obstacles = {
        "A": True,
        "B": True
    }

    model = {
        "A": "Unknown",
        "B": "Unknown"
    }

  
    location = "A"

    while True:
        print("Current Room:", location)

        if obstacles[location]:
            print("Obstacle detected")
            obstacles[location] = False
            location = "B" if location == "A" else "A"
            print("Moving to:", location)
            continue

        model[location] = rooms[location]

        if rooms[location] == "Dirty":
            print("Action: SUCK")
            rooms[location] = "Clean"
            model[location] = "Clean"
        else:
            location = "B" if location == "A" else "A"
            print("Moving to:", location)

        if rooms["A"] == "Clean" and rooms["B"] == "Clean":
            print("Both rooms are clean")
            break


vacuum_cleaner()
