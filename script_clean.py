import pandas as pd
import numpy as np

sf = pd.read_csv(r'Data_Job_SF.csv')
ny = pd.read_csv(r'Data_Job_NY.csv')
tx = pd.read_csv(r'Data_Job_TX.csv')
wa = pd.read_csv(r'Data_Job_WA.csv')


def clean_rows(x):
    '''
    Removing all rows with -1 values for Min_Salary and Max_salary column
    and getting x_clean dataframe.
    '''
    assert isinstance(x, pd.core.frame.DataFrame)
    ind_fmin = x[x['Min_Salary'] == -1].index.values
    ind_fmax = x[x['Max_Salary'] == -1].index.values
    ind_f = np.union1d(ind_fmin, ind_fmax)
    x_clean = x.drop(index=ind_f)
    ind_fmin = x_clean[x_clean['Min_Salary'] == -1].index.values
    ind_fmax = x_clean[x_clean['Max_Salary'] == -1].index.values
    assert len(ind_fmin) == 0 or len(ind_fmax) == 0
    return x_clean


def merge_field(field, df_list):
    '''
    Groups the datas from df_list into different csvs as per field
    '''
    assert isinstance(field, str)
    assert isinstance(df_list, list)

    grp = []
    ind = []

    for i, df in enumerate(df_list):
        assert isinstance(df, pd.core.frame.DataFrame)
        grp.append(df.groupby(field))
        ind.append(grp[i].all().index.values)

    all_ind = np.array([])

    for j in ind:
        all_ind = np.union1d(all_ind, j)

    m_grp = pd.DataFrame()

    for i in all_ind:
        m_grp = pd.DataFrame()
        for j, g_df in enumerate(grp):
            if i in ind[j]:
                m = g_df.get_group(i)
                m_grp = pd.concat([m, m_grp], ignore_index=True, sort=False)
        csv_name = i + '.csv'
        m_grp.to_csv(csv_name)
    pass


sf_clean = clean_rows(sf)
ny_clean = clean_rows(ny)
tx_clean = clean_rows(tx)
wa_clean = clean_rows(wa)

df_list = [sf_clean, tx_clean, wa_clean, ny_clean]
merge_field('Industry', df_list)