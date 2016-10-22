
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
