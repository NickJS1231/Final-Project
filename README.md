# Portfolio Utility: A Comparative Analysis <br> <br>
### The Research <br> <br>
This project aims to assess the utility of a given portfolio theme (i.e., sustainability, low beta, Technology, etc.) when compared to a larger sample benchmark (the S&P 500). At large scale (the big question), research in this area aims to validate the marginal utility of increased diversification by showing compromises in utility in a given subset of the larger sample. More directly, this research aims to show which themes of portfolios have which effects relative to the larger sample. Essentially, how much utility do you sacrifice by restricting your portfolio to a given theme of securities? <br><br>
**What it will look like** <br><br>
To visualize this, the project will create a dashboard that graphs the efficient frontier of a large sample (the S&P 500). Additionally, upon selection, the dashboard will then graph the efficient frontier of the subsample of the data based on a given portfolio theme. The themes will include:
 - Stability <br>
 - Technology <br>
 - Low Beta <br>
 - ESG Firms <br>
 - Firms headquartered in Pennsylvania <br>
 - Most expensive equities <br>
 - Cheapest equities <br>
 - Firms that create or deliver pizza i.e. Domino’s, Grubhub <br>
 - Tickers that contain the letters “L”, “E”, “H”, “I”, or “G” <br>
 - Etc. <br>
**The Analysis will then assess the following:** <br><br>
 - Which firms are included in the subset vs the benchmark? <br>
 - What is the marginal utility of the subset (assessed through the utility equation) <br>
 - Given different risk aversion levels (different points on the capital allocation line), how much more or less efficient does the subset become? <br>
 - Another ***potential*** area of interest for this dashboard could be providing explanatory insight into the above metrics over the course of time.  For example, how has the sustainability portfolio performed over the past five years as opposed to the prior five before that? How does the efficient set’s comparison to the benchmark change over time? Does time show trends of certain portfolio groups improving in utility? <br><br>
### The Data<br><br>
 - The final dataset used to perform an analysis will contain each firm and its return/variance over a given period of time. <br>
 - Dependent on adopting the time aspect of this model, the unit of observation will either be firm, or firm-time-period (i.e., 3yr CAGR foro 15 years of data). <br>
 - Sample period will depend on the adoption mentioned above, but at minimum will be a 1yr time from for which to compound returns over <br>
 - Sample restrictions will be made based on the listed portfolio themes, research into the categories will determine specific selections of firms. <br>
 - Data on returns, ticker, potential categorization values (i.e., ESG scores, beta etc.) are required and will likely need to be merged from multiple datasets.<br>
 - Raw data for all of the above is available, calculation of returns and variance will be required. This data will not be collected, rather computed off of raw data. <br>
 - Inputs will be return data and necessary thematic descriptors. Data will be stored as follows: <br><br>
### File Structure <br><br>
 - Inputs and Cleaning: think of this as a combination of the get text and build sample files from the midterm, being that data acquisition will be simpler, it can be incorporated into the build sample file. This will also include the computation of returns and assignment of firms to applicable subsets. A final dataframe of firms, portfolio categorizations (a binary variable that states if its in a given portfolio), returns and variances will be generated and sent into outputs <br><br>
 - Outputs: This file will include all code necessary to run the dashboard and will also incorporate the dynamic graphing of the efficient frontiers, calculation of utility scores, and all needed user input interface aspects. <br>
   - See pseudo code below for data transformation and output creation    

Pseudo-Code Procedure

1. Import dataset.
2. Depends on methodology i.e.
OpenBloomberg?
yfinance
Predetermined dataframe?
Selectable dataframe?
Calculate Return and variance of each security over a specified time horizon
Define levels of risk aversion (create arbitrarily calculated, selectable levels of “riskiness rather than using an assessment)
Research best ways to do this
With risk aversion and user-selected goals, able to calculate capital allocation 
Set aside percentage of capital for risk free assets
With equity section, continue to next step
Trim dataset depending on user-selected goals
Growth
Stability
Technology
Low Beta
ESG Firms
Firms headquartered in Pennsylvania
Most expensive equities
Cheapest equities
Firms that create or deliver pizza i.e. Domino’s, Grubhub
Tickers that contain the letters “L”, “E”, “H”, “I”, or “G”
Etc.
Calculate efficient frontier curves for entire dataset as well as the user-selected goal-oriented dataset-trim
Calculate distances between firms in the trimmed-dataset and the benchmark frontier curve
Add highest ranked (closest) firms to frontier curve to optimal equity list based on a user-selected number of securities to include
Utility calculations
Using utility theory function to calculate the given utility score of a portfolio
Compare utility score across portfolio to determine sacrifices/gains of a given portfolio.





