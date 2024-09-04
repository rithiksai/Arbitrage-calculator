import streamlit as st

# Input fields for user inputs
stake = st.number_input("Enter the total amount:", min_value=0, step=1)
o1 = st.number_input("Enter the odds of 1 (promotion):", min_value=0.0, step=0.01)
o2 = st.number_input("Enter the odds of 2:", min_value=0.0, step=0.01)

def checkArb(ODD1, ODD2):
    a = (1 / ODD1) + (1 / ODD2)

    if a < 1:
        return True, a
    else:
        return False, 0

def calcArb(ODD1, ODD2, a, s):
    roi = (1 / a - 1) * 100
    bet1 = 8350 / ODD1
    bet2 = 8350 / ODD2

    total = bet1 + bet2
    noOfBets = int(stake / total)
    
    # Display the results
    st.write(" ")
    st.write(f"{int(bet1)} * {noOfBets}")
    st.write(int(bet2 * noOfBets))
    st.write(" ")
    st.write(f"Total amount used to bet: {int(noOfBets * total)}")
    st.write(f"Number of accounts: {noOfBets + 1}")
    st.write(" ")
    
    x = int((int(noOfBets * total) * roi / 100) + int(noOfBets * total))
    st.write(f"Total Return: {x}")
    st.write(f"Profit: {x - int(noOfBets * total)}")

    return roi

# Check if arbitrage exists and calculate
if stake > 0 and o1 > 0 and o2 > 0:
    check = checkArb(o1, o2)

    if check[0]:
        roi = calcArb(o1, o2, check[1], stake)
        st.write(f"The ROI percentage is: {roi:.2f}%")
    else:
        st.write("There is no scope for arbitrage.")