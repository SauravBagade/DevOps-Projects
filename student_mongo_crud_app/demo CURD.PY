import pymongo

# ✅ 1️⃣ Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# ✅ 2️⃣ Create or connect to a database
db = client["mydb"]

# ✅ 3️⃣ Create or connect to a collection
mycol = db["student"]

# -------------------------------------------
#  # 🟢 CREATE (Insert)
# # -------------------------------------------

# # Insert ONE document
one_doc = {"name": "Saurav", "last_name": "Bagade", "marks": [85, 90, 75]}
x = mycol.insert_one(one_doc)
print("✅ One document inserted with ID:", x.inserted_id)

# Insert MANY documents
many_docs = [
    {"name": "Amit", "last_name": "Patil", "marks": [65, 70, 80]},
    {"name": "Rohit", "last_name": "Sharma", "marks": [88, 92, 95]},
    {"name": "Sneha", "last_name": "Joshi", "marks": [77, 82, 89]}
]
y = mycol.insert_many(many_docs)
print("✅ Many documents inserted with IDs:", y.inserted_ids)

# -------------------------------------------
# 🔵 READ (Find)
# -------------------------------------------

# Find ONE document (first match)
one_result = mycol.find_one()
print("\n📄 One Document:", one_result)

# Find ALL documents
print("\n📄 All Documents:")
for data in mycol.find():
    print(data)

# Find with condition
print("\n📄 Students with name='Saurav':")
for data in mycol.find({"name": "mayur"}):
    print(data)

# -------------------------------------------
# 🟠 UPDATE
# -------------------------------------------

# Update ONE document
update_one = mycol.update_one(
    {"name": "Saurav"},             # Filter condition
    {"$set": {"marks": [99, 98, 97]}}  # New value
)
print("\n✏️ One document updated count:", update_one.modified_count)

# Update MANY documents
update_many = mycol.update_many(
    {"last_name": "Patil"},
    {"$set": {"marks": [100, 100, 100]}}
)
print("✏️ Many documents updated count:", update_many.modified_count)

# -------------------------------------------
# 🔴 DELETE
# -------------------------------------------

# Delete ONE document
delete_one = mycol.delete_one({"name": "Rohit"})
print("\n🗑️ One document deleted count:", delete_one.deleted_count)

# Delete MANY documents
delete_many = mycol.delete_many({"marks": [100, 100, 100]})
print("🗑️ Many documents deleted count:", delete_many.deleted_count)

# -------------------------------------------
# 🧾 Display remaining documents
# -------------------------------------------

print("\n📦 Remaining documents in collection:")
for data in mycol.find():
    print(data)
