from typing import Optional
from fastapi import APIRouter, HTTPException
from domain.itemBaseModel import ItemBaseModel
from domain.item import Item
from services.itemServices import ItemServices

router = APIRouter()


# CREATE ITEMS
@router.post('/addItem/', response_model=None)
async def addItem(itemData: dict):
    try:
        service = ItemServices()
        item = Item(**itemData)
        result = service.createItem(item)
        if result:
            return {"message": "Item added successfully"}
        else:
            return {"message": "Failed to add item"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# SHOW ALL ITEMS
@router.get("/showAll/")
async def getAllItems():
    service = ItemServices()
    return service.getItems()


# UPDATE ITEMS BOTH WITH JSON AND URL
@router.put("/updateItemJSON/{ident}")
async def updateItem(ident: int, itemData: ItemBaseModel):
    service = ItemServices()
    try:
        existingItem = service.getItemById(ident)
        if existingItem:
            if service.updateItem(ident, **itemData.dict()):
                return {"message": "Item updated successfully"}
            else:
                raise HTTPException(status_code=500, detail="Failed to update item")
    except Exception:
        raise HTTPException(status_code=404, detail=f"Item with id {ident} not found")


@router.put("/updateItemURL/{ident}")
async def updateItem(ident: int,
                     name: Optional[str] = None,
                     description: Optional[str] = None,
                     price: Optional[float] = None,
                     availability: Optional[int] = None):
    service = ItemServices()
    try:
        existingItem = service.getItemById(ident)
        if existingItem:
            if service.updateItem(ident, name, description, price, availability):
                return {"message": "Item updated successfully"}
            else:
                raise HTTPException(status_code=500, detail="Failed to update item")
    except Exception:
        raise HTTPException(status_code=404, detail=f"Item with id {ident} not found")


# DELETE ITEMS
@router.delete('/deleteItem/', response_model=None)
async def deleteItem(name: str):
    service = ItemServices()
    return service.deleteItem(name)


# SEARCH ITEMS
@router.get('/searchItem/')
async def searchItem(name: str):
    try:
        service = ItemServices()
        return service.searchItem(name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# STOCK MANAGEMENT
@router.patch('/updateStock/{name}')
async def manageStock(name: str, availability: int, operator: str):
    service = ItemServices()
    return service.manageStock(name, availability, operator)


# GET STATISTICS
@router.get('/statistic/')
async def getStatistics(statistic: str):
    service = ItemServices()
    return service.statistics(statistic)
