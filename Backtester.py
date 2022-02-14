#You have to restart the kernal every time you run this.

import backtrader as bt #using the backtrader library here.
from datetime import datetime #feed in date range of interest


class SmaCross(bt.SignalStrategy): #have to define your trading strategy as a class.
    def __init__(self): #creating our initiation function. This runs immediately when an object is created from this class.
        sma = bt.ind.SMA(period=50) #collecting the simple moving average from the last 50 days.
        price = self.data #getting the price from the object's pointer.
        crossover = bt.ind.CrossOver(price, sma) #any points where the price and SMA crossover.
        self.signal_add(bt.SIGNAL_LONG, crossover) #buying long when there is a crossover.

cerebro = bt.Cerebro() #backtrader's main engine for your program. This comes with a lot of presets and
                       #automatically implements indicators like volume traded without me doing it manually. 
    
cerebro.broker.setcash(10000) #Starting with US$10000 
cerebro.addstrategy(SmaCross) #adding the strategy to the engine.

data = bt.feeds.YahooFinanceCSVData(dataname="GOOG.csv", fromdate=datetime(2012, 1, 1), todate=datetime(2022, 2, 13)) 
#the line above is how we give the script market history data, from a CSV file. ^Here we are defining the range
#of dates that we will pass. For instance, above I used the range from the 1st of Jan 2012 to the 13th of Feb 2022.

cerebro.adddata(data) #injecting the market history data to cerebro (the engine)
cerebro.addsizer(bt.sizers.AllInSizer, percents=95) #without this line, the program would only buy one share
#every time and then sell that one share when it needs to sell. With this line we buy with 95% of our balance.

cerebro.run() #run the backtesting.
cerebro.plot(iplot = False) #plot the graph. iplot = False just allows me to plot this while
                            #coding in Jupyter lab.
