import streamlit as st
from numeralab_core.image_to_equation import extract_equation_from_image
from numeralab_core.equation_solver import solve_equation_numeric
from numeralab_core.report_generator import generate_report

st.set_page_config(page_title="NumeraLab", layout="wide")
st.title("📐 NumeraLab: AI-Powered Numerical Assistant")

uploaded_file = st.sidebar.file_uploader("Upload equation image (JPG, PNG)", type=["jpg", "png"])
method = st.sidebar.selectbox("Select Numerical Method", ["Finite Difference Method (FDM)", "Runge-Kutta", "Newton-Raphson", "Curve Fitting"])

if uploaded_file:
    st.info("Extracting equation from image...")
    extracted_eq = extract_equation_from_image(uploaded_file)
    st.write("Detected Equation:")
    st.latex(extracted_eq)

    st.info("Solving numerically...")
    result, fig = solve_equation_numeric(extracted_eq, method)

    st.pyplot(fig)

    if st.button("Generate PDF Report"):
        report_path = generate_report(extracted_eq, method, result)
        st.success(f"Report generated: {report_path}")
from numeralab_core.critical_finder import find_critical_points

# ... diğer kodların altına ekle ...
    if st.button("Find Critical Points (AI Assisted)"):
        crit_points, crit_fig = find_critical_points(x_vals, y_vals)
        st.pyplot(crit_fig)
        st.write("Critical Points Found:")
        st.write(crit_points)
