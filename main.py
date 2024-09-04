import streamlit as st

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

stake = int(input("Enter the total amopunt : "))

o1 = float(input("enter the odds of 1 (promotion) : "))

o2 = float(input("enter the odds of 2 : "))

def checkArb(ODD1,ODD2):
    a = (1/ODD1) + (1/ODD2)

    if(a < 1):
        return True , a
    else:
        return False , 0
    
def calcArb(ODD1,ODD2,a,s):
    roi = (1/a - 1) * 100
    bet1 = 8350/ODD1
    bet2 = 8350/ODD2

    total  = bet1 + bet2

    noOfBets = int(stake/total)

   
    st.write(str(int(bet1)) , " * " , str(noOfBets))


check = checkArb(o1,o2)

#print(check)

if(check[0]):
    roi = calcArb(o1,o2,check[1],stake)
    
    
else:
    print("There is no scope for arbitrage")
    """
    print("    ")
    print(str(int(bet1))+" * " + str(noOfBets))
    print(int(bet2*noOfBets))
    print("    ")
    print("Total amount used to bet : "+str(int(noOfBets*total)))
    print("number of accounts : "+str(noOfBets+1))
    print("    ")
    x = int((int(noOfBets*total) * roi/100) + int(noOfBets*total))
    print("Total Return : "+str(x))
    print("Profit : "+str(x-int(noOfBets*total)))
    print("The roi percentage is : "+ str(roi))
    """


