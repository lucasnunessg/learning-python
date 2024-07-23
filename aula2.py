clubs_favorite_file = open("clubs-favorite.txt", mode="w")


clubs_favorite_file.write("Grêmio Football Porto Alegrense\n")
clubs_favorite_file.write("Manchester City Football Club\n")

print("SV Darmstadt", file=clubs_favorite_file)

more_clubs = ["EC São Gabriel\n"]

clubs_favorite_file.writelines(more_clubs)

clubs_favorite_file.close()
