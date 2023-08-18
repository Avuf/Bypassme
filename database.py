import motor.motor_asyncio

DATABASE_URI = "mongodb+srv://LINKBYPASSER:LINKBYPASSER@cluster0.1z2z5gw.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"


class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.req_one = self.db.reqs_a
        self.req_two = self.db.reqs_b

    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
            ban_status=dict(
                is_banned=False,
                ban_reason="",
            ),
        )
    
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return bool(user)
    
    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})
    

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def get_db_size(self):
        return (await self.db.command("dbstats"))['dataSize']

    async def add_req_one(self, user_id):
        try:
            await self.req_one.insert_one({"user_id": int(user_id)})
            return
        except:
            pass
        
    async def add_req_two(self, user_id):
        try:
            await self.req_two.insert_one({"user_id": int(user_id)})
            return
        except:
            pass

    async def get_req_one(self, user_id):
        return await self.req_one.find_one({"user_id": int(user_id)})

    async def get_req_two(self, user_id):
        return await self.req_two.find_one({"user_id": int(user_id)})

    async def delete_all_one(self):
        await await self.req_one.delete_many({})

    async def delete_all_two(self):
        await await self.req_two.delete_many({})
        
db = Database(DATABASE_URI, DATABASE_NAME)
