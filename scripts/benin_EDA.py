import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
plt.rcParams['font.family'] = 'Noto Sans Ethiopic'

benin_file_path = 'data/benin-malanville.csv'
# togo_file_path = 'd'
# benin_file_path = 'data/benin-malanville.csv'


df_benin = pd.read_csv(benin_file_path)

# to see the overview of the data
# print(df_benin.head())

# print(df_benin.dtypes)

# df_benin.info()

# columns_to_exclude = ['Timestamp', 'Cleaning', 'Comments']
# df_benin_filtered = df_benin.drop(columns= columns_to_exclude)

# columns_to_exclude_for_mode = ['Timestamp', 'Comments']
# df_benin_mode_filtered = df_benin.drop(columns = columns_to_exclude_for_mode)

# mean = df_benin_filtered.mean()
# median = df_benin_filtered.median()
# mode = df_benin_mode_filtered.mode().iloc[0]
# standard_deviation = df_benin_filtered.std()


# print(mean)
# print(median)
# print(mode)
# print(standard_deviation)

# print(df_benin_filtered.describe())

# List of columns to check for missing values
# columns_to_check = ['GHI', 'DNI', 'DHI']

# Check for missing values in these columns
# missing_values_specific = df_benin[columns_to_check].isnull().sum()

# Print missing values for these specific columns
# print("\nMissing values in GHI, DNI, DHI:\n", missing_values_specific)

# # Check for negative values in columns that should be positive
# negative_values = df_benin[df_benin[['GHI', 'DNI', 'DHI']] < 0].count()

# # Print count of negative values for each column
# print("\nNegative values count in GHI, DNI, DHI:\n", negative_values)

# # Function to detect outliers using IQR
# def detect_outliers_iqr(df, columns):
#     outliers = {}
#     for col in columns:
#         Q1 = df[col].quantile(0.25)
#         Q3 = df[col].quantile(0.75)
#         IQR = Q3 - Q1
#         outlier_mask = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))
#         outliers[col] = df[outlier_mask].shape[0]  # Number of outliers
#     return outliers

# # List of columns to check for outliers
# columns_with_outliers = ['ModA', 'ModB', 'WS', 'WSgust']

# # Detect outliers in specified columns
# beni_outliers_count = detect_outliers_iqr(df_benin, columns_with_outliers)

# # Print count of outliers for each column
# print("\nOutliers count in ModA, ModB, WS, WSgust:\n", beni_outliers_count)

# Sample DataFrame with timestamp in the specified format

# # Convert the 'timestamp' column to datetime using the correct format
# df_benin['Timestamp'] = pd.to_datetime(df_benin['Timestamp'], format='%Y-%m-%d %H:%M')

# # Extract components
# df_benin['year'] = df_benin['Timestamp'].dt.year
# df_benin['month'] = df_benin['Timestamp'].dt.month
# df_benin['day'] = df_benin['Timestamp'].dt.day
# df_benin['hour'] = df_benin['Timestamp'].dt.hour

# # Print the updated DataFrame
# print(df_benin.head())


# # Set the 'Timestamp' column as the index
# df_benin.set_index('Timestamp', inplace=True)

# # Plot GHI, DNI, DHI, and Tamb over time
# plt.figure(figsize=(14, 8))

# # Line plots for each variable
# plt.plot(df_benin.index, df_benin['GHI'], label='GHI', color='yellow')
# plt.plot(df_benin.index, df_benin['DNI'], label='DNI', color='blue')
# plt.plot(df_benin.index, df_benin['DHI'], label='DHI', color='black')
# plt.plot(df_benin.index, df_benin['Tamb'], label='Tamb', color='red')

# # Add titles and labels
# plt.title('Time Series Plot of GHI, DNI, DHI, and Tamb')
# plt.xlabel('Time')
# plt.ylabel('Result')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.show()

# # Convert numeric columns to float, forcing errors to NaN
# df_benin['DNI'] = pd.to_numeric(df_benin['DNI'], errors='coerce')
# df_benin['GHI'] = pd.to_numeric(df_benin['GHI'], errors='coerce')
# df_benin['DHI'] = pd.to_numeric(df_benin['DHI'], errors='coerce')
# df_benin['Tamb'] = pd.to_numeric(df_benin['Tamb'], errors='coerce')


# # Plot GHI, DNI, DHI, and Tamb over time
# plt.figure(figsize=(14, 8))

# # Line plots for each variable
# plt.plot(df_benin.index, df_benin['GHI'], label='GHI', color='orange')
# plt.plot(df_benin.index, df_benin['DNI'], label='DNI', color='blue')
# plt.plot(df_benin.index, df_benin['DHI'], label='DHI', color='green')
# plt.plot(df_benin.index, df_benin['Tamb'], label='Tamb', color='red')

# # Add titles and labels
# plt.title('Time Series Plot of GHI, DNI, DHI, and Tamb')
# plt.xlabel('Date')
# plt.ylabel('Values')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.show()

# # Plot area plots for each variable
# plt.figure(figsize=(14, 8))

# # Area plots
# plt.fill_between(df_benin.index, df_benin['GHI'], color='black', alpha=0.5, label='GHI')
# plt.fill_between(df_benin.index, df_benin['DNI'], color='blue', alpha=0.5, label='DNI')
# plt.fill_between(df_benin.index, df_benin['DHI'], color='yellow', alpha=0.5, label='DHI')
# plt.fill_between(df_benin.index, df_benin['Tamb'], color='red', alpha=0.5, label='Tamb')

# # Add titles and labels
# plt.title('Area Plot of GHI, DNI, DHI, and Tamb')
# plt.xlabel('Date')
# plt.ylabel('Values')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.show()

# # Resample data by month and calculate the mean for each variable

# df_benin['Timestamp'] = pd.to_datetime(df_benin['Timestamp'], errors='coerce')

# # Drop rows where 'Timestamp' could not be converted
# df_benin = df_benin.dropna(subset=['Timestamp'])

# # Set 'Timestamp' as the index
# df_benin.set_index('Timestamp', inplace=True)

# monthly_data = df_benin.resample('ME').mean()

# plt.figure(figsize=(20, 8))

# # Line plots for monthly averages
# plt.plot(monthly_data.index, monthly_data['GHI'], label='GHI', color='orange')
# plt.plot(monthly_data.index, monthly_data['DNI'], label='DNI', color='blue')
# plt.plot(monthly_data.index, monthly_data['DHI'], label='DHI', color='green')
# plt.plot(monthly_data.index, monthly_data['Tamb'], label='Tamb', color='red')

# # Add titles and labels
# plt.title('Monthly Average of GHI, DNI, DHI, and Tamb')
# plt.xlabel('Month')
# plt.ylabel('Average Values')
# plt.legend()

# # Set x-axis major locator and formatter for month-year format
# plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# # Rotate and format date labels to fit all months
# plt.gcf().autofmt_xdate()

# # Add grid
# plt.grid(True)

# # Show the plot
# plt.show()

# # Extract hour from datetime index

# # Group by hour and calculate the mean for each variable

# df_benin.index = pd.to_datetime(df_benin.index)

# # Create a new column 'Hour' by extracting the hour from the index
# df_benin['Hour'] = df_benin.index.hour

# # Now, you can group by the 'Hour' column
# hourly_data = df_benin.groupby('Hour').mean()

# plt.figure(figsize=(14, 8))

# # Line plots for hourly averages
# plt.plot(hourly_data.index, hourly_data['GHI'], label='GHI', color='orange')
# plt.plot(hourly_data.index, hourly_data['DNI'], label='DNI', color='blue')
# plt.plot(hourly_data.index, hourly_data['DHI'], label='DHI', color='green')
# plt.plot(hourly_data.index, hourly_data['Tamb'], label='Tamb', color='red')

# # Add titles and labels
# plt.title('Hourly Average of GHI, DNI, DHI, and Tamb')
# plt.xlabel('Hour of the Day')
# plt.ylabel('Average Values')
# plt.legend()
# plt.grid(True)

# # Show the plot
# plt.show()
