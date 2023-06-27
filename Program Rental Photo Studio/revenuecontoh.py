
revtoday = [65,24,76,90]
def addFile(revenue,name):
    with open(revenue, 'w') as j:
        for i in name:
            j.write("%s\n" %str(i))
        #j.write("\n".join(str(i) for i in name))
    j.close()
addFile('revenue.txt',revtoday)