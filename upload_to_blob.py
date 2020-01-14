import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

block_blob_service = BlockBlobService(account_name='terrastatefile', account_key='P4D8mPNPRUsB1SJuQkWBjtDndh12GAZA8KuWvT4SMfqx3rf/3bifpTeoNkU9mp4GxZL2BiDdBYxAh0+lfUOBVA==')

# Create a container called 'featureflagconfig'.
container_name ='featureflagconfig'
block_blob_service.create_container(container_name)

# blob permission
block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

# test the upload
local_path=os.path.abspath(os.path.curdir)
local_file_name =input("Enter file name to upload : ")
full_path_to_file =os.path.join(local_path, local_file_name)
print("Temp file = " + full_path_to_file)
print("\nUploading to Blob storage as blob " + local_file_name)
# Upload the created file, use local_file_name for the blob name
block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)
# List the blobs in the container
print("\nList blobs in the container")
generator = block_blob_service.list_blobs(container_name)
for blob in generator:
    print("\t Blob name: " + blob.name)

