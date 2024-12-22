import json

def access_point_key():
    with open('C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.9 (Matching JSON Pairs)/Security/data.json', 'r') as file:
        load = json.load(file)

    password = load['Gpassword']
    print(f"General_Password : {password}")
    instagram = load['instagram']
    print(f"Instagram : {instagram}")
    facebook = load['facebook']
    print(f"Facebook : {facebook}")
    whatsapp = load['whatsapp']
    print(f"Whatsapp : {whatsapp}")
    print("\n")