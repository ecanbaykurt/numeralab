import streamlit as st
from numeralab_core.image_to_equation_google import extract_equation_from_image_google_api
from numeralab_core.equation_solver import solve_equation_numeric
from numeralab_core.report_generator import generate_report
from numeralab_core.critical_finder import find_critical_points
from numeralab_core.ai_summary import generate_scientific_summary
import numpy as np
import sympy as sp

# Page config
st.set_page_config(page_title="NumeraLab", layout="wide")
st.title("📐 NumeraLab: AI-Powered Numerical Assistant")

# User inputs
uploaded_file = st.sidebar.file_uploader("Upload equation image (JPG, PNG)", type=["jpg", "png"])
method = st.sidebar.selectbox(
    "Select Numerical Method",
    ["Finite Difference Method (FDM)", "Runge-Kutta", "Newton-Raphson", "Curve Fitting"]
)

# Main workflow
if uploaded_file:
    st.info("Extracting equation from image using Google Cloud Vision API...")
    extracted_eq = extract_equation_from_image_google_api(uploaded_file)
    st.write("Detected Equation:")
    st.latex(extracted_eq)

    st.info("Solving numerically...")
    result, fig = solve_equation_numeric(extracted_eq, method)
    st.pyplot(fig)

    # X and Y calculation for further analysis
    try:
        x = sp.symbols('x')
        f = sp.lambdify(x, sp.sympify(extracted_eq), 'numpy')
        x_vals = np.linspace(-10, 10, 200)
        y_vals = f(x_vals)

        # Auto-Critical Finder
        if st.button("Find Critical Points (AI Assisted)"):
            crit_points, crit_fig = find_critical_points(x_vals, y_vals)
            st.pyplot(crit_fig)
            st.write("Critical Points Found:")
            st.write(crit_points)

            # AI Summary
            if st.button("Generate AI Scientific Summary"):
                ai_summary = generate_scientific_summary(extracted_eq, method, crit_points)
                st.write("AI Scientific Summary:")
                st.info(ai_summary)

    except Exception as e:
        st.error(f"Error in processing equation: {e}")

    # PDF Report
    if st.button("Generate PDF Report"):
        report_path = generate_report(extracted_eq, method, result)
        st.success(f"Report generated: {report_path}")
