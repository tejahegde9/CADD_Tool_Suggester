# 🔬 CADD Tool Suggester: Immunoinformatics Pipeline

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tejahegde9-cadd-tool-suggester-app-wcfi7r.streamlit.app/)

This interactive web application, built with **Streamlit** and **Python**, serves as a decision support system for common tasks in **Computer-Aided Drug Design (CADD)** and **Rational Vaccine Design**.

It implements a complete end-to-end **Immunoinformatics pipeline** (from Sequence Retrieval to Molecular Dynamics) by recommending the best open-source or web-based tools for each step.

---

## 🧬 Key Pipeline Steps Covered

The app's database provides curated, verified tool recommendations for the following critical steps:

1.  **Sequence Retrieval:** Obtaining target protein sequences (UniProt).
2.  **Safety Screening:** **Antigenicity** (VaxiJen) and **Allergenicity** (AllerTOP) checks.
3.  **Structure Prediction:** Secondary and Tertiary structure modeling.
4.  **Model Validation:** Structural refinement and quality checks (MolProbity, ProSA-web).
5.  **Epitope Screening:** T-cell (MHC) and B-cell epitope prediction for vaccine candidates (IEDB).
6.  **Immune Simulation:** Modeling the host immune response (C-ImmSim).
7.  **Optimization:** Codon optimization (JCat) for enhanced expression and stability analysis (GROMACS).

---

## 🛠️ Technology Stack

* **Web Framework:** Streamlit (Python)
* **Data Storage:** JSON (used as a simple, structured database for tool entries)
* **Deployment:** Streamlit Community Cloud
* **Version Control:** Git/GitHub

## 🚀 Installation & Usage (Local)

To run this application locally, follow these steps:

1.  Clone the repository: `git clone https://github.com/tejahegde9/CADD_Tool_Suggester.git`
2.  Navigate to the directory: `cd CADD_Tool_Suggester`
3.  **Activate your environment** and install dependencies:
    ```bash
    # Ensure your venv is active
    pip install streamlit pandas
    ```
4.  Run the application: `streamlit run app.py`
