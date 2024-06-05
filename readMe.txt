to show all Items : /showAll/

to create new item : /addItem/ + JSON like this 
{
    "name" : "Iphone",
    "description": "mobile phone",
    "price": 150,
    "availability": 12
}

to update item WITH URL : /updateItemURL/{ident}==(id of item you want to update after endpoint) 
update it by adding key - value after {ident}

to update item WITH JSON : /updateItemJSON/{ident} ==(id of item you want to update after endpoint) 
update it by adding a json object in raw(can only add the value you want,no need to write the whole object)

to delete item : /deleteItem/ and pass the name as a key - value pair of the object you want to delete

to search specific item : /searchItem/ and pass the name as a key - value pair of the object you want to search

to update the stock availability : /updateStock/{name}=={name of item whose availability you want to update}
In key - values pass "plus" to increase the availability or "minus" to decrease it.Then pass availability - the number you want to be added or substracted

to get statistics: /statistic/
In key - values you can pass : statistic - Total Stock to get the availability of all items 
			       statistic - Average Price to get the avarage price of the items in database
			       statistic - Highest Price to get the product with the highest price	