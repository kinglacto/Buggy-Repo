from fastapi import APIRouter, HTTPException
from models import Item
from bson import ObjectId

<<<<<<< HEAD
# Fixed router initialization - it was incorrectly defined as empty dict
router = APIRouter()
=======
router = {}
>>>>>>> d78737ca44aebbb43c528f6425ce1b3c85a49559

async def get_items_collection():
    from db import init_db
    return init_db()["items_collection"]

@router.get("/")
async def get_items():
    collection = await get_items_collection()
    items = []
    async for item in collection.find():
        item["_id"] = str(item["_id"])
        items.append(item)
    return items

@router.post("/")
async def create_item(item: Item):
    collection = await get_items_collection()
    result = await collection.insert_one(item.dict())
    return {"id": str(result.inserted_id)}

<<<<<<< HEAD
# Removed duplicate create_item function with the same path

# Simplified delete endpoint to use only one parameter
@router.delete("/{item_id}")
async def delete_item(item_id: str):
    collection = await get_items_collection()
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count:
        return {"status": "deleted"}
=======
@router.post("/")
async def create_item(item: Item):
    return {"id": "Item Inserted"}
# I want a chocolate
@router.delete("/{item_id}/{item_details}")
async def delete_item(item_id: str, item_details:str):
    collection = await get_items_collection()
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    result2 = await collection.delete_one({"_id": ObjectId(item_details)})
    if result.deleted_count:
        return {"status": "deleted", "deleted_item":result2}
>>>>>>> d78737ca44aebbb43c528f6425ce1b3c85a49559
    raise HTTPException(status_code=404, detail="Item not found")