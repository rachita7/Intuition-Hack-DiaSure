import tkinter as tk
import diab
import FuncSet
from tkinter import *
import math

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, FinalPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="How to use:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        Info=tk.Text(self, height=6, width=38)
        Info.pack(padx=5)
        Info.insert(tk.END, "For the first two weeks of usage, \nplease update each meal/snack's value \nand the related details.\n\
After these two weeks, the app will \nhave enough data to start \npredicting your blood sugar patterns.")
        button = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()
        fbutton= tk.Button(self, text="Final result-->", command=lambda: controller.show_frame(FinalPage))
        fbutton.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter details:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        name_label = tk.Label(self, text="Name:")
        age_label = tk.Label(self, text="Age:")
        sex_label = tk.Label(self, text="Sex:")
        type_label = tk.Label(self, text="Type of diabetes:")
        name_entry = tk.Entry(self)

        age_entry = tk.Entry(self)
        sex_entry = tk.Entry(self)
        type_entry = tk.Entry(self)
        name_label.pack(padx=5, pady=5)
        name_entry.pack(padx=5, pady=5)
        age_label.pack(padx=5, pady=5)
        age_entry.pack(padx=5, pady=5)
        sex_label.pack(padx=5, pady=5)
        sex_entry.pack(padx=5, pady=5)
        type_label.pack(padx=5, pady=5)

        type_entry.pack(padx=5, pady=5)

        button1 = tk.Button(self, text="Next->",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose the meal:", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Breakfast",
                            command=lambda: controller.show_frame(PageThree))
        button1.pack(padx=5, pady=5)

        button2 = tk.Button(self, text="Lunch",
                            command=lambda: controller.show_frame(PageThree))
        button2.pack(padx=5, pady=5)
        button3 = tk.Button(self, text="Dinner",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(padx=5, pady=5)
        button4 = tk.Button(self, text="Snack",
                            command=lambda: controller.show_frame(PageThree))
        button4.pack(padx=5, pady=5)
class PageThree(tk.Frame):
    daynum = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        if PageThree.daynum > 0:
            FuncSet.readAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList,
                            accRangeList, oldDetailsList)
        else:
            overallDict = {}
            breakfastDict = {}
            lunchDict = {}
            dinnerDict = {}
            snacksDict = {}
            bldSgrList = []
            qtyList = []
            accRangeList = []
            oldDetailsList = [0,0,0]
            FuncSet.writeAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList, accRangeList, oldDetailsList)
        choices = FuncSet.dictToList(overallDict)
        choices.append('Others...')
        item_label=tk.Label(self, text="Item:")
        item_label.pack(pady=10, padx=10)
        var = tk.StringVar()
        # initial value
        var.set(choices[0])
        option = tk.OptionMenu(self, var, *choices)
        option.pack(padx=10, pady=10)
        item=var.get()

        add_button=tk.Button(self, text="Add to list", command=lambda: controller.show_frame(PageFour))
        add_button.pack(padx=5, pady=5)

        qty_label = tk.Label(self, text="Quantity:")
        qty = tk.StringVar()
        qty_label.pack(pady=10, padx=10)
        qty_entry = tk.Entry(self, textvariable=qty)
        qty_entry.pack(padx=5, pady=5)


        def addEntry():
            OverallDict=diab.toDict("FoodDict.txt")
            exist=diab.exists(OverallDict,item)

            print(type(item_entry.get()))
            print(item_entry.get(), qty_entry.get(), time_entry.get())
        button1 = tk.Button(self, text="Save", command=addEntry)
        button1.pack()
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        daynum=0
        if daynum > 0:
            FuncSet.readAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList,
                            accRangeList, oldDetailsList)
        else:
            overallDict = {}
            breakfastDict = {}
            lunchDict = {}
            dinnerDict = {}
            snacksDict = {}
            bldSgrList = []
            qtyList = []
            accRangeList = []
            oldDetailsList = [0,0,0]
            FuncSet.writeAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList, accRangeList, oldDetailsList)
        FuncSet.readAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList,
                        accRangeList, oldDetailsList)
        item_label=tk.Label(self, text="Item name")
        item_label.pack(padx=5, pady=5)
        item=tk.StringVar()
        item_entry=tk.Entry(self, textvariable=item)
        item_entry.pack(padx=5,pady=5)
        qty_label = tk.Label(self, text="Quantity:")
        qty = tk.StringVar()
        qty_label.pack(pady=10, padx=10)
        qty_entry = tk.Entry(self, textvariable=qty)
        qty_entry.pack(padx=5, pady=5)
        bldsgr_label=tk.Label(self, text="Expected increase in blood sugar per unit:")
        bldsgr_label.pack(padx=5, pady=5)
        bldsgr=tk.StringVar()
        bldsgr_entry=tk.Entry(self,textvariable=bldsgr)
        bldsgr_entry.pack(padx=5, pady=5)
        acc_label=tk.Label(self, text="Accuracy level:")
        acc_label.pack(padx=5, pady=5)
        acc=tk.StringVar()
        acc_entry=tk.Entry(self, textvariable=acc)
        acc_entry.pack(padx=5, pady=5)
        PageThree.daynum=PageThree.daynum+1
        buttona=tk.Button(self, text="Add item", command=lambda: [FuncSet.newInput(item_entry.get(),qty_entry.get(),bldsgr_entry.get(),acc_entry.get(),overallDict, breakfastDict, bldSgrList, qtyList, accRangeList), FuncSet.writeAll(overallDict, breakfastDict, lunchDict, dinnerDict, snacksDict, bldSgrList, qtyList, accRangeList, oldDetailsList)])
        buttona.pack(padx=5, pady=5)
        next_button=tk.Button(self, text="Next", command=lambda: controller.show_frame(FinalPage))
        next_button.pack(padx=5, pady=5)

class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        oldTimeStr = open('dummyTimeAndSgr.txt', 'r').readlines()[0]
        oldSgr = float(open('dummyTimeAndSgr.txt', 'r').readlines()[1])
        oldTime = FuncSet.convertTime(oldTimeStr)
        currTime = FuncSet.currentTime()
        diff = FuncSet.timeDiff(oldTime, currTime)
        slopeList = FuncSet.toList('dummySlopes.txt')
        if 600<oldTime<=1200:
            avgSlope = slopeList[0]
        elif 1200<oldTime<=1900:
            avgSlope = slopeList[1]
        else:
            avgSlope = slopeList[2]
        currSgr = FuncSet.currBldSgr(avgSlope, diff, oldSgr)
        currSgr=round(currSgr,2)

        overallDict = FuncSet.toDict('dummyFoodDict.txt')
        bldSgrList = FuncSet.toList('dummyBldSgrLv.txt')
        recDict = diab.recommend(currSgr, overallDict, bldSgrList)
        f = open("rec.txt", 'w+')
        f.write("Item\tIncr. in blood sugar\t\tMax safe qty\n")
        for key in recDict:
            f.write("{food}\t\t{bldsgr}\t\t{maxqty}\n".format(food=key, bldsgr=recDict[key][0], maxqty=recDict[key][1]))
        f.close()
        Hi_label=tk.Label(self, text="Hi! Your current blood sugar level is approximately-")
        Hi_label.pack()
        currsgr=tk.Label(self, text=currSgr)
        currsgr.pack()
        reco=tk.Label(self,text="You may eat:")
        reco.pack()
        configfile = tk.Text(self, width=45, height=15)
        with open("rec.txt", 'r') as f:
            configfile.insert(INSERT, f.read())
        configfile.pack(padx=10, pady=10)









app = SeaofBTCapp()
app.mainloop()
