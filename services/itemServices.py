from repository.repositoryItem import RepositoryItem
from services.mapper import mapItems
from domain.item import Item
from typing import Optional


class ItemServices:
    repoItem = RepositoryItem()

    def getItems(self):
        return mapItems(self.repoItem.getItems())

    def getItemById(self, ident: int):
        listItems = mapItems(self.repoItem.searchItemById(ident))
        return listItems[0]

    def searchItem(self, name: str):
        listItems = mapItems(self.repoItem.searchItem(name))
        try:
            return listItems[0]
        except Exception:
            return f"Item with name = {name} doesnt exist"

    def updateItem(self,
                   ident: int,
                   name: Optional[str] = None,
                   description: Optional[str] = None,
                   price: Optional[float] = None,
                   availability: Optional[int] = None):
        try:
            self.repoItem.updateItem(ident, name, description, price, availability)
            return True
        except Exception as e:
            print(f"Error updating item: {e}")
            return False

    def deleteItem(self, name: str):
        try:
            self.repoItem.deleteItem(name)
            return "Item deleted successfully"
        except Exception:
            print("Error deleting item")

    def createItem(self, item: Item) -> bool:
        try:
            self.repoItem.createItem(item)
            return True
        except Exception as e:
            print(f"Error adding item: {e}")
            return False

    def manageStock(self, name: str, availability: int, operator: str):
        return self.repoItem.manageStock(name, availability, operator)

    def statistics(self, statistic: str):
        return self.repoItem.statistics(statistic)
