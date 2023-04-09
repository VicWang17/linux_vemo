import sys
import csv
import os
from datetime import datetime
from get_path import cpath

def help():
    print("Usage: Vemo [opration] [arg] [opration] [arg]...")
    print("None   :Get into work place")
    print("-a     :Add a new memo event, without its deadline")
    print("-e     :Edit a memo information")
    print("-h     :See a short help document")
    print("-r     :Remove a memo information")
    print("-v     :View all the memo information so far")
    print("-V     :Checkout the version code of Vemo ")

def error(reason):
    print('\033[1;91m'+"ERROR: "+reason+'\033[m')
    exit()

def warning(reason):
    print('\033[1;93m'+"WARNING: "+reason+'\033[m')

def checkarg(index):
    try:
        v = sys.argv[index+1]
    except:
        error("Missing necessary argument value")


def is_t(index):
    try:
        if sys.argv[index+1] == '-t':
            return True
        else:
            return False
    except:
        return False

def is_valid_time(date):
    try:
        datetime.strptime(date, "%Y-%m-%d-%H:%M")
    except:
        error("Invlid time format, time should be like 2023-1-1 18:00")

def csv_w(row):
    with open(cpath,mode = 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)   

def csv_r():
    with open(cpath,newline='') as f:
        reader = csv.reader(f)
        datas = [row for row in reader]
    return datas

def time_diff(time):
    date = datetime.strptime(time, '%Y-%m-%d-%H:%M')
    now = datetime.now()
    diff = date - now
    days = diff.days
    seconds = diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    strtime = f"{days} days {hours:02} hours {minutes:02} minutes {seconds:02} seconds"
    return strtime,diff


def view():
    datas = csv_r()
    i = 1 
    print("----------------------------------------------------------------------")
    print(f"   {'Events':<40}{'Deadline':<16}Remain")
    print("----------------------------------------------------------------------")
    for data in datas:
        print(f"{i}. ", end="")
        i += 1
        if data[1] == "":
            print(data[0])
        else:
            remain, diff = time_diff(data[1])
            if diff.total_seconds() <= 0:
                print(f"{data[0]:<40} {data[1]:<16} \033[1;31;40mTIMEOUT!\033[m")
            elif diff.days < 1:
                print(f"{data[0]:<40} {data[1]:<16} \033[1;33;40m{remain}\033[m")
            else:
                print(f"{data[0]:<40} {data[1]:<16} {remain}")
    print("----------------------------------------------------------------------")
def scan(index):
    op = sys.argv[index]

    if op == '-a':
        checkarg(index)
        index += 1
        event = sys.argv[index]
        if is_t(index):
            index+=2
            date = sys.argv[index]
            is_valid_time(date)
            csv_w([event,date])
            print("Adding Successful!")
        else:
            csv_w([event,""])
            warning("This event has no deadline")
            print("Adding successful!")

    elif op == '-e':
        pass
    elif op == '-r':
        pass
    elif op == '-h':
        help()
    elif op == '-V':
        print("Vemo 0.0.1 Developed by VicWang17")

    elif op == '-v':
       view() 
    elif op == '-t':
        error("Need to append a event first")
    else:
        error("Invalid operation")

    return index


if __name__ == '__main__':
    index = 1
    max = len(sys.argv)
    if max >= 2:
        while(index < max):
            index = scan(index)
            index += 1
    else:
        view()

