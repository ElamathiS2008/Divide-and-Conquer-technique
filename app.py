import streamlit as st

from PROGRAM import (
    run_divide_conquer,
    run_naive,
    optimal_formula
)


# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Min-Max Comparison",
    page_icon="🔢",
    layout="centered"
)


# --------------------------------
# Title
# --------------------------------

st.title("🔢 Min-Max Finding Algorithm")

st.write(
    "Find the Minimum and Maximum values "
    "using Divide and Conquer and Naive approaches."
)


# --------------------------------
# User Input
# --------------------------------

st.subheader("Enter Array")

n = st.number_input(
    "Enter the number of elements",
    min_value=1,
    step=1,
    value=5
)

array_input = st.text_input(
    "Enter array elements separated by spaces",
    placeholder="Example: 3 1 7 4 9"
)


# --------------------------------
# Button
# --------------------------------

if st.button("Find Minimum and Maximum"):

    # Check if input is empty
    if not array_input:

        st.error(
            "Please enter the array elements."
        )

    else:

        try:

            # Convert input string to integer list
            arr = list(
                map(
                    int,
                    array_input.split()
                )
            )


            # --------------------------------
            # Check Number of Elements
            # --------------------------------

            if len(arr) != n:

                st.error(
                    f"Expected {n} elements, "
                    f"but received {len(arr)} elements."
                )

            else:

                # --------------------------------
                # Divide and Conquer
                # --------------------------------

                dc_min, dc_max, dc_comps = \
                    run_divide_conquer(arr)


                # --------------------------------
                # Naive Method
                # --------------------------------

                naive_min, naive_max, naive_comps = \
                    run_naive(arr)


                # --------------------------------
                # Formula
                # --------------------------------

                formula = optimal_formula(n)


                # --------------------------------
                # Display Input
                # --------------------------------

                st.subheader("Input Array")

                st.write(arr)


                # --------------------------------
                # Display Minimum and Maximum
                # --------------------------------

                st.subheader("Result")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Minimum",
                        dc_min
                    )

                with col2:

                    st.metric(
                        "Maximum",
                        dc_max
                    )


                # --------------------------------
                # Comparison Analysis
                # --------------------------------

                st.subheader(
                    "Comparison Analysis"
                )

                st.write(
                    "Divide & Conquer Comparisons: ",
                    dc_comps
                )

                st.write(
                    "Naive Comparisons: ",
                    naive_comps
                )

                st.write(
                    "Optimal Formula (3n/2 - 2): ",
                    formula
                )


                # --------------------------------
                # Verification
                # --------------------------------

                if (
                    dc_min == naive_min
                    and dc_max == naive_max
                ):

                    st.success(
                        "Both algorithms produced "
                        "the same Minimum and Maximum."
                    )


        except ValueError:

            st.error(
                "Invalid input! "
                "Please enter only integer values separated by spaces."
            )
