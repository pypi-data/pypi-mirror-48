# List Slicer
This library has a function to split the data list into several small sections

## Usage
Use the following code to split your list data

### Split List data
```
from listslicer.slicer import Slicer

#My list data
data = [
    200, 1230, 15, 2200, 5550
]
#2 is amount to split
data_slice = Slicer.cut(data, 2)
print(data_slice)
```
### Result
```
[[200, 1230], [15, 2200], [5550]]
```

## Example to split Dictionary
```
data = [
    {
        "foodname": "Ayam Bakar",
        "price": 12000
    }, 
    {
        "foodname": "Jus Mangga",
        "price": 7000
    },
    {
        "foodname": "Mie Goreng",
        "price": 9000
    },
    {
        "foodname": "Chicken Katsu",
        "price": 15000
    },
]
print(slicer.cut(data, 2))
```
### Result 
```
[
    [{'price': 12000, 'foodname': 'Ayam Bakar'}, {'price': 7000, 'foodname': 'Jus Mangga'}], 
    [{'price': 9000, 'foodname': 'Mie Goreng'}, {'price': 15000, 'foodname': 'Chicken Katsu'}]
]
```