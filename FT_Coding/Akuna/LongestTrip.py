def process(line: str) -> str:
    line_data = line.split(":")
    if line_data[0] in city.keys():
        city[line_data[0]][line_data[1]] = int(line_data[2])
    else:
        city[line_data[0]] = {}
        city[line_data[0]][line_data[1]] = int(line_data[2])

    if line_data[1] in city.keys():
        city[line_data[1]][line_data[0]] = int(line_data[2])
    else:
        city[line_data[1]] = {}
        city[line_data[1]][line_data[0]] = int(line_data[2])
    
    if len(city) >= 3:
        c1, c2, c3 = "", line_data[0], line_data[1]
        c2_cities = city[c2].copy()
        c2_cities.pop(c3)
        c1 = max(c2_cities, key=c2_cities.get)
        c1, c3 = sorted([c1, c3])

        dt = city[c1][c2] + city[c2][c3]
        return ":".join([str(dt), c1, c2, c3])
    else:
        return "NONE"
