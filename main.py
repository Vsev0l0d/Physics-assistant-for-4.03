table = []
file = open('input.csv', "r")
for line in file.readlines():
    table.append([float(j) for j in line.replace(",", ".").split(";")])
file.close()

waiting_for_a_min = True
r_light = [""]
r_dark = []
v_max = []
v_min = []
for i in range(2, 1000):
    if waiting_for_a_min:
        if table[i][1] > table[i - 1][1]:
            r_dark.append(table[i - 1][0])
            v_min.append(table[i - 1][1])
            waiting_for_a_min = False
    else:
        if table[i][1] < table[i - 1][1]:
            r_light.append(table[i - 1][0])
            v_max.append(table[i - 1][1])
            waiting_for_a_min = True

r = []
for i in range(min(len(r_dark), len(r_light) - 1)):
    r.append(r_dark[i] + (r_light[i + 1] - r_dark[i]) / 2)

while len(v_min) != len(r):
    v_min.pop()
while len(v_max) != len(r):
    v_max.pop()


def level_lists(list_1, list_2):
    while len(list_2) != len(list_1):
        if len(list_2) < len(list_1):
            list_2.append("")
        else:
            list_1.append("")


level_lists(r_dark, r_light)
level_lists(r_dark, r)
level_lists(r, v_min)
level_lists(r, v_max)

file = open("table.csv", "w")
file.write("r_dark;r_light;;r;v_max;v_min" + ' \n')
for i in range(len(r_dark)):
    line = str(r_dark[i]).replace(".", ",") + ";" + str(r_light[i]).replace(".", ",")
    line += ";;" + str(r[i]).replace(".", ",")
    line += ";" + str(v_max[i]).replace(".", ",") + ";" + str(v_min[i]).replace(".", ",")
    file.write(line + ' \n')
file.close()
