## IMPORTS GO HERE if required
import collections
## END OF IMPORTS 


#### YOUR CODE FOR uniqueEntries GOES HERE ####
def uniqueEntries(x):
    list = []
    for i in x:
        if i not in list:
            list.append(i)
    v = [item for item, count in collections.Counter(x).items() if count > 1]
    return(list,v)


#### End OF MARKER ----uniqueEntries



if __name__ == '__main__':
    uniqueEntries([12,24,35,24,88,120,155,88,120,155])
