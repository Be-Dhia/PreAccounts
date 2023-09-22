print("""
    Hello Add Welcome To PreAcounts
    the new Way to Skip THe signup Problems
    and enjoy the full experience by sharing cookies
    No more Creating accounts , to see downloading Links
""")
def get_choice():
    choice = input("""
                    Please Choose the Site that You want to Acces :
                1- Netflix
                2- Spotify
                3- repack.me
                4- Quit
                """)
    return choice
choice = get_choice()

if(choice.isdecimal()):
    choice = int(choice)
    if(choice==1):
        print("Netflix")
    elif(choice==2):
        print("Spotify")
    elif(choice==3):
        print("repack.me")
    elif(choice==4):
        print("Quit")
        exit()
    else:
        print("invalid Choice")