import sys
from matplotlib import pyplot
'''
Pass a file path and this simple method will create a dictionary of lists for each column
in the dataset
'''
def readData(file):
    f = open(file,'r')
    readHeader = False

    data = {'category' : [], 'brand': [], 'name' : [], 'price' : [], 'rating' : [], 'model' : [], 'weight' :[],
            'product_id' : [], 'url' : []}

    for line in f:
        if not readHeader:
            readHeader = True
            continue
        split = line.split(',')
        data['category'].append(split[0])
        data['brand'].append(split[1])
        data['name'].append(split[2])
        data['price'].append(split[3])
        data['rating'].append(split[4])
        data['model'].append(split[5])
        data['weight'].append(split[6])
        data['product_id'].append(split[7])
        data['url'].append(split[8])
    return data
'''
Returns a tuple of (missing,total)
for specified data and column name
'''
def missingValues(data, column_name):
    missing = 0
    total = 0
    if column_name in data:
        list = data[column_name]
        total = len(list)
        for val in list:
            if val is '':
                missing +=1

    else:
        return (-1,-1)
    return (missing, total)


'''
Returns a tuple of the (min, average, max) string lengths of the
specified datamatrix and column. (Note strings of length 0 are not
considered)
'''
def stringLengthSummary(data, column_name):
    total = 0
    minlen = sys.maxint
    maxlen = -sys.maxint - 1
    notMissing = 0
    if column_name in data:
        for str in data[column_name]:
            if not str is '':
                notMissing += 1
                minlen = min(minlen,len(str))
                maxlen = max(maxlen, len(str))
                total += len(str)
        return (minlen, total / notMissing, maxlen)
    else:
        return (-1,-1,-1)

def stringLengthHistogram(data, column_name, num_bins):
    lengths = []
    if column_name in data:
        for str in data[column_name]:
            if not str is '':
                lengths.append(len(str))
        pyplot.hist(lengths,label=column_name,bins=num_bins)
        pyplot.show()

def missingComparison(data, missingCol, compareCol):
    compare = []

    if missingCol in data and compareCol in data:
        zipped =  zip(data[missingCol], data[compareCol])
        for pair in zipped:
            if pair[0] is '':
                compare.append(pair[1])
    return compare


