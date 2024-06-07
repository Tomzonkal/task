import matplotlib.pyplot as plt
import seaborn as sns
import mlflow 

def plot(df):
    # Rating distribution
    fig=plt.figure(figsize=(10, 6))
    sns.countplot(x='rating', data=df)
    plt.title('Rating Distribution')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    mlflow.log_figure(fig,"Number of Reviews Over Time")

    # Time series of reviews
    fig=plt.figure(figsize=(12, 6))
    df.set_index('date')['rating'].resample('M').count().plot()
    plt.title('Number of Reviews Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Reviews')
    mlflow.log_figure(fig,"Rating Distribution")

    # Boxplot of ratings over time
    fig=plt.figure(figsize=(12, 6))
    sns.boxplot(x=df['date'].dt.year, y='rating', data=df)
    plt.title('Ratings Distribution by Year')
    plt.xlabel('Year')
    plt.ylabel('Rating')
    mlflow.log_figure(fig,"Ratings Distribution by Year")


def check_empty_values(df):
    null_sum=df.isnull().sum().to_dict()
    mlflow.log_dict(null_sum," null_summary")