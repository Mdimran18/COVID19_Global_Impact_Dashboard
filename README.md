# COVID-19 Global Impact Dashboard

## Project Overview
This project analyzes and visualizes the global impact of COVID-19 using comprehensive datasets from [Our World in Data](https://ourworldindata.org/coronavirus). The dashboard highlights key health, vaccination, and economic trends across countries and over time, providing insights to better understand the pandemic’s progression and its effects worldwide.

## Objectives
- Explore COVID-19 case trends, deaths, and vaccination progress by country.
- Visualize global patterns using clear and interactive charts.
- Provide data-driven insights to inform public health responses and policy decisions.
- Make data accessible through an intuitive Power BI dashboard and Python exploratory analysis.

## Data Source
- Dataset used: `owid-covid-data.csv` from [Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data).

## Project Components

### 1. Data Exploration and Cleaning
- Conducted exploratory data analysis using Python Jupyter notebooks (`notebooks/EDA.ipynb`).
- Cleaned and preprocessed data to ensure accuracy and consistency.

### 2. Data Visualizations
- Created multiple interactive visualizations using Power BI to illustrate:
  - Daily and cumulative COVID-19 cases and deaths.
  - Vaccination rates and trends across continents and countries.
  - Economic impact indicators such as GDP changes.
- Visualizations include bar charts, line charts, scatter plots, and maps for geographic analysis.

### 3. Interactivity and User Experience
- Implemented filter options in Power BI dashboard to enable users to explore data by region, date range, and specific metrics.
- Added tooltips and hover effects for detailed data points.
- Ensured clarity through appropriate color schemes, legends, and axis labels.

## How to Use

### Power BI Dashboard
- Open the Power BI Desktop file (`COVID19_Global_Impact_Dashboard.pbix`) located in the repository.
- Use slicers to filter by continent, country, and date range.
- Hover over charts for detailed tooltips.
- Explore trends and correlations through interactive visuals.

### Python Notebook
- Open `notebooks/EDA.ipynb` in Jupyter Notebook or Jupyter Lab.
- Run the cells sequentially to reproduce the exploratory analysis.
- Modify or extend the analysis with additional queries as needed.

## Key Insights

- Significant variance in COVID-19 case and death rates between continents, with some countries facing severe outbreaks.
- Vaccination rollout trends show disparities in coverage, emphasizing the need for equitable distribution.
- Economic indicators reveal correlations between pandemic severity and GDP fluctuations.

## Repository Structure

```
COVID19_Global_Impact_Dashboard/
│
├── data/
│   └── owid-covid-data.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── visuals/
│   └── (screenshots of key charts)
│
├── scripts/
│   └── (optional data preprocessing scripts)
│
├── COVID19_Global_Impact_Dashboard.pbix
├── README.md
```

## How to Contribute
Feel free to open issues or submit pull requests to improve the dashboard or add new insights.

## License
This project is licensed under the MIT License.

---

*Prepared by Md Imran — June 2025*
