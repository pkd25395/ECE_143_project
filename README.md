![data to vis](https://github.com/pkd25395/ECE_143_project/blob/main/RM_Images/data-to-vis.png)  
# ECE_143_project
## Project Description
  
### Analysis  and Visualization of Current Job Postings in Data Science Field
This project creates data visualization for a dataset of glassdoor job postings in the data science field, as found in [this kaggle set](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data). The goal of this project is to help inform and provide insight to data science majors nearing graduation.

This code uses custom python function definitions (`project_functions.py`) to import, clean and concatenate four discrete datasets (from csv format to pandas dataframes) from different regions in python scripts.  

![data process](https://github.com/pkd25395/ECE_143_project/blob/main/RM_Images/data_process.png)
![other process](https://github.com/pkd25395/ECE_143_project/blob/main/RM_Images/other_process.png)

Each script does visualization specific data manipulation to generate plots (i.e. one script for each style of visualization) to parse and present the data in more intuitive ways.  
 
`project_plots.ipynb` can be ran step-by-step to illustrate the process.
     
Please see instructions and requirements below.

## File Structure

### File Structure Detail
***ECE_143_project***: Main repo directory
1. **Plots**: Directory containing all plots generated for presentation.  
1. **Source_Code**: Source code directory.  
*Note:*\
Each chart/plot has it's own script (e.g. box & whisker plots are generated when `box_and_whisker.py` is ran).  
     - `__init__.py`: Empty file to make directory into a package (allows imports to `project_plots.ipynb` in higher level directory).  
     - `project_functions.py`: All custom functions are located in this file, and imported from this file for use in scripts.  
     - `box_and_whisker.py`: Script that generates box and whisker plots as presented.  
     *Note:*\
     The code used to count 'top 5' industries by job posts are in this script, commented out.\
     The count was done in series so it is included so that our process may be duplicated.  
     - `word_clouds.py`: Script that generates word clouds as presented.  
     - `cloud.png`: Image file used in `word_clouds.py` to create wordcloud mask.  
     - `radial_column_chart.py`: Script that generates radial column chart as presented.  
     - `radar_chart.py`: Script that generates radar charts as presented.  
     - `Data_Job_NY.csv`: New York state'raw' csv file of data scraped from glassdoor--needed to run scripts.  
     - `Data_Job_SF.csv`: San Francisco area 'raw' csv file of data scraped from glassdoor--needed to run scripts.  
     - `Data_Job_TX.csv`: Texas 'raw' csv file of data scraped from glassdoor--needed to run scripts.  
     - `Data_Job_WA.csv`: Washington state 'raw' csv file of data scraped from glassdoor--needed to run scripts.  
     1. **Archive**: Folder for depricated code.
     2. **__pycache__**   
 - `project_plots.ipynb`: jupyter notebook which shows all the visualizations generated for the Team 19 presentation.  
 - `team19_presentation.pdf`: pdf copy of project presentation.
 - `README.md`: Read me file outlining file structure, instructions to run code and required third-party libraries and modules.

 ### Traditional File Structure
 ```
 .
 ├─ Plots                          # Directory containing all plots generated for presentation.
 ├─ Source_Code                    # Source code directory.
 │   ├── __init__.py               # Empty file to make directory into a package
 │   ├── project_functions.py      # All custom functions for this project
 │   ├── box_and_whisker.py        # Script that generates box and whisker plots as presented
 │   ├── word_clouds.py            # Script that generates word clouds as presented
 │   ├── cloud.png                 # Image used for mask in wordcloud function
 │   ├── radial_column_chart.py    # Script that generates radial column chart as presented
 │   ├── radar_chart.py            # Script that generates radar clouts as presented
 │   ├── Data_Job_NY.csv           # Original NY dataset
 │   ├── Data_Job_SF.csv           # Original SF dataset
 │   ├── Data_Job_TX.csv           # Original TX dataset
 │   ├── Data_Job_WA.csv           # Original WA dataset
 │   ├── Archive                   # Directory for depricated source code.
 │   └── __pycache__               # Cache
 ├─ project_plots.ipynb            # Jupyter Notebook for project
 ├─ team19_presentation.pdf        # PDF copy of project presentation
 └── README.md                     # Read-me file for project
 ```



## How to run code
There are two methods to run this code:
#### Run with Jupiter Notebook
1. Open and run `project_plots.ipynb`.  
2. Follow the markdown notes, install requirements (listed below) and run the code cell-by-cell.
3. Plots and Figures will be generated as used in presentation.
#### Run fron Source Code Scripts
1. Ensure all required third party modules (listed below) are installed.
2. Ensure all files located in *Source Code* folder are kept in the same directory (including job data csv files) as outlined above. 
3. Run scripts files to generate plots (e.g. to generate the word clouds used in our presentation, run `word_clouds.py`).  
     - If not addressed here, read script comments which are designed to be helpful if there are any lower-level issues or questions. 
     - *Scatter plots were generated separately in `project_plots.ipynb` due to better compatibility between Jupyter Notebook and Altair

## Required Third Party Libraries and Modules
1. **wordcloud**
 - `conda install -c conda-forge wordcloud`
 - [wordcloud documentation](https://anaconda.org/conda-forge/wordcloud)
2. **seaborn**  
 - `conda install seaborn`
 - `pip install seaborn`
 - [seaborn documentation](https://seaborn.pydata.org/installing.html)  
3. **numpy**  
 - `conda install numpy`  
 - `pip install numpy`  
 - [numpy documentation](https://numpy.org/install/)  
4. **pandas**  
 - `conda install pandas`  
 - `pip install pandas`  
 - [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)  
5. **matplotlib**  
 - `conda install -c anaconda matplotlib`
 - `python -m pip install -U pip`\
    `python -m pip install -U matplotlib`  
 - [matplotlib documentation](https://matplotlib.org/3.3.3/users/installing.html)  
6. **PIL**  
 - `conda install -c anaconda pillow`
 - `python3 -m pip install --upgrade pip`/
    `python3 -m pip install --upgrade Pillow`  
 - [PIL documentation](https://github.com/python-pillow/Pillow/)  
7. **altair**  
 - `conda install -c conda-forge altair`
 - `pip install altair`  
 - [altair documentation](https://altair-viz.github.io/getting_started/installation.html) 
8. **vega**  
 - `conda install vega --channel conda-forge`  
 - `pip install vega`
 - [vega documentation](https://vega.github.io/vega/) 
9. **bokeh**  
 - `conda install bokeh`
 - `pip install bokeh`
 - [bokeh documentation](https://docs.bokeh.org/en/latest/docs/installation.html)
10. **Next 3rd Party Package**  
 - `conda console command`  
 - `pip console command`  
 - [next package documentation](https://insert-link-here)  

 ## ECE143, FA20, Team 19 Contributors   
Harker Russell <hrussell@ucsd.edu>  

Pratyush Dwivedi <pdwivedi@ucsd.edu>  

Jake Kim <jyk005@ucsd.edu>  

Ruihao Wei <r5wei@ucsd.edu>  

 
