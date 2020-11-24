##==========WORD CLOUD FUNCTIONS==========##

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


##==========BOX AND WHISKER FUNCTIONS==========##

def merge_MinMax_Salary(in_df):
    """
    Description:    Take job-data dataframe with Min_Salary and Max_Salary columns, and change to dataframe with
                    Salary column, and a new "Min_Max" column with 'min' or 'max' as value. For box & whisker plotting purposes
    :Warning in_df: this function is intended for data set specific to team19, FA20, ece143 final project
    :param in_df:   in_df is dataframe, must have column of strings titled "Job_Desc"
    :type in_df:    in_df must be type pd.DataFrame
    """
    import pandas as pd
    assert isinstance(in_df,pd.DataFrame), ':type in_df: in_df must be pd.DataFrame type'
    assert "Min_Salary" in in_df, "no 'Min_Salary' column in input dataframe 'in_df'"
    assert "Max_Salary" in in_df, "no 'Max_Salary' column in input dataframe 'in_df'"
    assert "Job_title" in in_df, "no 'Job_title' column in input dataframe 'in_df'"
    assert "Company" in in_df, "no 'Company' column in input dataframe 'in_df'"
    assert "State" in in_df, "no 'State' column in input dataframe 'in_df'"
    assert "City" in in_df, "no 'City' column in input dataframe 'in_df'"
    assert "Job_Desc" in in_df, "no 'Job_Desc' column in input dataframe 'in_df'"
    assert "Industry" in in_df, "no 'Industry' column in input dataframe 'in_df'"
    assert "Rating" in in_df, "no 'Rating' column in input dataframe 'in_df'"
    assert "Date_Posted" in in_df, "no 'Date_Posted' column in input dataframe 'in_df'"
    assert "Valid_until" in in_df, "no 'Valid_until' column in input dataframe 'in_df'"
    assert "Job_Type" in in_df, "no 'Job_Type' column in input dataframe 'in_df'"

    # create new dataframe without max salary and industry column
    in_df_minmax_low = in_df[["Job_title","Company","State","City","Min_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]].copy()
    # rename Min_Salary to be Salary
    in_df_minmax_low.rename(columns={"Min_Salary":"Salary"},inplace=True)
    # add Min_Max column full of "min" indicating Salary is min salary 
    in_df_minmax_low["Min_Max"]="min"
    
    # create new dataframe without min salary and industry columns
    in_df_minmax_high = in_df[["Job_title","Company","State","City","Max_Salary","Job_Desc","Industry","Rating","Date_Posted","Valid_until","Job_Type"]].copy()
    # rename Max_Salary to be Salary
    in_df_minmax_high.rename(columns={"Max_Salary":"Salary"},inplace=True)
    # add Min_Max column full of "max" indicating Salary is max salary 
    in_df_minmax_high["Min_Max"]="max"

    #join the two dataframes
    frames = [in_df_minmax_low, in_df_minmax_high]
    in_df_minmax = pd.concat(frames)
    #filter to remove all non-data science rows
    in_df_minmax_filtered = in_df_minmax[in_df_minmax['Salary'] >= 0]
    return in_df_minmax_filtered

def count_members_by_column(in_df, col):
    """
    Description:    Takes dataframe in_df, and returns a single dataframe with count of members in a column 'col'

    :param in_df:   in_df is dataframe, must have column of strings titled "Job_Desc"
    :type in_df:    in_df must be type DataFrame
    :param col:     col must be string matching column value of in_df
    :type col:      col must be of type str
    """
    import pandas as pd
    assert isinstance(in_df,pd.DataFrame), ':type in_df: in_df must be pd.DataFrame type'
    assert isinstance(col,str), ":type col: col must be of type str"

    df_count = in_df[col]      #series with only industries column
    list_colCount = df_count.tolist()  #smash to list
    set_colCount = set(list_colCount)    #remove duplicates
    indices = list(set_colCount)
    indices = [x for x in indices if str(x) != 'nan'] #remove any nan rows
    indices_count = []
    for item in indices:
        strCount = df_count.str.count(item)
        indices_count.append(strCount.sum())

    df_col={"count":indices_count}
    df_occurances = pd.DataFrame(data=df_col,index=indices) # correlate count to industry listed
    df_occurances = df_occurances.sort_values("count") # sort dataframe by occurances
    return(df_occurances)