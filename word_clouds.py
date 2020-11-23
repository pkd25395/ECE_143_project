"""
DO THIS FOR ONLY for TOP 5 Industries: 
INDUSTRY                            COUNT
Finance                             181.0
Health Care                         193.0
Biotech & Pharmaceuticals           289.0
Business Services                   310.0
Information Technology              508.0

AND FOR TOP 5 COMPANIES of those Industries:
COMPANY                         COUNT
Forescout Technologies Inc.        60 (Not Great)
Banfield Pet Hospital              60 (NO GOOD)
Booz Allen Hamilton                80
Genentech                         118
Veterinary Emergency Group        120 (Not Great)
National Debt Relief              120
"""

def remove_non_keywords(in_str,kwd_list):
    """ 
    Description: Takes in_str, and returns a string with only words from kwd_list
    :param in_str:      in_str is string desired to be reduced to instances of key-words in kwd_list
    :type in_str:       in_str myst be type str
    :param kwd_list:    kwd_list is list of strings to be kept in in_str
    :type kwd_list:     kwd_list must be type list with elements of type str
    """
    assert isinstance(in_str,str), ":type in_str:       in_str myst be type str"
    assert isinstance(kwd_list,list), ":type kwd_list:     kwd_list must be type list"
    for elem in kwd_list:
        assert isinstance(elem,str),":type kwd_list:     kwd_list elements must be of type str"
    
    in_str = in_str.lower()
    in_str = in_str.split(" ")
    result_list = []
    for kwd in kwd_list:
        for wrd in in_str:
            if kwd==wrd:
                result_list.append(wrd)
            else:
                pass
    result_str = " ".join(result_list)
    return(result_str)

def create_JobDescription_string(in_df, col, target):
    """
    Description:    Takes dataframe in_df, and returns a single string with all job description values, new-lines removed,
                    corresponding to rows with value 'target' in collumn 'col'.
    :param in_df:   in_df is dataframe, must have column of strings titled "Job_Desc"
    :type in_df:    in_df must be type DataFrame
    :param col:     col must be string matching column value of in_df
    :type col:      col must be of type str
    :param target:  target must be string, must be a value in stipulated column
    :type target:   target must be of type str
    """
    import pandas as pd
    assert isinstance(in_df,pd.DataFrame), ':type in_df: in_df must be pd.DataFrame type'
    assert "Job_Desc" in in_df, "no 'Job_Desc' column in input dataframe 'in_df'"
    #assert target in in_df[col], "'target' value not present in 'col' column of 'in_df'"
    
    #split into dataframes by col:
    df_grouped = in_df.groupby(in_df[col]) #create groupby object
    #create dataframes for specified target value in column
    df_target = df_grouped.get_group(target)
    #create job description string for target
    str_target = " ".join(df_target["Job_Desc"].tolist()).lower()
    #remove newline characters
    str_target = str_target.replace("\n"," ")
    #return string
    return(str_target)

def generate_and_display_wordcloud(in_str,chart_title,img_path):
    """
    Description:    Takes dataframe in-str, generates WordCloud object and displays wordcloud for 'in-str'.
                    in particular this is for team 19, FA20, ECE143 project
    :Warning Cls:       must install wordcloud 'conda install -c conda-forge wordcloud'
    :param in_str:      in_str must be string of words
    :type in_str:       in_str must be type str
    :param chart_title: chart_title should be title of graph
    :type chart_title:  chart_title must be type str
    """
    # conda install -c conda-forge wordcloud
    from wordcloud import WordCloud, STOPWORDS
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    assert isinstance(in_str,str), ":type in_str:   in_str must be type str"
    assert isinstance(chart_title,str), ":type chart_title:   in_str must be type str"

    cloud_mask = np.array(Image.open(img_path))

    wordcloud_object = WordCloud(mask=cloud_mask, collocations=False, min_font_size=5, max_font_size=100, 
                                max_words=None, background_color="white", margin=0, 
                                font_step=1).generate(in_str)
    plt.figure()
    plt.imshow(wordcloud_object, interpolation='bilinear')
    plt.title(chart_title)
    plt.axis("off")
    plt.margins(x=0,y=0)
    plt.show()

import pandas as pd


#import .csvs as dataframes
col_list = ["Job_title","Company","State","City","Min_Salary","Max_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]
files_list = ["Data_Job_NY.csv"
                ,"Data_Job_SF.csv"
                ,"Data_Job_TX.csv"
                ,"Data_Job_WA.csv"]
df_NY = pd.read_csv(files_list[0],usecols=col_list)
df_SF = pd.read_csv(files_list[1],usecols=col_list)
df_TX = pd.read_csv(files_list[2],usecols=col_list)
df_WA = pd.read_csv(files_list[3],usecols=col_list)
df_NY = df_NY[df_NY['Max_Salary'] >= 0] # remove non-data science jobs from dataset
df_SF = df_SF[df_SF['Max_Salary'] >= 0]
df_TX = df_TX[df_TX['Max_Salary'] >= 0]
df_WA = df_WA[df_WA['Max_Salary'] >= 0]

#create df only Job Desc and Industry
#df_NY_2col = df_NY[["Job_Desc","Industry"]].copy()
#df_SF_2col = df_SF[["Job_Desc","Industry"]].copy()
#df_TX_2col = df_TX[["Job_Desc","Industry"]].copy()
#df_WA_2col = df_WA[["Job_Desc","Industry"]].copy()

#join all above dataframes into one dataframe
#frames_all = [df_NY_2col, df_SF_2col, df_TX_2col, df_WA_2col]
frames_all = [df_NY, df_SF, df_TX, df_WA]
df_combined = pd.concat(frames_all)

##===================BY INDUSTRY===================##

#create string of all Job_Desc values by Industry, from combined dataframe.
## Health Care
str_HealthCare = create_JobDescription_string(df_combined,"Industry","Health Care")
## Finance 
str_Finance = create_JobDescription_string(df_combined,"Industry","Finance")
## IT
str_IT = create_JobDescription_string(df_combined,"Industry","Information Technology")
## Biotech
str_Biotech = create_JobDescription_string(df_combined,"Industry","Biotech & Pharmaceuticals")
## Business
str_Business = create_JobDescription_string(df_combined,"Industry","Business Services")

keyword_list = ["models","statistics","probability","machine learning","data science","numpy","pandas","sql","scikit-learn","r","databases","database","team",
"MSc","PhD","mathematics","computer science","physics","research","data","relational databases","python","c++","matlab","modeling","dbt","snowflake",
"mode analytics","fivetran","Census","amplitude","segment","tensorflow","optimization","prediction","engineering","data engineering","neural networks",
"bigquery","pyspark","degree","bachelor","bachelors","scala","data analysis","analysis","data visualization","algorithms","classification",
"model","java","javascript","caffe","deep learning","data processing","hpc","hadoop","ms","bs","m.s.","b.s.","masters","master","stem","postgres",
"software development","agile","querying","experience","skills","credentials","hands-on","communication","presentation","ownership"]

#remove all non-keywords from job descriptions for:
## Health Care
str_HealthCare = remove_non_keywords(str_HealthCare, keyword_list)
## Finance 
str_Finance = remove_non_keywords(str_Finance, keyword_list)
## IT
str_IT = remove_non_keywords(str_IT, keyword_list)
## Biotech
str_Biotech = remove_non_keywords(str_Biotech, keyword_list)
## Business
str_Business = remove_non_keywords(str_Business, keyword_list)

#create wordcloud object for:
## Health Care
generate_and_display_wordcloud(str_HealthCare,"Health Care","cloud.png") #8iGbRApyT.png")
## Finance
generate_and_display_wordcloud(str_Finance,"Finance","cloud.png") #dollar.jpg")
## IT
generate_and_display_wordcloud(str_IT,"Information Technology","cloud.png") #cursor.jpg")
## Biotech
generate_and_display_wordcloud(str_Biotech,"Biotech & Pharmaceuticals","cloud.png") #flask.jpg")
## Business
generate_and_display_wordcloud(str_Business,"Business Services","cloud.png") #tie.jpg")

##===================BY COMPANY===================##

#create string of all Job_Desc values by Company, from combined dataframe.
## Forescout Technologies Inc.
str_Forescout = create_JobDescription_string(df_combined,"Company","Forescout Technologies Inc.")
## Booz Allen Hamilton 
str_Booz = create_JobDescription_string(df_combined,"Company","Booz Allen Hamilton")
## Genentech
str_Genentech = create_JobDescription_string(df_combined,"Company","Genentech")
## Veterinary Emergency Group
str_Veterinary = create_JobDescription_string(df_combined,"Company","Veterinary Emergency Group")
## National Debt Relief
str_National = create_JobDescription_string(df_combined,"Company","National Debt Relief")

#remove all non-keywords from job descriptions for:
## Forescout Technologies Inc.
str_Forescout = remove_non_keywords(str_Forescout, keyword_list)
## Booz Allen Hamilton 
str_Booz = remove_non_keywords(str_Booz, keyword_list)
## Genentech
str_Genentech = remove_non_keywords(str_Genentech, keyword_list)
## Veterinary Emergency Group
str_Veterinary = remove_non_keywords(str_Veterinary, keyword_list)
## National Debt Relief
str_National = remove_non_keywords(str_National, keyword_list)

#create wordcloud object for:
## Forescout Technologies Inc.
generate_and_display_wordcloud(str_Forescout,"Forescout Technologies Inc.","cloud.png") #8iGbRApyT.png")
## Booz Allen Hamilton
generate_and_display_wordcloud(str_Booz,"Booz Allen Hamilton","cloud.png") #dollar.jpg")
## Genetech
generate_and_display_wordcloud(str_Genentech,"Genentech","cloud.png") #cursor.jpg")
## Veterinary Emergency Group
generate_and_display_wordcloud(str_Veterinary,"Veterinary Emergency Group","cloud.png") #flask.jpg")
## National Debt Relief
generate_and_display_wordcloud(str_National,"National Debt Relief","cloud.png") #tie.jpg")