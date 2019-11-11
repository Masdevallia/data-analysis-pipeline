
# Data cleaning related functions:

def resub_list(array, sub_before, sub_after):
    '''
    re.sub for e in array
    '''
    import re
    return [re.sub(sub_before,sub_after,e) for e in array]


def delete_outliers(df, cutoff):
    '''
    Deleting otliers from a dataframe
    Return a list containing the rows to delete (outliers) from the dataframe
    '''
    import pandas as pd
    stats = df.describe().transpose()
    stats['IQR'] = stats['75%'] - stats['25%']
    outliers = pd.DataFrame(columns=df.columns)
    for col in stats.index:
        iqr = stats.at[col,'IQR']
        cutoff = iqr * cutoff
    lower = stats.at[col,'25%'] - cutoff
    upper = stats.at[col,'75%'] + cutoff
    results = df[(df[col]<lower)|(df[col]>upper)].copy()
    results['Outlier'] = col
    outliers = outliers.append(results)
    rowstodelete = list(set(outliers.index))
    return rowstodelete