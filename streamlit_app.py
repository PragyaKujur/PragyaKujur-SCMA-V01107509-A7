import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample marketing data
data = {
    'Campaign': ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D'],
    'Clicks': [1000, 1500, 2000, 2500],
    'Impressions': [10000, 15000, 20000, 25000],
    'CTR': [0.1, 0.1, 0.1, 0.1],
    'Conversions': [100, 120, 150, 180],
    'Cost': [500, 700, 800, 900],
    'Revenue': [1500, 2100, 3000, 4000],
    'Duration': [30, 45, 60, 75],  # Duration of campaign in days
    'ROI': [200, 200, 275, 344]  # ROI percentage
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Marketing Campaign Dashboard')

# Sidebar for data input
st.sidebar.header('Data Input')

# File upload
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("File uploaded successfully")

# Data entry widgets
st.sidebar.subheader('Add New Campaign')
campaign = st.sidebar.text_input('Campaign Name')
clicks = st.sidebar.number_input('Clicks', min_value=0)
impressions = st.sidebar.number_input('Impressions', min_value=0)
conversions = st.sidebar.number_input('Conversions', min_value=0)
cost = st.sidebar.number_input('Cost', min_value=0.0)
revenue = st.sidebar.number_input('Revenue', min_value=0.0)
duration = st.sidebar.number_input('Duration (days)', min_value=1)

# Add data to DataFrame
if st.sidebar.button('Add Campaign'):
    new_data = {
        'Campaign': campaign,
        'Clicks': clicks,
        'Impressions': impressions,
        'CTR': conversions / impressions if impressions > 0 else 0,
        'Conversions': conversions,
        'Cost': cost,
        'Revenue': revenue,
        'Duration': duration,
        'ROI': (revenue - cost) / cost * 100 if cost > 0 else 0
    }
    df = df.append(new_data, ignore_index=True)
    st.sidebar.success('Campaign added successfully')

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

# Comparison options
st.sidebar.header('Comparison Options')
comparison = st.sidebar.selectbox('Select Comparison', [
    'None', 
    'Clicks vs Impressions', 
    'Cost vs Revenue', 
    'CTR vs Conversions', 
    'Revenue vs Duration', 
    'Cost vs Duration', 
    'Impressions vs Duration',
    'Clicks vs Conversions (Box Plot)',
    'Heatmap of Metrics'
])

# Generate comparison plots
if comparison == 'Clicks vs Impressions':
    st.write('### Clicks vs Impressions')
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['Clicks'], filtered_data['Impressions'])
    ax.set_xlabel('Clicks')
    ax.set_ylabel('Impressions')
    st.pyplot(fig)

elif comparison == 'Cost vs Revenue':
    st.write('### Cost vs Revenue')
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['Cost'], filtered_data['Revenue'])
    ax.set_xlabel('Cost')
    ax.set_ylabel('Revenue')
    st.pyplot(fig)

elif comparison == 'CTR vs Conversions':
    st.write('### CTR vs Conversions')
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['CTR'], filtered_data['Conversions'])
    ax.set_xlabel('CTR')
    ax.set_ylabel('Conversions')
    st.pyplot(fig)

elif comparison == 'Revenue vs Duration':
    st.write('### Revenue vs Duration')
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['Revenue'], filtered_data['Duration'])
    ax.set_xlabel('Revenue')
    ax.set_ylabel('Duration (days)')
    st.pyplot(fig)

elif comparison == 'Cost vs Duration':
    st.write('### Cost vs Duration')
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['Cost'], filtered_data['Duration'])
    ax.set_xlabel('Cost')
    ax.set_ylabel('Duration (days)')
    st.pyplot(fig)

elif comparison == 'Impressions vs Duration':
    st.write('### Impressions vs Duration')
    fig, ax = plt.subplots()
    ax.scatter(filtered_data['Impressions'], filtered_data['Duration'])
    ax.set_xlabel('Impressions')
    ax.set_ylabel('Duration (days)')
    st.pyplot(fig)

elif comparison == 'Clicks vs Conversions (Box Plot)':
    st.write('### Clicks vs Conversions (Box Plot)')
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_data[['Clicks', 'Conversions']], ax=ax)
    st.pyplot(fig)

elif comparison == 'Heatmap of Metrics':
    st.write('### Heatmap of Metrics')
    fig, ax = plt.subplots()
    sns.heatmap(filtered_data[['Clicks', 'Impressions', 'CTR', 'Conversions', 'Cost', 'Revenue', 'ROI', 'Duration']].corr(), annot=True, ax=ax)
    st.pyplot(fig)

st.write('### Additional Analysis')
st.write("""
This dashboard provides an overview of marketing campaign performance. You can use the filters to select specific campaigns and analyze their performance in terms of clicks, impressions, conversions, cost, and revenue. The Click Through Rate (CTR) chart helps visualize the effectiveness of each campaign, and the ROI calculation provides insight into the profitability of each campaign.
""")
