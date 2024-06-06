import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import chardet

def visualize_customers_data(file_path):
    # Detect encoding
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    
    # Load dataset with detected encoding
    data = pd.read_csv(file_path, encoding=encoding)
    
    # Display the first few rows and column names of the dataset
    print(data.head())
    print(data.columns)
    
    # Convert 'Subscription Date' column to datetime
    if 'Subscription Date' in data.columns:
        data['Subscription Date'] = pd.to_datetime(data['Subscription Date'])
        
        # Line Chart: Subscriptions Over Time
        data['YearMonth'] = data['Subscription Date'].dt.to_period('M').astype(str)
        subscriptions_over_time = data.groupby('YearMonth').size().reset_index(name='Subscriptions')
        fig = px.line(subscriptions_over_time, x='YearMonth', y='Subscriptions', title='Subscriptions Over Time')
        fig.show()
    
    # Bar Chart: Subscriptions by Country
    if 'Country' in data.columns:
        subscriptions_by_country = data['Country'].value_counts().reset_index()
        subscriptions_by_country.columns = ['Country', 'Subscriptions']
        fig = px.bar(subscriptions_by_country, x='Country', y='Subscriptions', title='Subscriptions by Country')
        fig.show()
    
    # Bar Chart: Subscriptions by City
    if 'City' in data.columns:
        subscriptions_by_city = data['City'].value_counts().reset_index()
        subscriptions_by_city.columns = ['City', 'Subscriptions']
        fig = px.bar(subscriptions_by_city, x='City', y='Subscriptions', title='Subscriptions by City')
        fig.show()
    
    # Pie Chart: Email Domain Distribution
    if 'Email' in data.columns:
        data['Email Domain'] = data['Email'].str.split('@').str[1]
        email_domain_distribution = data['Email Domain'].value_counts().reset_index()
        email_domain_distribution.columns = ['Email Domain', 'Count']
        fig = px.pie(email_domain_distribution, names='Email Domain', values='Count', title='Email Domain Distribution')
        fig.show()

# Example usage:
visualize_customers_data('customers-100.csv')
