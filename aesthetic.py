import streamlit as st

# App title and description
st.set_page_config(page_title="Arbitrage Calculator", page_icon="💰", layout="centered")
st.title("💰 Arbitrage Betting Calculator")
st.write("Calculate potential arbitrage opportunities and returns based on the odds provided.")

# Sidebar for inputs
st.sidebar.header("Input Parameters")
stake = st.sidebar.number_input("Enter the total amount:", min_value=0, step=1)
o1 = st.sidebar.number_input("Enter the odds of 1 (promotion):", min_value=0.0, step=0.01)
o2 = st.sidebar.number_input("Enter the odds of 2:", min_value=0.0, step=0.01)

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

    # Columns for displaying results side by side
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Bet Breakdown")
        st.write(f"*Bet on Odd 1:* {int(bet1)} * {noOfBets}")
        st.write(f"*Bet on Odd 2:* {int(bet2 * noOfBets)}")
        st.write(f"*Total Amount Used to Bet:* {int(noOfBets * total)}")
        st.write(f"*Number of Accounts Needed:* {noOfBets + 1}")
    
    with col2:
        st.markdown("### Returns")
        x = int((int(noOfBets * total) * roi / 100) + int(noOfBets * total))
        st.metric(label="Total Return", value=f"${x}")
        st.metric(label="Profit", value=f"${x - int(noOfBets * total)}", delta=f"{roi:.2f}%")

    return roi

# Check for valid input before calculating
if stake > 0 and o1 > 0 and o2 > 0:
    check = checkArb(o1, o2)

    if check[0]:
        roi = calcArb(o1, o2, check[1], stake)
        st.success(f"The ROI percentage is: {roi:.2f}%")
    else:
        st.error("There is no scope for arbitrage with the provided odds.")
else:
    st.info("Please enter valid inputs to calculate arbitrage.")