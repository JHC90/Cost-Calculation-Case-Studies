def calBEPSalesWithCMR(TFC, VC, SP):
    '''
    Calculation the return at Point of BEV with the CMR
    '''
    BEPs=(TFC/(calcCMR(VC, SP)))
    return(BEPs)

def calcCMR(VC, SP):
    '''
    Calculating the CMR 
    '''
    # CM = calcCM(VC, SP)
    CMR = (calcCM(VC, SP))/SP
    return(CMR)
    

def calBEPUnits(TFC, VC, SP):
    '''
    Calculation for
    '''
    cm = calcCM(VC, SP)
    BEPu=(TFC/cm)
    return(BEPu)

def calcCM(VC, S):
    '''
    Calculation for the Contribution Margin, insert first the Sales and afterwards the VariableCost
    '''
    CM = S - VC
    return(CM)

def calcProfit(X, TFC, VC, SP):
    '''
    Calculation for the Profit, give the Sequence of "SP, X, VC, TFC"
    '''
    profit = ((SP * X) - (VC * X) - TFC)
    return(profit)

def printBEP(X, TFC, VC, SP, switch):
    import matplotlib.pyplot as plt
    '''
    Diese Funktion plotet ein Break-Even-Chart mit einer dazugehörigen Legende
    '''
    quantity = list(range(0, X, 1))
    
    # Fixed Cost
    fixedCost = TFC
    fixedCostSeries = [fixedCost] * len(quantity)
    
    # Variable Cost
    varCost = VC
    varCostSeries = []
    for i in range(0,len(quantity),1):
        varCostSeries.append(fixedCost + i * varCost)
        
    # Sales
    sellingPrice = SP
    sellingPriceSeries = []
    for i in range(0,len(quantity),1):
        sellingPriceSeries.append(sellingPrice *i)
   
    
    plt.plot(quantity, fixedCostSeries, label = "Fixed-Cost") 
    plt.plot(quantity, varCostSeries, label = "Variable-Cost") 
    plt.plot(quantity, sellingPriceSeries, label = "Sales")
    if(switch==1):
        plt.fill_between(quantity, varCostSeries, sellingPriceSeries, color='blue', alpha=.1)
    plt.legend()
    #return(plt)