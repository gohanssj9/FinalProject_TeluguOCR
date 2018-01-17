#Write all telugu characters to Html file.

import itertools

a_aa = [i for i in range(3077,3093)]
a_aa.append(3168)
a_aa.append(3169)
a_aa.remove(3085)
a_aa.remove(3089)

k_kha = [i for i in range(3093,3130)]
k_kha.remove(3113)
k_kha.remove(3124)

vattu = [3073]
for i in range(3134,3159):
    vattu.append(i)
vattu.remove(3141)
vattu.remove(3145)

vattu.append(3074)
vattu.append(3075)
for i in range(3150,3157):
    vattu.remove(i)

#generate combinations:

all_comb = []
for i in k_kha:
    for j in vattu:
        if j == 3073:
            all_comb.append([i])
        else:
            all_comb.append([i,j])

actual_string = ""
for i in a_aa:
    dummy = "&#"+str(i)+";"
    actual_string = actual_string + dummy + "&#32"
actual_string = actual_string + "&#3077;&#3074;&#32;&#3077;&#3075"

actual_string = actual_string + "<br>"

c = 0
for i in all_comb:
    if len(i) == 2:
        dummy = "&#"+str(i[0])+";"
        dummy = dummy + "&#"+str(i[1])+";"
        actual_string = actual_string + dummy + "&#32"
    else:
        dummy = "&#"+str(i[0])+";"
        actual_string = actual_string + dummy + "&#32"
    c += 1
    if c == 19:
        c = 0
        actual_string = actual_string + "<br>"

actual_string = actual_string + "<br>"

print actual_string

html_file = open("initial.html","w")
html_file.write(actual_string)
html_file.close()

