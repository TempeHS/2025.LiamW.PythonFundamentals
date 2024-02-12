file = input("Upload File: ")
File = file.strip().lower()

if File.endswith(".gif"):
    print("image/gif")
elif File.endswith(".jpeg") | File.endswith(".jpg"):
    print("image/jpeg")
elif File.endswith(".png"):
    print("image/apng")
elif File.endswith(".pdf"):
    print("application/pdf")
elif File.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
