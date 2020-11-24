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