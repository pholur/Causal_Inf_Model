# This code takes the data from the text file and adds it to the csv file.
import re
import csv

number_of_questions = 16
number_of_options = 5

number_of_studs = 10
w, h = number_of_questions*number_of_options + 2, number_of_studs;

Matrix = [["0" for x in range(w)] for y in range(h)] 

def initr():
    with open("/Users/pavan/Desktop/Research/Masters_Project/SRC/assessments/assess1_LP.txt",'r') as f:
        mylist = f.read().splitlines() 
    return mylist

def scrape(lines):
    ID = []
    r = 1
    for line in lines:
        my_list = line.split("&")
        for obj in my_list:
            keyval = obj.split("=")
            if keyval[0] == "ID":
                c = 0
            elif keyval[0] == "time":
                c = 1
            else:
                c = int(keyval[0]) + 1

            if keyval[1] == "on":
                val = "1"
            else:
                val = keyval[1]

            Matrix[r][c] = val 
            Matrix[0][0] = "ID"
            Matrix[0][1] = "Time"
        r = r + 1
    return Matrix,r-1

# WIPES PREVIOUS ENTRIES INTO CSV. SAVE INSTANCE!!
def save_to_csv(db,r):     
    with open("/Users/pavan/Desktop/Research/Masters_Project/SRC/assessments/assess1_LP.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(db[0:r+1][:])   

if __name__ == '__main__':
    lines = initr()
    db,r = scrape(lines)
    save_to_csv(db,r)

