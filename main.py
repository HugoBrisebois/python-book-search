import requests

# Base Url 
Base_URL = "https://openlibrary.org/subjects"


# Getting Libraries
def get_Topics():
    URL = f"{Base_URL}/architecture.json"
    response = requests.get(URL)
    print(response)

    if response.status_code == 200:
        pass
    else:
        print(f"retrieval failed {response.status_code}")
get_Topics()

# Arriving program
print("Welcome To Your Book recommendation Center")
print("")
Topic = input("What Topic Are You interested in? (Comp Science Or Programming) ")

if Topic == "Comp Science" or "comp science":
    print("alright")



