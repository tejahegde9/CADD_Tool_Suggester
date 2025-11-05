import streamlit as st
import pandas as pd
import json

# Function to load your CADD data (runs once for performance)
@st.cache_data
def load_data():
    try:
        # Load your curated CADD data from the JSON file
        with open('cadd_data.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error("Error: cadd_data.json not found. Make sure the file is in the same folder.")
        return []

cadd_data = load_data()

st.set_page_config(layout="wide") # Use wide layout for better table view
st.title("🔬 CADD Tool Suggester")
st.markdown("A curated database of the best tools for **Computer-Aided Drug Design** tasks, complete with backup options and official links.")

# 1. Create the Search Interface
# Flatten the task list into a simple list of task names for the search box
task_options = [entry['task_query'] for entry in cadd_data]
search_query = st.selectbox(
    "Select a CADD Task:",
    options=[''] + task_options, # Add an empty option
    index=0
)

# 2. Display the Results (The "Answer Engine" part)
if search_query:
    # Find the matching task entry
    result = next((item for item in cadd_data if item["task_query"] == search_query), None)
    
    if result:
        st.subheader(f"✅ Best Tool Recommendation: {result['best_tool_name']}")
        st.info(f"**Reason:** {result['best_tool_reason']}")
        
        st.subheader("🛠️ All Available Tools (with Backup Links)")
        
        # Convert the tools_list array to a Pandas DataFrame for easy display
        tools_df = pd.DataFrame(result['tools_list'])
        
        # Format the URL column to be a clickable link (using Markdown for better display)
        tools_df['Tool Link'] = tools_df.apply(lambda row: f"[Go to site]({row['url']})", axis=1)

        # Display only relevant columns for the final table
        st.dataframe(tools_df[['name', 'focus', 'category', 'Tool Link']], 
                     hide_index=True, 
                     use_container_width=True,
                     column_config={
                         "Tool Link": st.column_config.Column(
                             "Official Link",
                             width="small"
                         )
                     }
        )