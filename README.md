# Portfolio Utility: A Comparative Analysis <br> <br>
### The Research <br> 
Are you an active investor? Have you ever tried to position your portfolio towards a specifc area to "maximize" your portfolio? If you have, this repo will teach you a valueable lesson: diversification rules! <br> <br>
This project aims to assess the utility of a given portfolio theme (i.e., sustainability, low beta, sector specific investing, etc.) when compared to a larger population benchmark (the S&P 500 in this case). At large scale (the big question), research in this repo aims to validate the marginal utility of increased diversification, by showing compromises in utility in a given subset of the larger population. Essentially, how much utility do you sacrifice by restricting your portfolio to a given theme of securities? <br> <br>
The dashboard in this project is based off of a previous dashboard in professor Don Bowen's "Data Science for Finance" Course, found here:(https://github.com/donbowen/portfolio-frontier-streamlit-dashboard). Our project builds on this dashboard by providing insight into the effect of portfolio themes. It deviates from the previous project by eliminating the option for leveraged portfolios and providing a risk quiz; it rather shows the difference in utility between a population of securities and a subset at a arbitrarily selected level of risk aversion. <br> <br>
***Official Research Question:*** How many utils are sacrificed/gained based by investing in a specifically themed portfolio? <br><br>
**What this looks like** <br>
To visualize this, the project will create a dashboard that graphs the efficient frontier of a popualation of securities (the S&P 500). Additionally, upon selection, the dashboard will then graph the efficient frontier of the subsample of the data based on a given portfolio theme. The themes will include:
 - ESG <br>
 - Low Beta Securities
 - High Beta Securities
 - Ticker contains letters in LEHIGH
 - Cheapest Securities (price per share)
 - Sector (can be one or a combination)<br>
   - Industries
   - Healthcare
   - Technology
   - Utilities
   - Financial Services
   - Basic Materials
   - Consumer Cyclical
   - Real Estate
   - Communication Services
   - Consumer Defensive
   - Energy
 <br> <br>

**The Analysis will then assess the following:** <br>
 - What is the utility of the subset? What is the utility of the population? What is the difference between the two? <br>
 - Given different risk aversion levels (different points on the capital allocation line), how much more or less efficient does the subset become (based on utils)? <br> <br>
The utility of a portfolio is calculated using the following formula:

U = Expected Return - (1/2) * A * σ^2
<br> <br>

Where:
- \( U \) is the utility of the portfolio.
- Expected Return is the expected return of the portfolio.
- \( A \) is the risk aversion level.
- \( \sigma \) is the volatility (standard deviation) of returns.


### The Structure of this Repo<br>
The creation process for this repo follows this process: <br>
1. **`getting_ESG_scores`** This will generate a csv of firms and ESG scores for the desired population called "esg_scores".
1. **`Get_Data-Copy`** - This is the file where all the data fun happens. When you run this file you will <br>
  a. Download the required data for the S&P 500 including variables required for themeatic subsetting (industry, beta, adj price, etc.) (2019-2023) <br>
  b. Do some manual data manipulation to make working this data easier <br>
  c. Appends ESG scores to the primary dataframe <br>
  d. Gets the risk free rate needed for the analysis <br>
  e. Calculates expected return for each firm <br>
  f. Generates a variance covariance matrix <br>
  g. Generates a subset of the primary dataframe with one observation per firm <br>
  h. Outputs the needed data to "covariance_matrix_returns", "data_scores", "expected_returns", "sp500_data_with_scores", and "sp500_tickers"
1. **`app.py`** - This is the python file that runs the streamlit dashboard you see. This file uses the following functions
 - **`theme_selector()`:** This function allows users to select thematic themes    or sectors from a dropdown menu in the sidebar. It returns the selected option     and any sectors chosen by the user.

 - **`get_ef_points(ef, ef_param, ef_param_range)`:** This helper function         calculates the points on the efficient frontier based on an EfficientFrontier      object (`ef`) and a specified parameter (`ef_param`) over a range of values        (`ef_param_range`). It returns the expected returns and volatilities of the        portfolios.

 - **`get_plotting_structures(asset_list=None)`:** This function retrieves the     necessary data, such as expected returns, volatility, and risk-free rate, to       construct the efficient frontier. It also initializes the EfficientFrontier        object and computes the tangency portfolio. It returns these data structures for   plotting.

 - **`get_theme_assets(option, selected_sectors)`:** This function retrieves a     list of assets based on the selected theme or sectors. It filters stocks based on  the chosen option and returns a subset of asset tickers.

These functions are essential for collecting data, selecting thematic themes or sectors, calculating efficient frontier points, and retrieving assets based on user input. They facilitate the functionality of the dashboard by handling data processing and visualization tasks.

### Running This Yourself
As per the prior projects instruction, here is how you can use this repo yourself
1. A working python / Anaconda installation
1. Git 

Then, open a terminal and run these commands one at a time:

```sh
# download files (you can do this via github desktop too)
cd <path to your FIN377 folder> # make sure the cd isn't a repo or inside a repo!
git clone https://github.com/donbowen/portfolio-frontier-streamlit-dashboard.git

# move the terminal to the new folder (adjust next line if necessary)
cd portfolio-frontier-streamlit-dashboard  

# this deletes the .git subfolder, so you can make this your own repo
# MAKE SURE THE cd IS THE portfolio-frontier-streamlit-dashboard FOLDER FIRST!
rm -r -fo .git 

# set up the packages you need for this app to work 
# (YOU CAN SKIP THESE if you have already streamlit-env, or you can 
# give this one a slightly diff name by modifying the environment.yml file)
conda env create -f streamlit_env.yml
conda activate streamlit-env

# start the app in a browser window
streamlit run app.py

# open any IDE you want to modify app - spyder > jupyterlab for this
spyder  # and when you save the file, the app website will update
```

### To deploy the site on the web, 
1. Use Github Desktop to make this a repo your own account. 
1. Go to streamlit's website, sign up, and deploy it by giving it the URL to your repo.
1. Wait a short time... and voila!






