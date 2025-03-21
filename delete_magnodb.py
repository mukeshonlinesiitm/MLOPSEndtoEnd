from llm_engineering.domain.documents import ArticleDocument, UserDocument

user = UserDocument.get_or_create(first_name="Maxime", last_name="Labonne")
collection = ArticleDocument.get_collection_name()
print(f"collection_name: {collection}")
#Delete All Documents in a Collection
out = ArticleDocument.delete_all()

print(f"out : {out}")

#Drop an Entire Collection
#collection.drop()

#print("Collection dropped.")
