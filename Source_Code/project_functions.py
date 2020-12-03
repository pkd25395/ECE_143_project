
import pandas as pd
import numpy as np
import altair as alt
from collections import OrderedDict
from math import log, sqrt
import matplotlib.pyplot as plt
from math import pi

from altair import Chart
from bokeh.plotting import figure, output_file, show

##==========WORD CLOUD FUNCTIONS==========##

def clean_data(x):
    '''
    Cleaning data by removing spurious entries 
    :x: dataframe 
    returns clean dataframe 
    :author: Pratyush Dwivedi 
    '''
    assert isinstance(x, pd.core.frame.DataFrame)
    ind_fmin = x[x['Min_Salary'] == -1].index.values
    ind_fmax = x[x['Max_Salary'] == -1].index.values
    ind_f = np.union1d(ind_fmin, ind_fmax)
    x_clean = x.drop(index=ind_f)
    ind_fmin = x_clean[x_clean['Min_Salary'] == -1].index.values
    ind_fmax = x_clean[x_clean['Max_Salary'] == -1].index.values
    assert len(ind_fmin) == 0 or len(ind_fmax) == 0

    rm_wlist = ['Ultrasound', 'Veterinarian', 'Veterinary', 'mechanic', 'Therapist', 'Mechanic',
                'Regional Vice President',
                'ADVOCACY', 'Construction', 'LPN']

    a = x_clean.groupby('Job_title')
    m = a.all().index.values
    f = []
    for j in rm_wlist:
        for k in m:
            if (j in k):
                f.append(k)
    for i in f:
        ind = x_clean[x_clean['Job_title'] == i].index.values
        x_clean = x_clean.drop(index=ind)

    return x_clean


def clean_and_merge(x_list):
    '''
    Cleaning and merging data. 
    :x_list: list of dataframes 
    returns a merged dataframe 
    :author: Pratyush Dwivedi 
    '''
    assert isinstance(x_list, list)

    m_data = pd.DataFrame()

    for i in x_list:
        assert isinstance(i, pd.core.frame.DataFrame)
        c_data = clean_data(i)
        m_data = pd.concat([c_data, m_data], ignore_index=True, sort=False)

    return m_data


def merge_field(field, df_list):
    '''
    Groups the datas from df_list into a dictionary as per field 
    :field: field according to which data is to be splitted 
    :df_list: list of clean_data 
    returns a dictionary of separated datasets 
    :author: Pratyush Dwivedi 
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

    dict_all = {}

    for i in all_ind:
        m_grp = pd.DataFrame()
        for j, g_df in enumerate(grp):
            if i in ind[j]:
                m = g_df.get_group(i)
                m_grp = pd.concat([m, m_grp], ignore_index=True, sort=False)
        dict_all[i] = m_grp
    return dict_all

def remove_non_keywords(in_str,kwd_list):
    """ 
    Description: Takes in_str, and returns a string with only words from kwd_list. 
    :param in_str:      in_str is string desired to be reduced to instances of key-words in kwd_list 
    :type in_str:       in_str myst be type str 
    :param kwd_list:    kwd_list is list of strings to be kept in in_str 
    :type kwd_list:     kwd_list must be type list with elements of type str 
    :author: Harker Russell
    """
    assert isinstance(in_str,str), ":type in_str:       in_str myst be type str"
    assert isinstance(kwd_list,list), ":type kwd_list:     kwd_list must be type list"
    for elem in kwd_list:
        assert isinstance(elem,str),":type kwd_list:     kwd_list elements must be of type str"
    
    in_str = in_str.lower()
    in_str = in_str.split(" ")
    result_list = []
    for wrd in in_str:
        if wrd in kwd_list:
            result_list.append(wrd)
        else:
            pass

    result_list = [i for i in result_list if len(i) > 2]
    #print(result_list)
    result_str = " ".join(result_list)
    #result_str = "+".join(result_list)
    #print(result_str)
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
    :author: Harker Russell
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
                    in particular this is for team 19, FA20, ECE143 project. 
    :Warning Req:       must install wordcloud 'conda install -c conda-forge wordcloud' 
    :param in_str:      in_str must be string of words 
    :type in_str:       in_str must be type str 
    :param chart_title: chart_title should be title of graph 
    :type chart_title:  chart_title must be type str 
    :author: Harker Russell 
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
                                font_step=1,).generate(in_str)#regexp=r"\w[\w' ]+").generate(in_str)
    plt.figure(figsize=(12,8))
    plt.imshow(wordcloud_object, interpolation='bilinear')
    plt.title(chart_title)
    plt.axis("off")
    plt.margins(x=0,y=0)
    plt.show()


##==========BOX AND WHISKER FUNCTIONS==========##

def merge_MinMax_Salary(in_df):
    """
    Description:    Take job-data dataframe with Min_Salary and Max_Salary columns, and change to dataframe with
                    Salary column, and a new "Min_Max" column with 'min' or 'max' as value. For box & whisker plotting purposes. 
    :Warning in_df: this function is intended for data set specific to team19, FA20, ece143 final project 
    :param in_df:   in_df is dataframe, must have column of strings titled "Job_Desc" 
    :type in_df:    in_df must be type pd.DataFrame 
    :author: Harker Russell 
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
    Description:    Takes dataframe in_df, and returns a single dataframe with count of members in a column 'col'. 
    :param in_df:   in_df is dataframe, must have column of strings titled "Job_Desc" 
    :type in_df:    in_df must be type DataFrame 
    :param col:     col must be string matching column value of in_df 
    :type col:      col must be of type str 
    :author: Harker Russell 
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

def gen_and_disp_boxWhiskerPlot(in_df,chart_title,x_col,y_col,hue_col):
    """
    Description:    Takes dataframe in-str, generates WordCloud object and displays wordcloud for 'in-str'.
                    in particular this is for team 19, FA20, ECE143 project. 
    :param in_df:       in_df is dataframe, must have column of strings titled "Job_Desc" 
    :type in_df:        in_df must be pd.DataFrame type. 
    :param chart_title: chart_title should be title of graph. 
    :type chart_title:  chart_title must be of type str. 
    :param x_col:       x_col must be string, column of df.  
    :type x_col:        x_col must be of type str.   
    :param y_col:       y_col must be string, column of df.  
    :type y_col:        y_col must be of type str. 
    :param hue_col:     hue_col must be string, column of df. 
    :type hue_col:      hue_col must be of type str. 
    :author: Harker Russell 
    """
    # conda install -c conda-forge wordcloud
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    assert isinstance(in_df,pd.DataFrame), ':type in_df: in_df must be pd.DataFrame type'
    assert isinstance(chart_title,str), ":type chart_title:   in_str must be type str"
    assert isinstance(x_col,str), ":type x_col: x_col must be of type str"
    assert x_col in in_df, "no x_col column in input dataframe 'in_df'"
    assert isinstance(y_col,str), ":type y_col: y_col must be of type str"
    assert y_col in in_df, "no y_col column in input dataframe 'in_df'"
    assert isinstance(hue_col,str), ":type hue_col: y_col must be of type str"
    assert hue_col in in_df, "no hue_col column in input dataframe 'in_df'"

    sns.set(font_scale=1.1)
    plt.figure(figsize=(12,8))
    sns.boxplot( x=in_df[x_col], y=in_df[y_col], hue=in_df[hue_col])
    plt.title(chart_title) #1300x850
    plt.show()

##==========SCATTERPLOT FUNCTIONS==========##
def salary_v_rating_scatter(df_chart, legend, separate=False):
    """
    Description:    Create an altair chart for a salary vs rating scatterplot. 
    :param df_chart:   Dataframe of job listings with both salaries and ratings that will be used to make chart object 
    :type df_chart:    pandas.DataFrame 
    :param legend:     How we want plot to be organized i.e. by industry
    :type legend:      str in cols
    :author: Jake Kim 
    """
    cols = ['Job_title', 'Company', 'State', 'City', 'Min_Salary', 'Max_Salary', 
            'Job_Desc', 'Industry', 'Rating', 'Date_Posted', 'Valid_until', 'Job_Type']
    assert isinstance(df_chart, pd.DataFrame)
    assert legend in cols
    
    avg_sal = list()
    for i in range(df_chart.shape[0]):
        assert df_chart.loc[i,'Max_Salary'] > 0
        assert df_chart.loc[i,'Min_Salary'] > 0
        avg_sal.append((df_chart.loc[i,'Max_Salary']+df_chart.loc[i,'Min_Salary'])/2)
    
    df_chart['Avg_Salary'] = avg_sal
    
    df_chart = Chart(df_chart)
    
    if separate:
        chart = df_chart.mark_point().encode(x='Avg_Salary',y='Rating',color=legend,column=legend)
    else:
        chart = df_chart.mark_point().encode(x='Avg_Salary',y='Rating',color=legend)
    
    chart = chart.properties(title = 'Salary vs. Company Ratings')
    
    return chart

def salary_v_listings_scatter(df_chart, legend, separate=False):
    """
    Description:    Create an altair chart for a salary vs job listings scatterplot
        
    :param df_chart:   Dataframe of job listings with both salaries and listings that will be used to make chart object
    :type df_chart:    pandas.DataFrame
    :param legend:     How we want plot to be organized i.e. by industry
    :type legend:      str in cols
    :author: Jake Kim 
    """
    cols = ['Job_title', 'Company', 'State', 'City', 'Min_Salary', 'Max_Salary', 
           'Job_Desc', 'Industry', 'Rating', 'Date_Posted', 'Valid_until', 'Job_Type']
    assert legend in cols
    assert isinstance(df_chart, pd.DataFrame)
    
    listings = list(df_chart[legend])
    listing_set = set(listings)
    list_dict = dict.fromkeys(listing_set, 0)
    
    for i in range(len(listings)):
        list_dict[listings[i]] += 1
    
    entries = list()
    for i in range(df_chart.shape[0]):
        entries.append(list_dict[df_chart.loc[i,legend]])
    
    df_chart['Listings'] = entries
    
    avg_sal = list()
    for i in range(df_chart.shape[0]):
        assert df_chart.loc[i,'Max_Salary'] > 0
        assert df_chart.loc[i,'Min_Salary'] > 0
        avg_sal.append((df_chart.loc[i,'Max_Salary']+df_chart.loc[i,'Min_Salary'])/2)
    
    df_chart['Avg_Salary'] = avg_sal
    
    df_chart = Chart(df_chart)
    
    if separate:
        chart = df_chart.mark_point().encode(x='Listings',y='Avg_Salary',color=legend,column=legend)
    else:
        chart = df_chart.mark_point().encode(x='Listings',y='Avg_Salary',color=legend)
    
    chart = chart.properties(title = 'Salary vs. # of Job Lstings')
        
    return chart
        
#=======================Radial Column Chart====================================#
def plot_radial_column_chart(df,min_scale,max_scale):
    '''
    This function reading the dataframe and plot the corresponding radial column chart
    ----------
    df : A corresponding dataframe that needs to be plot

    '''
    assert isinstance(df,pd.DataFrame), 'input needs to be a pandas dataframe'
    assert isinstance(min_scale,int) and isinstance(max_scale,int), 'min scale and max scale needs to be int'
    
    # set company bar color
    companys = [column for column in df.columns]
    companys = companys[1::]
    colors = ["#0d3362","#c64737", "black" ] * 5
    company_color = OrderedDict({companys[i]:colors[i] for i in range(len(companys))})
    print()
    
    # set industry section color
    industry_color = OrderedDict([
    ("Asrospace", "#FFFFE0"), # Yellow
    ("Finance", "#FF69B4"), # Pink
    ("Biotech", "#9370DB"),  # Purple
    ("Business", "#00BFFF"), # Blue
    ("InfoTech", "#F0FFF0"), # Green
    ])
    
    # adjust graph board size
    width = 1000
    height = 1000
    # adjust graph circule size
    inner_radius = 50           
    outer_radius = 350 
    
    # magic equal that scale the value to the radius (I don't know how it works)
    # minr = min_scale you want for the data (be reasonable)
    # maxr = max_scale you want for the data (be reasonable)
    minr = sqrt(log(min_scale * 1E4))
    maxr = sqrt(log(max_scale * 1E4))
    a = (outer_radius - inner_radius) / (minr - maxr)
    b = inner_radius - a * maxr

    def rad(mic):
        return abs(a * np.sqrt(np.log(mic * 1E4)) + b)

    big_angle = 2.0 * np.pi / (len(df) + 1 ) # divide the circules based on the length of df(sections)
    small_angle = big_angle / 7 # divide the sections again for bar positions
    
    # create the figure and plot the background
    p = figure(plot_width=width, plot_height=height, title="",
               x_axis_type=None, y_axis_type=None,
               x_range=(-420, 420), y_range=(-420, 420),
               min_border=0, outline_line_color="black",
               background_fill_color="#f0e1d2")


    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # plot the sections circule
    # angle for each sections
    angles = np.pi/2 - big_angle/2 - df.index.to_series()*big_angle 
    # color for each sections
    colors = [industry_color[industry] for industry in df.Industry]
    p.annular_wedge(
        0, 0, inner_radius, outer_radius, -big_angle+angles, angles, color=colors,
        )   


    # radial axes

    p.annular_wedge(0, 0, inner_radius-10, outer_radius+10,
                -big_angle+angles, -big_angle+angles, color="black")
    
    # circular axes and lables

    labels = [scale for scale in range(0,180000,20000)]
    radii = [inner_radius + outer_radius*scale//max_scale for scale in range(0,max_scale - 1000,1000)]
    p.circle(0, 0, radius=radii, fill_color=None, line_color="black")
    

    

    p.text(0, radii[:-1], ['$' + str(r) for r in labels[:-1]],
       text_font_size="11px", text_align="center", text_baseline="middle")
    
    
    # plot the company bars
    
    company_index = 0
    for section in range(len(angles)):
        company_angle = angles[section]
        company_rad = rad(df[companys[company_index]])[section]
        company = companys[company_index]
        company_index += 1 
        
        p.annular_wedge(0, 0, inner_radius, company_rad,
                -big_angle+company_angle+5*small_angle, -big_angle+company_angle+6*small_angle,
                color=company_color[company])

        company_rad = rad(df[companys[company_index]])[section]
        company = companys[company_index]
        company_index += 1 
        p.annular_wedge(0, 0, inner_radius, company_rad,
                -big_angle+company_angle+3*small_angle, -big_angle+company_angle+4*small_angle,
                color=company_color[company])
        
        company_rad = rad(df[companys[company_index]])[section]
        company = companys[company_index]
        company_index += 1 
        p.annular_wedge(0, 0, inner_radius, company_rad,
                -big_angle+company_angle+1*small_angle, -big_angle+company_angle+2*small_angle,
                color=company_color[company])
    


    # industry labels
    labels = np.power(10.0, np.arange(3, 4))
    radii = a * np.sqrt(np.log(labels * 1E4)) + b
    xr = radii[0]*np.cos(np.array(-big_angle/2 + angles))
    yr = radii[0]*np.sin(np.array(-big_angle/2 + angles))
    label_angle=np.array(-big_angle/2+angles)
    label_angle[label_angle < -np.pi/2] += np.pi # easier to read labels on the left side
    p.text(xr, yr, df['Industry'], angle=label_angle,
       text_font_size="12px", text_align="center", text_baseline="middle")

    # OK, these hand drawn legends are pretty clunky, will be improved in future release
    industry_legends_x = [-400,-400,-200,-200,0]
    industry_legends_y = [400,350,400,350,400]
    p.circle(industry_legends_x, industry_legends_y, color=list(industry_color.values()), radius=5)
    
    industry_legends_x = [ x + 10 for x in industry_legends_x]
    p.text(industry_legends_x, industry_legends_y, text=["Industry-" + industry for industry in industry_color.keys()],
           text_font_size="9px", text_align="left", text_baseline="middle")
    
    
    # company labels
    company_labels_x = [-400,-400,-400,-400,-400,-400,-200,-200,-200,-200,-200,-200,0,0,0]
 
    company_labels_y = [390,380,370,340,330,320,390,380,370,340,330,320,390,380,370]
    p.circle(company_labels_x, company_labels_y,color=list(company_color.values()), radius=3)
    
    company_labels_x = [x + 10 for x in company_labels_x] 
    
    company_salary = {company:str(df[company].iloc[0])  for company in company_color.keys()}
    
    p.text(company_labels_x, company_labels_y, text=["" + company + ':  $' + company_salary[company] for company in company_color.keys()],
       text_font_size="9px", text_align="left", text_baseline="middle")
    
    show(p)
        
#==============================RadarChart=======================================#

def plot_job_title_radar(ind, data, yt, yl):
    '''
    This function plots the radar chart for top 5 job title in the industry ind
    ind : string indicating name of industry
    data: dataframe corresponding to the industry
    yt: list indicating the yticks
    yl: int indicating limit of y axis
    author: Pratyush Dwivedi
    '''
    assert isinstance(ind, str)
    assert isinstance(yt, list)
    assert isinstance(yl, int)
    assert isinstance(data, pd.core.frame.DataFrame)

    grp = data.groupby('Job_title')
    m = grp.all().index.values
    cdict = {}
    for i in m:
        a = grp.get_group(i)
        cdict[i] = a.shape[0]
    sortdic = sorted(cdict.items(), key=lambda x: x[1], reverse=True)

    ff = sortdic[:10]

    fdict = {}
    for i in ff:
        fdict[i[0]] = i[1]

    fig = plt.figure()
    ax = plt.subplot(polar="True")
    catg = list(fdict.keys())[:5]
    vals = list(fdict.values())[:5]
    vals += vals[:1]
    N = len(catg)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    plt.polar(angles, vals, marker='o', linewidth=1)
    plt.fill(angles, vals, alpha=0.2)

    plt.xticks(angles[:-1], catg)
    if (yt):
        plt.yticks(yt, color="grey")
    if (yl != -1):
        plt.ylim(0, yl)

    title = f'Top 5 job posted in {ind}'
    plt.title(title)

    plt.show()
        
    