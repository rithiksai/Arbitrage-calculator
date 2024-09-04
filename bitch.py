import streamlit as st

# Set page configuration (this must be the first Streamlit command)
st.set_page_config(page_title="Cool Arbitrage Calculator", page_icon="🔥", layout="centered")

# Custom CSS for background and styling
st.markdown(
    """
    <style>
    .main {
        background-color: #000000; /* Black background */
        color: #ffffff; /* White text */
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        color: #00ff7f; /* Spring Green color */
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .stMarkdown {
        color: #ffffff; /* White text */
    }
    .stButton>button {
        background-color: #ff6347; /* Tomato color */
        color: #ffffff; /* White text */
        border-radius: 8px;
        height: 50px;
        width: 200px;
        font-size: 18px;
        font-weight: bold;
    }
    .input-box {
        background-color: #1e1e1e; /* Darker box background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px #ff6347;
        margin-bottom: 20px;
    }
    .stMetric {
        color: #ff4500; /* OrangeRed color */
        font-size: 24px;
        text-align: center;
    }
    .stSuccess {
        color: #32cd32; /* Lime Green color */
    }
    .stError {
        color: #ff4500; /* OrangeRed color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and description with emojis
st.title("🔥 Super Cool Arbitrage Betting Calculator")
st.markdown("Calculate potential arbitrage opportunities and returns based on the odds provided. Make your betting smart and profitable! 💵")

# Create an input box for entering details
with st.form(key='betting_form'):

    stake = st.number_input("Enter the total amount:", min_value=0, step=500)
    o1 = st.number_input("Enter the odds of 1 (promotion):", min_value=0.0, step=0.01)
    o2 = st.number_input("Enter the odds of 2:", min_value=0.0, step=0.01)

    

    # Submit button
    submit_button = st.form_submit_button(label="Calculate 🔍")

def checkArb(ODD1, ODD2):
    a = (1 / ODD1) + (1 / ODD2)
    if a < 1:
        return True, a
    else:
        return False, 0

def calcArb(ODD1, ODD2, a, stake):
    roi = (1 / a - 1) * 100
    bet1 = 8350 / ODD1
    bet2 = 8350 / ODD2

    total = bet1 + bet2
    noOfBets = int(stake / total)
    
    # Cool progress bar for ROI calculation
    st.markdown("### Calculating ROI and Bets 🚀")
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    # Cool metrics and results with icons
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Bet Breakdown 💸")
        st.write(f"*Bet on Odd 1:* {int(bet1)} * {noOfBets}")
        st.write(f"*Bet on Odd 2:* {int(bet2 * noOfBets)}")
        st.write(f"*Total Amount Used to Bet:* ${int(noOfBets * total)}")
        st.write(f"*Number of Accounts Needed:* {noOfBets + 1}")
    
    with col2:
        st.markdown("### Returns 💰")
        x = int((int(noOfBets * total) * roi / 100) + int(noOfBets * total))
        st.metric(label="Total Return", value=f"${x}", delta="🎯")
        st.metric(label="Profit", value=f"${x - int(noOfBets * total)}", delta=f"{roi:.2f}% 🔥")

    return roi

# Check for valid input before calculating
if submit_button:
    if stake > 0 and o1 > 0 and o2 > 0:
        check = checkArb(o1, o2)

        if check[0]:
            roi = calcArb(o1, o2, check[1], stake)
            st.balloons()
            st.success(f"🎉 The ROI percentage is: {roi:.2f}%")
        else:
            st.error("⚠ There is no scope for arbitrage with the provided odds. Try different values!")
    else:
        st.info("Please enter valid inputs to calculate arbitrage.")

# Footer styling and additional info
st.markdown(
    """
    <hr style='border: 2px solid #555;'>
    <p style='text-align: center; color: #ff6347;'>Built by Rithik ❤ | Make Smart Bets!</p>
    """,
    unsafe_allow_html=True
)
