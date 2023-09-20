row = 1
column = 1
muiltply = 1

for row in range(1,13):
    for column in range(1,21):
        muiltply = row * column

        print(f"{column:>2}  * {row:>2} = {muiltply: ^4}",end=" ")
        #print(column,"*",row,"=",muiltply,"\t", end=" " "\t")
    print()


