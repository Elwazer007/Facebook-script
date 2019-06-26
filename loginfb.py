from selenium import webdriver
passprog = '123456789' # passwoed to run your script
url = 'https://www.facebook.com/'
user = ""
username = ""
password = ""
close = ""
x = ""
dic = {} # the dictionary hash the email and password for log in and the key is username that can be used again to make login

print('Enter The password to the prograam')
x = input()
while x!=passprog:
    print('Wrong passworg to log in to your script please tryagain')
    x = input()

print('Logged in ')
for i in range(100): # to continue in my script while working woth many fb accounts
    print('Choose what to wanna do')
    print('1. login to existing FB account')
    print('2. add FB account')
    choice = input()
    while choice == "2":
        print('Enter your FB account name')
        user = input()
        print('Enter your FB email or phonenumber')
        username = input()
        print('Enter your FB passwoed')
        password = input()
        dic[user] = (username , password )
        print("Enter choice again")
        choice = input()
    print("Enter user you want to make log in")
    user = input()
    flag = "0"
    while flag == "0":
        if user in dic:
            flag = "1"
        else:
            print("User doesn't exist Enter again")
            user = input()
    driver = webdriver.Firefox(executable_path=r'C:/Users/Lenovo/Downloads/geckodriver.exe')
    driver.get(url)
    driver.find_element_by_id('email').send_keys(dic[user][0])
    driver.find_element_by_id('pass').send_keys(dic[user][1])
    driver.find_element_by_id('loginbutton').click()
    print("Done..")
