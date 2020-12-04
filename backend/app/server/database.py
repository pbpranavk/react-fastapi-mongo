import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.simple_db

simple_collection = database.get_collection("simple_db_collection")


def simple_helper(simple_obj) -> dict:
    return {"id": str(simple_obj["_id"]), "item": simple_obj["item"]}


async def retrieve_simple_objects():
    objs = []
    async for obj in simple_collection.find():
        objs.append(simple_helper(obj))
    return objs


async def add_obj(simple_obj_data: dict) -> dict:
    obj = await simple_collection.insert_one(simple_obj_data)
    new_obj = await simple_collection.find_one({"_id": obj.inserted_id})
    return simple_helper(new_obj)


async def retrieve_obj(id: str) -> dict:
    obj = await simple_collection.find_one({"_id": ObjectId(id)})
    if obj:
        return simple_helper(obj)


async def update_obj(id: str, data: dict):
    if len(data) < 1:
        return False
    obj = await simple_collection.find_one({"_id": ObjectId(id)})

    if obj:
        updated_obj = await simple_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_obj:
            return True
        return False


async def delete_obj(id: str):
    obj = await simple_collection.find_one({"_id": ObjectId(id)})
    if obj:
        await simple_collection.delete_one({"_id": ObjectId(id)})
        return True
