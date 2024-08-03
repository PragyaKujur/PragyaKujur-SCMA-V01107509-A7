import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample marketing data
data = {
    'Campaign': ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D'],
    'Clicks': [1000, 1500, 2000, 2500],
    'Impressions': [10000, 15000, 20000, 25000],
    'CTR': [0.1, 0.1, 0.1, 0.1],
    'Conversions': [100, 120, 150, 180],
    'Cost': [500, 700, 800, 900],
    'Revenue': [1500, 2100, 3000, 4000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Marketing Campaign Dashboard')

st.sidebar.header('Filters')

# Sidebar filters
selected_campaigns = st.sidebar.multiselect('Select Campaigns', options=df['Campaign'], default=df['Campaign'])

# Filter data
filtered_data = df[df['Campaign'].isin(selected_campaigns)]

# Display filtered data
st.write('### Filtered Data', filtered_data)

# Plotting Clicks vs Conversions
st.write('### Clicks vs Conversions')
fig, ax = plt.subplots()
ax.bar(filtered_data['Campaign'], filtered_data['Clicks'], label='Clicks')
ax.bar(filtered_data['Campaign'], filtered_data['Conversions'], bottom=filtered_data['Clicks'], label='Conversions')
ax.set_xlabel('Campaign')
ax.set_ylabel('Number')
ax.legend()

st.pyplot(fig)

# Plotting Click Through Rate (CTR)
st.write('### Click Through Rate (CTR)')
fig, ax = plt.subplots()
ax.bar(filtered_data['Campaign'], filtered_data['CTR'], color='green')
ax.set_xlabel('Campaign')
ax.set_ylabel('CTR')
st.pyplot(fig)

# Plotting Cost vs Revenue
st.write('### Cost vs Revenue')
fig, ax = plt.subplots()
ax.bar(filtered_data['Campaign'], filtered_data['Cost'], label='Cost')
ax.bar(filtered_data['Campaign'], filtered_data['Revenue'], bottom=filtered_data['Cost'], label='Revenue')
ax.set_xlabel('Campaign')
ax.set_ylabel('Amount')
ax.legend()

st.pyplot(fig)

# Show data statistics
st.write('### Data Statistics')
st.write(filtered_data.describe())

# ROI Calculation
st.write('### Return on Investment (ROI)')
filtered_data['ROI'] = (filtered_data['Revenue'] - filtered_data['Cost']) / filtered_data['Cost'] * 100
st.write(filtered_data[['Campaign', 'ROI']])

st.write('### Additional Analysis')
st.write("""
This dashboard provides an overview of marketing campaign performance. You can use the filters to select specific campaigns and analyze their performance in terms of clicks, impressions, conversions, cost, and revenue. The Click Through Rate (CTR) chart helps visualize the effectiveness of each campaign, and the ROI calculation provides insight into the profitability of each campaign.
""")
