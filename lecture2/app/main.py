
txtfile = open("danish_companies.txt", "r")
content = txtfile.read()

# Receives txt and output json
# CVR
# Company Name
# Street
# Number
# Postal Code
# Town
# Email Address
txtfile.close()

sections = content.split("|")

def printer(sections):
    for i in sections:
        print(i)

def main():
    printer(sections)

if __name__ == "__main__":
    main()
