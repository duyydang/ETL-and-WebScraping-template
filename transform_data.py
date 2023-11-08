def transform_data(df):
    values = df['MC_USD_Billion']
    # Adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places
    df['MC_GBP_Billion'] = round(values * 0.8, 2)
    df['MC_EUR_Billion'] = round(values * 0.93, 2)
    df['MC_INR_Billion'] = round(values * 82.95, 2)

    return df
