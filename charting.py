#    charting.py
from Tkinter import *
from globals import *
from ms_data import MS_stockHandler
import gf_data

'''
#charting one stock here
stock = gf_data.getQuote("WUBA")
handler = MS_stockHandler(google_stock_dict_data = stock)
#if hander is initialized without error
if handler.initialized:
    #parse and initialize data before analize
    handler.parseBalanceSheet()
    handler.parseKeyRatios()
'''

#helper functions for draw Chart
def mapit(minv, maxv, t):
    r = maxv-minv
    h = t-minv
    return h/r

def getmaxmin(val_dict):
    max = -100000.0
    min = 100000.0
    for i in val_dict.keys():
        v = val_dict[i]
        if v:   #if v have value
            if v > max:
                max = v
            if v < min:
                min = v
    return max, min

def drawChart(handler, data_to_chart = "Book Value Per Share USD"):


    latest_year = 2015  #TODO: clean this up. hard coded.
    #data_to_chart = "Book Value Per Share USD"

    price_list = dict()
    for i in range (0, 10):
        year = latest_year - i
        bps = handler.getFinancialData("key_ratios", str(year), data_to_chart)
        if bps == None:
            price_list[str(year)] = None
        else:
            price_list[str(year)] = float(bps)

    print price_list

    #get max and min value in the list
    max_val, min_val = getmaxmin(price_list)
    print max_val, min_val
    max_val = max_val*1.1   #a simple mult here for top spacing
    min_val = min_val*0.8   #a simple mult here for bottom spacing

    #variables for ui
    m = 20
    step = 50
    width = 600
    height = 400

    #tkinter gui
    master = Tk()
    master.geometry('+10+10') 
    w = Canvas(master, width=width, height=height)

    chart_title_text = handler.exchange+":"+handler.ticker
    w.create_text(10, 10, text=chart_title_text, fill="blue", anchor="nw", font=("Purisa", 15))
    w.create_text(10, 30, text=data_to_chart, fill="black",anchor="nw")
    master.title(chart_title_text+"  "+data_to_chart)

    #bg lines
    for i in range(0,11):
        w.create_line(step*i, 0, step*i, height,fill="gray", dash=(4, 4))

    #variabale for the drawing loop
    s = step    #step size in x.
    c = 1       #for skip line draw on first year
    ptw = 36    #price bg width
    pth = 15    #price bg height

    for i in sorted(price_list.keys()):

        year = i
        val = price_list[i]

        if val == None:
            print "No value found for year: ", year
            s+=step
            continue

        pos = mapit(min_val, max_val, val)*height

        #first value. no line need to be drawn.
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

    w.pack()
    w.update()
    #output eps file
    w.postscript(file=TEMP_DIR+handler.ticker.lower()+".eps", colormode='color')

    #run it
    master.mainloop()



#drawChart(handler)