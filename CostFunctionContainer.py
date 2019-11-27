##################---BASIC-FORMULA---##################
def calcX(S, SP):
    '''
    Calculate the Sold units, given the Sales and the selling Price
    '''
    x = S/SP
    return(x)

def calcTVC(X, VCU):
    '''
    Calculate the total Variable Cost, given the Units and the VCU
    '''
    VC = X * VCU
    return(VC)

def calcVCU(X, TVC):
    '''
    CalculateVC per unit, given TVC and X
    '''
    VCU = TVC / X
    return(VCU)



##################---BASIC-FORMULA---##################

##################---Contribution Margin---##################

def calcCM(TVC, S):
    '''
  Contribution Margion gesamt = Deckungsbeitrag
    '''
    CM = S - TVC
    return(CM)

def calcCMU(VCU, SP):
    '''
  Contribution Margion per Stück = Deckungsbeitrag jedes einzelnen Stückes
    '''
    CMU = SP - VCU
    return(CMU)


def calcCMR(VCU, SP):
    '''
    Wieviel % von dem SP gehen für die Deckung der Kosten/ zu Generation des Gewinnes bei
    '''
    # CM = calcCM(VC, SP)
    CMR = (calcCM(VCU, SP))/SP
    return(CMR)
##################---Contribution Margin---##################    
##################---PROFIT---##################
def calcProfitsimpleTotal(TFC, TVC, S):
    '''
    Calculation for the Profit, give the Sequence of "SP, X, VC, TFC"
    '''
    profit = S - TVC - TFC
    return(profit)


def calcProfitsimplePerUnit(X, TFC, VCU, SP):
    '''
    Calculation for the Profit, give the Sequence of "SP, X, VC, TFC"
    '''
    profit = ((SP * X) - (VCU * X) - TFC)
    return(profit)

def calcProfitWithCMR(S, CMR, TFC):
    '''
    Calculation for the Profit, given the Sales and the CMR
    '''
    profit = (S * CMR) - TFC
    return(profit)
##################---PROFIT---##################

##################---BEP---##################

def calcBEPUnits(TFC, VCU, SP):
    '''
    Calculation for
    '''
    cm = calcCM(VCU, SP)
    BEPu=(TFC/cm)
    return(BEPu)

def calcBEPUnitsWithCMU(TFC, CMU):
    '''
    Calculation BEPUnits with the CM /Unit
    '''
    BEPu = TFC / CMU
    return(BEPu)

def calcBEPSalesWithCMR(TFC, VCU, SP):
    '''
    Calculation the return at Point of BEP with the CMR
    '''
    BEPs=(TFC/(calcCMR(VCU, SP)))
    return(BEPs)

def calcBEPSalesSimple(BEPU, SP):
    '''
    Calculation the return at Point of BEP Simple
    '''
    BEPs = BEPU * SP
    return(BEPs)

def calcMarginOfSafety(S, BEPS):
    '''
    Calculation for
    '''
    MS = S - BEPS
    return(MS)


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
    
    
##################---BEP---##################