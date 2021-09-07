from time import sleep
import requests

def check(name):
    r = requests.get("https://lols.gg/en/name/checker/na/" + name) # uses lols.gg to check names :D
    if "Add to Calendar" in r.text:
        print("")
        return False
    else:
        print("AVAILABLE!")
        return True

file2 = open('availablenames.txt', 'a')
file2.write("--------------------------\n")
file2.close()
file1 = open('names.txt', 'r')

count = 0
 
print("Now checking league names ...")

for line in file1:
    file2 = open('availablenames.txt', 'a')
    count += 1
    print(line.strip(), end = "\t")
    try:
        if(check(line.strip())):
            file2.write(line.strip() + "\n")
    except:
        pass

 
# Closing files
file1.close()
print(" >> fin")
