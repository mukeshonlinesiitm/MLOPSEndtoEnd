from llm_engineering.domain.documents import ArticleDocument, UserDocument

user = UserDocument.get_or_create(first_name="Maxime", last_name="Labonne")
articles = ArticleDocument.bulk_find(author_id=str(user.id))
collection_name = ArticleDocument.get_collection_name()
print(f"collection_name: {collection_name}")
#print(f"articles: {articles}") Maxime Labonne

print(f"User ID: {user.id}")
print(f"User name: {user.first_name} {user.last_name}")
print(f"Number of articles: {len(articles)}")
for i in range(len(articles)):
    print(f"{i} article link: {articles[i].link}")
    print(f"{i} article content:  {articles[i].content}") 