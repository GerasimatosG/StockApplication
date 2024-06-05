from fastapi import HTTPException
from domain.item import Item
from typing import Optional
from repository.databaseConnection import DBConnection
from services.mapper import mapItemsForAvailability


class RepositoryItem:
    repositoryPostgres = DBConnection()

    # INSERT ITEMS IN DB
    def createItem(self, item: Item):
        query = f"""INSERT INTO items (name,description,price,availability) VALUES
                ('{item.name}','{item.description}',{item.price},{item.availability})"""
        connection = self.repositoryPostgres.executeQuery(query)
        connection.close()

    # UPDATE ITEMS
    def updateItem(self,
                   ident: int,
                   name: Optional[str] = None,
                   description: Optional[str] = None,
                   price: Optional[float] = None,
                   availability: Optional[int] = None):
        try:
            query = "UPDATE items SET "

            columns = []
            if name is not None:
                columns.append(f"name = '{name}'")
            if description is not None:
                columns.append(f"description = '{description}'")
            if price is not None:
                columns.append(f"price = {price}")
            if availability is not None:
                columns.append(f"availability = {availability}")
            query += ", ".join(columns)
            query += f" WHERE id = {ident}"
            self.repositoryPostgres.executeQuery(query)
            return True
        except Exception as e:
            print(f"Error updating item: {e}")
            return False

    # SEARCH ITEMS WITH NAME
    def searchItem(self, name: str):
        query = f"SELECT * FROM items WHERE name = '{name}'"
        return self.repositoryPostgres.fetchData(query)

    # SEARCH ITEMS WITH ID
    def searchItemById(self, ident: int):
        query = f"SELECT * FROM items WHERE id = {ident}"
        return self.repositoryPostgres.fetchData(query)

    # SHOW ALL ITEMS
    def getItems(self):
        query = "SELECT * FROM items"
        return self.repositoryPostgres.fetchData(query)

    # DELETE ITEM WITH NAME
    def deleteItem(self, name: str):
        selectQuery = f"SELECT * FROM items WHERE name = '{name}'"
        selectResult = self.repositoryPostgres.fetchData(selectQuery)
        if selectResult is None or len(selectResult) == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            deleteQuery = f"DELETE FROM items WHERE name = '{name}'"
            return self.repositoryPostgres.executeQuery(deleteQuery)

    # UPDATE STOCK/AVAILABILITY BY NAME
    def getCurrentAvailability(self, name: str):
        item = mapItemsForAvailability(self.searchItem(name))
        return item.availability

    def manageStock(self, name: str, availability: int, operator: str):
        currentAvailability = self.getCurrentAvailability(name)
        currentAvailability = int(currentAvailability)
        newAvailability = 0
        if operator == "plus":
            newAvailability = availability + currentAvailability
        elif operator == "minus":
            if availability < currentAvailability:
                newAvailability = currentAvailability - availability
            elif availability > currentAvailability:
                raise HTTPException(status_code=400, detail="New availability cant be negative")
        else:
            return "Please enter a valid operator"

        updateQuery = f"UPDATE items SET availability = {newAvailability} WHERE name = '{name}'"
        self.repositoryPostgres.executeQuery(updateQuery)
        return "Stock updated successfully."

    # ITEM STATISTICS

    def statistics(self, statistic: str):
        if statistic == "Total Stock":
            query = "SELECT SUM(availability) FROM items"
            queryResults = self.repositoryPostgres.fetchData(query)
            totalAvailability = queryResults[0][0] if queryResults else 0
            return f"Total Stock of All items is {totalAvailability}"
        elif statistic == "Average Price":
            query = "SELECT AVG(price) FROM items"
            queryResults = self.repositoryPostgres.fetchData(query)
            averagePrice = queryResults[0][0] if queryResults else 0
            roundedAveragePrice = round(averagePrice, 2)
            return f"Average price for items is {roundedAveragePrice}"
        elif statistic == "Highest Price":
            queryPrice = "SELECT MAX(price) FROM items"
            queryPriceResults = self.repositoryPostgres.fetchData(queryPrice)
            maxPrice = queryPriceResults[0][0] if queryPriceResults else 0
            queryItem = f"SELECT name FROM items WHERE price = {maxPrice}"
            queryItemResults = self.repositoryPostgres.fetchData(queryItem)
            expensiveItem = queryItemResults[0][0]
            return f"Most expensive item is {expensiveItem} and costs {maxPrice}"
        else:
            raise HTTPException(status_code=404, detail="The statistic you searched for doesnt exist")
