import requests


def menu():#Function to display menu options  

 counter = 0
 while counter == 0:
    #Menu display for choice
    print("--------------------------------------------------------------")
    print("Check Website")
    print("--------------------------------------------------------------")
    print("[1] Check Website")
    print("[2] Exit Programm")
    
    try:#Error handling
     choice = int(input("\nYour choice: "))
     if choice == 1:
        url = input("Enter the site URL: ")
        check_website(url)
     elif choice == 2:
         counter = choice
         print("\nClosing program...")
         exit() 
     else:
         print("❌ This option is not in the menu; please try again with an option that is in the menu.")
    except ValueError:#Treatment for incorrect choice
        print("Value not accept try again")

def check_website(url):#Function for check website
    try:#Error handling
        response = requests.get(url, timeout=5) 
        if response.status_code == 200:
            print(f"✅ {url} is online!")
        else:
            print(f"⚠️ {url} responded with code {response.status_code}.")
    except requests.ConnectionError:#Handling connection errors
        print(f"❌ {url} is of the air (connection error).")
    except requests.Timeout:#Handling for timeout error
        print(f"⏰{url} response time exceeded.")
    except Exception as e:
        print(f"⚙️ Unknown error while verifying URL. {url}:{e}")    


#Testing program
testing = menu()
print(testing)
