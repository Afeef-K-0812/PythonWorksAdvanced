# json File Operations
#import json

# 1. Read json file

#import json                     # To read json files import json first

#f=open('products.json','r')
#content=json.load(f)            # Use json.load to read full content, if json.read used read as string can't access index
#print(content)


# Write json file

#import json

#data=[
#    {"name":"Arun","age":20},
#    {"name":"Amal","age":23}
#]

#f=open('data.json','w')
#json.dump(data,f)