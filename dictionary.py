def main():
    templist = []
    temp = {}
    sortedlist_PrPar = []
    sortedlist_NoAdj = []
    stringify = ""

    with open("dictionarylist.txt","r") as f:
        splits = f.read().split("\n")

    for i in splits:
        templist = [j.strip() for j in i.split(":")]
        print(templist[0])
        temp[templist[0]] = [templist[1],templist[2],templist[3]]
        sortedlist_NoAdj += templist[0]
    sortedlist_NoAdj.sort()
    count = 0
    # particles, pronouns, conj

    # nouns, adj, etc
    for i in sortedlist_NoAdj:
        print(sortedlist_NoAdj)
        stringify += f"<div class='dict-single'>\n\t<h1 class='word'>{i}</h1>\n\t<h3 class='pronun-type'>{temp[i][0]} . {temp[i][1]}</h2>\n"
        temptemp = [j.strip() for j in temp[i][2].split(",")]
        for j in temptemp:
            count+=1
            stringify += f"\t<h2 class='meaning'>{count}. {j}</h2>\n"
        stringify += "</div>\n"
    print("\n"+stringify)

# <div class='dict'>
#     <h1 class='word'>Word</h1>
#     <h3 class='pronun-type'>/wɜrd/ . noun</h2>
#     <h2 class='meaning'>a combination of one or more letters or sounds that symbolise or convey a distinct meaning</h2>
# </div>

if __name__ == "__main__":
    main()