import streamlit as st

def show_progress(kyc, underwriting, pdf):
    cols = st.columns(3)
    cols[0].success("KYC" if kyc else "KYC Pending")
    cols[1].success("Underwriting" if underwriting else "Underwriting Pending")
    cols[2].success("PDF" if pdf else "PDF Pending")
