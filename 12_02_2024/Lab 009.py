# using match condition to ask user which browser they want

browser = str(input("Enter the browser name\n"))
browser = browser.lower() # it means even if lower or upper case are use,
# code will still be executed

match browser:
    case "chrome":
        print("Chrome code executed")
    case "firefox":
        print("Firefox code executed")
    case _:
        print("No browser Found")