import json

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as file:
    header_line = file.readline()
    head_column = header_line.strip().split("\t")

    movies = []
    for line in file:
        rows = line.strip().split("\t")

        movie = {}
        for index in range(len(head_column)):
                column_name = head_column[index]
                value = rows[index]  
                
                if column_name == "PRIMARYTITLE":
                    movie["Title"] = value
                elif column_name == "DIRECTOR":
                    movie["Director"] = value.split(",") if value else []
                elif column_name == "CAST":
                    movie["Cast"] = value.split(",") if value else []
                elif column_name == "GENRES":
                    movie["Genre"] = value.split(",") if value else []
                elif column_name == "STARTYEAR":
                    movie["Decade"] = value[:3] + "0" 

        movies.append(movie)


with open("netflix_movies.json", 'w', encoding="utf-8") as output_file:
    json.dump(movies, output_file, ensure_ascii=False, indent=4)
