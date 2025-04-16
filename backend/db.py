from motor.motor_asyncio import AsyncIOMotorClient
import os

def init_db():
    MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["testdb"]
    return {
<<<<<<< HEAD
        "items_collection": db["items_collection"],
        "users_collection": db["users_collection"]
=======
        "items_collection": db["item"],
        "users_collection": db["users"]
>>>>>>> d78737ca44aebbb43c528f6425ce1b3c85a49559
    }
    # Question for chocolate: How can we implement nosql syntax in mysql ???