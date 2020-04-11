# Travel Distance
def process(line: str) -> str:
    line_data = line.split(":")
    if line_data[0] == "LOC":
        # Replace city with self.city
        city[line_data[1]] = (radians(float(line_data[2])), radians(float(line_data[3])))
        # print("line_data -", line_data)
        # print("city -", city)
        return line_data[1]
    elif line_data[0] == "TRIP":
        dt = 0
        c1, c2 = line_data[2], line_data[3]
        d_psi = abs(city[c1][1] - city[c2][1])
        d_sigma = acos(sin(city[c1][0])*sin(city[c2][0]) + cos(city[c1][0])*cos(city[c2][0])*cos(d_psi))
        dt = RADIUS_MILES * d_sigma
        line_data.append(str(floor(dt)))
        # print("line_data -", line_data)
        # print("city -", city)
        return ":".join(line_data[1:])
    pass