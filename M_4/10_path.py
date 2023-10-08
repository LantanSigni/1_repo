from pathlib import Path

p = Path(r'C:\Users\grebe\Downloads')
for i in p.iterdir():
    print(i.name)
