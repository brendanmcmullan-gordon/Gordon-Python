season = input("Please enter the name of a season in Proper Case")

if (season == "Summer"):
    print("December, January and February are in", season)
else:
    if (season == "Autumn"):
        print("March, April and May are in", season)
    else:
        if (season == "Winter"):
            print("June, July and August are in", season)
        else:
            if (season == "Spring"):
                print("September, October and November are in", season)
            else:
                print("Please enter a valid season in Proper Case")
