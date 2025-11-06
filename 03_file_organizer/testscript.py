import os

source = "test_source"
os.makedirs(source, exist_ok=True)

# Create some dummy files
files = ["image1.jpg", "image2.png", "document1.txt", "music.mp3", "data.csv", "README"]
for file in files:
    with open(os.path.join(source, file), "w") as f:
        f.write("sample content")
print("Dummy files created.")
