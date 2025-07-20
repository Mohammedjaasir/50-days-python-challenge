import streamlit as st

def main():
    st.set_page_config(
        page_title="Simple Streamlit Calculator",
        page_icon="🧮"
    )

    st.title("🧮 Simple Calculator")
    st.write("Perform basic arithmetic operations with two numbers.")

    st.write("---") # Horizontal line for separation

    # --- User Inputs ---
    st.header("Enter Numbers")

    # Input for the first number
    # Use st.number_input for numerical input
    num1 = st.number_input("First Number", value=0.0, format="%.2f", key="num1")

    # Input for the second number
    num2 = st.number_input("Second Number", value=0.0, format="%.2f", key="num2")

    # --- Operation Selection ---
    st.header("Select Operation")

    # Dropdown to choose the operation
    operation = st.selectbox(
        "Choose an operation:",
        ("Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"),
        key="operation"
    )

    st.write("---") # Horizontal line for separation

    # --- Calculation and Display Result ---
    st.header("Result")
    result = None # Initialize result to None

    # Perform calculation based on selected operation
    if st.button("Calculate", key="calculate_button"):
        try:
            if operation == "Add (+)":
                result = num1 + num2
            elif operation == "Subtract (-)":
                result = num1 - num2
            elif operation == "Multiply (*)":
                result = num1 * num2
            elif operation == "Divide (/)":
                if num2 == 0:
                    st.error("Error: Division by zero is not allowed!")
                    result = "Undefined" # Set result to a string for error case
                else:
                    result = num1 / num2
        except Exception as e:
            st.error(f"An error occurred during calculation: {e}")
            result = "Error"

    # Display the result if it's not None
    if result is not None and result != "Undefined" and result != "Error":
        st.success(f"The result is: **{result:.2f}**")
    elif result == "Undefined":
        st.warning("Result is undefined (division by zero).")
    elif result == "Error":
        st.error("Please check your input or operation.")


    st.markdown("---")
    st.info("💡 Tip: Change numbers or operation and click 'Calculate' again!")

if __name__ == "__main__":
    main()