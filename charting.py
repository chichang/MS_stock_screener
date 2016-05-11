#    charting.py
import sys
sys.path.append("/USERS/chichang/workspace/3rd_party/MS_stock_screener")
from ms_data import MS_stockHandler
import gf_data
from globals import *


stock = gf_data.getQuote("FLY")
handler = MS_stockHandler(google_stock_dict_data = stock)
#if hander is initialized without error
if handler.initialized:
    #parse and initialize data before analize
    handler.parseBalanceSheet()
    handler.parseKeyRatios()

latest_year = 2015
price_list = dict()
for i in range (0, 10):
    year = latest_year - i
    bps = handler.getFinancialData("key_ratios", str(year), "Book Value Per Share USD")
    if bps == None:
        bps =0
    price_list[str(year)] = float(bps)

print price_list



from Tkinter import *

def mapit(minv, maxv, t):
    range = maxv-minv
    h = t-minv
    print range, h
    return h/range

def getmaxmin(val_dict):
    max = -100000.0
    min = 100000.0
    for i in val_dict.keys():
        v = val_dict[i]
        if v > max:
            max = v
        if v < min:
            min = v
    return max, min

max_val, min_val = getmaxmin(price_list)

max_val = max_val*1.1
min_val = min_val*0.8


latest_year = 2015

m = 20
step = 50
width = 400
height = 400

print mapit(min_val, max_val, 26.78)*400

#mult = height/max_val
#print mult

master = Tk()

w = Canvas(master, width=600, height=400)
w.pack()

w.create_text(10, 10, text="TEST:TICKER", fill="blue", anchor="nw")
w.create_text(10, 22, text="Book Value Per Share USD", fill="black",anchor="nw")

#bg lines
for i in range(0,11):
    w.create_line(step*i, 0, step*i, height,fill="gray", dash=(4, 4))

s = step
c = 1
ptw = 36
pth = 15

for i in sorted(price_list.keys()):
    print i
    #first value. no line.

    pos = mapit(min_val, max_val, price_list[i])*height

    if c == 1:

        prev_val = price_list[i]
        #price bg
        w.create_rectangle(s, height-pos, s+ptw, (height-pos)+pth,fill="red")
        #price
        w.create_text(s, height-pos, text=price_list[i], fill="blue", anchor="nw")
        #year
        w.create_text(s, height-20, text=i, fill="black", anchor="nw")

        c+=1
        continue

    year = i
    val = price_list[i]
    
    ppos = mapit(min_val, max_val, prev_val)*height
    
    #line
    w.create_line(s, height-ppos, s+step, height-pos, fill="blue", width=2)
    #price bg
    w.create_rectangle(s+step, height-pos, s+step+ptw, (height-pos)+pth,fill="red")
    #price
    w.create_text(s+step, height-pos, text=price_list[i], fill="blue", anchor="nw")
    #year
    w.create_text(s+step, height-20, text=i, fill="black", anchor="nw")
    
    prev_val = price_list[i]
    s+=step
    c+=1


#w.create_text(step*10, height-y10*mult, text=str(y10), fill="blue", anchor="nw")
#w.create_text(step, height-20, text=str(latest_year-10), fill="black", anchor="nw")
#w.create_text(step*10, height-20, text=str(latest_year), fill="black", anchor="nw")

#w.create_text(step*10, height-y10*mult, text=str(y10), fill="blue", anchor="nw")

#for i in range(0,10):
#    w.create_line(step*i, 0, step*i, height,fill="gray", dash=(4, 4))
#w.create_rectangle(50, 25, 150, 75, fill="blue")


#w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()
