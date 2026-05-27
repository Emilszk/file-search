import os

path=""

while True:
    if not path:
        path=input("Enter folder path (Press enter = current directory): ")
        if path.strip()=="":
            path=os.getcwd()

    file=input("Enter file name: ")

    found=False
    count=0

    print(f"\nSearching for '{file}' in {path}...\n")

    for root, dirs, files in os.walk(path):
        for f in files:
            if file.lower() in f.lower():
                print("FOUND:", os.path.join(root,f))
                found=True
                count+=1

    if not found:
        print("File not found!")
    print(f"\nTotal matches: {count}")

    choice = input("\nDo you want to search again? (y/n): ")
    if choice.lower() != "y":
        print("Goodbye :)")
        break

    choice = input("\nDo you want to search in the same path? (y/n): ")
    if choice.lower() != "y":
        path=""

    print("\n" + "=" * 50)
    print("NEW SEARCH SESSION")
    print("=" * 50 + "\n")
