from zenml.client import Client
artifact = Client().get_artifact_version('4afb0fea-8a86-4db3-9dbf-e27f62b78a22')
loaded_artifact = artifact.load()
print(loaded_artifact)
