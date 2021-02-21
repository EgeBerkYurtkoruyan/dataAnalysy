# -*- coding: utf-8 -*-
"""Yurtkoruyan_Ege_hw3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H5IdkzwhjWKeZZezmRjJBfWXnvnGiBRe

# Homework 3: Exploratory Data Analysis

*In this homework, you are going to perform exploratory data analysis (EDA) on a dataset compiled by a research group from Harvard University.*

**Submission Instructions**

---
It is important that you follow the submission instructions. 
1. Copy this assignment notebook to your Drive. <font color = 'red'> `File` --> `Save a copy in Drive`</font>. Rename it as <font color = 'green'>`Lastname_Firstname_hw3`</font>.

2. Write your solutions in the cells  marked <font color = 'green'>`# your code`</font>.

3. **Do not delete your outputs. They are essential for the grading. Make sure that cells containing your solutions are executed, and the results are displayed on the notebook.**

4. When you're done please submit your solutions as an <font color="red">`.ipynb`</font> file. To do so:

  - Click on <font color="red">`File`</font>  at the top left on the Colab screen, then click on <font color = 'red'>`Download .ipynb`</font>.
  - Then submit the downloaded <font color="red">`.ipynb`</font> version of your work on SUCourse.


For any question, you may send an email to your TAs and LAs.

---

## Income Segregation by Education Level

In 2017, Chetty et al. compiled an anonymous data from USA Federal Government, in which they recorded the earnings of students born between 1980 and 1990 in their thirties. In addition, they recorded the earnings of their parents as well. In their study, they analyze the future financial status of students coming from different parental income levels and display how colleges help students progress.

More information and the paper itself can be obtained from here: https://opportunityinsights.org/paper/undermatching/

In this homework, you are going to analyze the dataset compiled in this study, `mrc_table3.csv`. In addition to the dataset, we also shared a PDF document, named `Codebook-MRC-Table-3.pdf`, prepared by the research team as the data dictionary that displays the columns and their explanations.

The dataset is indexed by `cohorts`. In this context, a cohort is a group of students of the same age and college. In the image below a snippet from the dataset can be observed. Although `cohort` is a column name for the students' age; the actual cohort can be conceptualized as of age + college. For instance, the first row in the image below captures the attributes of the students born in 1980 and attended Brown University.

![](https://i.ibb.co/cbvSpL5/gg.png)

As stated above, the dataset stores the estimated financial status of the students in their 30s and their parents. In addition to storing mean income values to represent financial status, such as `par_mean` and `k_mean`, the researchers also provide a set of attributes to capture the relative information. To this end, they utilize *quintiles* and *percentiles* to represent fractions of the cohort.

Below, you may find some of the column patterns that utilize quintiles and percentiles, along with their explanations.

- **par_q[PARQUINT]**: Fraction of parents in income quintile [PARQUINT]. 1 is the bottom quintile and 5 is the top.
  - Remember that each row stores the financial status of that cohort's students and their families financial attributes. The value in this attribute captures the fraction of parents that reside in the [PARQUINT] quintile. 
  - Since, with quintiles we basically divide the data into 5 different regions, [PARQUINT] can take values between 1 and 5. 
    - 1 -> bottom quintile, in other words, lowest income level
    - 5 -> top quintile, or the highest income level
  - *So, there are five columns that store the fraction of parents in that quintile, e.g. `par_q5` stores the percentage of the parents that are in the top quintile.*

- **k_top[PCTILE]pc**: Fraction of students in the top [PCTILE] percentile. For instance, `top1pc` refers to children in the top 1% of the income
distribution. 
  - The columns that contains the [PCTILE] tag captures the fractions with respect to `percentiles`.
  - As stated in the these attributes store the percentage of students that reside in the top [PCTILE]% of the income.
    - *e.g. If `k_top1pc` is set to 0.56, then we can conclude that 56% of the students in that cohort are in the top 1% of the income distribution in their 30s.*

And lastly, the researchers provide conditional probabilities as a financial projection for the students.

- **ktop1pc_cond_parq[PARQUINT]**: Probability of student in top 1%, conditional on parent in quintile [PARQUINT].
  - *e.g. ktop1pc_cond_parq1 stores the probability of a student being in the top 1% income level given that his/her parents were in the bottom quintile.*

- **kq[KIDQUINT]_cond_parq[PARQUINT]**: Probability of kid in quintile [KIDQUINT], conditional on parent in quintile [PARQUINT].
  - *e.g. kq5_cond_parq1 stores the probability of a student being in the top income quintile given that his/her parents were in the bottom quintile.*

*p.s. In this notebook, the terms `students`, `child` and `children` are used interchangeably. Each usage refers to a cohort.*
"""

from google.colab import drive
drive.mount("./drive")

path_prefix = "./drive/My Drive"

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os.path import join

# %matplotlib inline

fname = "mrc_table3.csv"
df = pd.read_csv(join(path_prefix, fname))
df.head(2)

from google.colab import drive
drive.mount('/content/drive')

"""## Get to Know the Dataset

In this section, you are going to display the distribution of some attributes to better understand the data you are dealing with.

### Q1: NaN Values

In this notebook, we are not interested in all of the attributes. From the non-financial attributes, we are only interested in the `cohort`, `name`, `tier_name` and `type` columns. You need to make sure that there is no NaN value in these columns. And for the financial attributes we're interested in the all of the columns begining with `par_mean` (index 17 in the columns) till the end.

1. Check and print the NaN distributions in `cohort`, `name`, `tier_name` and `type` columns. If there are any NaN values in those columns, remove the corresponding rows.
2. Directly remove the rows where at least one NaN value exists in the financial attributes. *Notice that the columns starting from index 17 till the end are all financial attributes.*
"""

# your code
print("Numer of missing values in cohort column:\t", df["cohort"].isna().sum())
print("Numer of missing values in name column: \t", df["name"].isna().sum())
print("Numer of missing values in tier_name column:\t", df["tier_name"].isna().sum())
print("Numer of missing values in type column: \t", df["type"].isna().sum())

df = df.dropna(axis="index", how="any", subset=["cohort", "name" , "tier_name", "type"])
c = df.columns[17:]
df = df.dropna(axis="index", how="any", subset=c)

x="1.0"
x.isalnum()

"""### Q2: College Tier Distribution

In the dataset, colleges are categorized into types and tiers at differing granularities. In the `type` column, the colleges are categorized as `public`, `private non-profit` and `for-profit`.

Find the number of colleges in each type and display their percentages as a bar chart. 

The result should look like the figure below.

![](https://i.ibb.co/2gSJCQ6/q1-1.png)
"""

# your code
p = len(df[df["type"] == 1])
pnp = len(df[df["type"] == 2])
fp = len(df[df["type"] == 3])
percent = 100/(p+pnp+fp) 

y = ["for-profit","private non-profit" ,  "public"]
xlocs = [fp*percent , pnp*percent, p*percent]
plt.barh(y,xlocs)

xlocs = np.linspace(0, 50, 5)
ticks_labels = [f"{xloc:.0f}%" for xloc in xlocs]
plt.xticks(xlocs, ticks_labels)

plt.title("Collage Distribution by Type")
plt.xlabel("Share")
plt.ylabel("type")
plt.grid(b = True, color = "white", linestyle = "-", linewidth = 0.3)
plt.show()

"""### Q3: Student & Parent Income Distribution

Columns `par_mean` and `k_mean` store the mean income for the parents and students in a cohort. In order to understand the overall distribution, display the `par_mean` and `k_mean` attributes as boxplots on the same figure.

However, the mean distributions are highly skewed. So, in order to better evaluate the distributions, we can remove the outliers. 

- Create a 2x1 grid layout. Display the boxplots of the original distributions on the left. 

- Remove the outliers from both of the distributions by utilizing 1.5xIQR rule.

- Generate the boxplots for the resulting distributions on the right axes. 

The result should look like the figure below.

![](https://i.ibb.co/YkSzc9d/q2.png)
"""

# your code
fig,axes = plt.subplots(1,2,figsize = (15,5))

title = "Mean Income Distribution per Parent and Students"
x_vals = ["Parent Mean Income" , "Student Mean Income"]

df.boxplot(column = ["par_mean", "k_mean"], labels = x_vals, ax=axes[0])
line=np.linspace(0,df[["par_mean","k_mean"]].values.max(),10)
axes[0].set_yticks(line)
axes[0].set_yticklabels([f"${i/1000:.0f}K" for i in line])
axes[0].set_title(title)
axes[0].set_ylabel("Income in ($) Thousands")
axes[0].set_xticklabels(x_vals)

q1, q3 = np.percentile(df.par_mean, [25,75])
iqr = q3 - q1
up = q3 + 1.5*iqr
down = q1 - 1.5*iqr

Income = df[df["par_mean"] > down]
Income = Income[Income["par_mean"] < up]

q1, q3 = np.percentile(df.k_mean, [25,75])
iqr = q3 - q1
up = q3 + 1.5*iqr
down = q1 - 1.5*iqr

Income = Income[Income["k_mean"] < up]
Income = Income[Income["k_mean"] > down]

Income.boxplot(column = ["par_mean", "k_mean"], labels = x_vals, ax=axes[1])

line=np.linspace(0,Income[["par_mean","k_mean"]].values.max(),10)
axes[1].set_yticks(line)
axes[1].set_yticklabels([f"${i/1000:.0f}K" for i in line])
axes[1].set_title(title)
axes[1].set_ylabel("Income in ($) Thousands")
axes[1].set_xticklabels(x_vals)
axes[1].set_title(title)

plt.show()

"""## Bivariate Analysis

In this section,  you are going to perform bivariate analysis on different attribute pairs.

### Q1: Parent Income Distribution by College Tier

The income distribution is highly skewed as it can be observed in the previous question. With the generated charts, we see how the overall distribution is shaped with the help of boxplots. However, we can not observe how this distribution changes with respect to college tiers.

As you can see from the shared data dictionary, there are 14 different college types. Instead of putting all of the tiers into account, in this question, you are going to focus on 6 of them: `Ivy Plus, Other elite schools (public and private), Highly selective public, Highly selective private, Selective public, Selective private`. Display the `par_mean` distribution for each of the selected tiers.

- Group the dataframe with respect to the selected tier types.
- For each group, display the `par_mean` attribute on the same figure as a boxplot.
- Sort the boxplots with respect to their medians.

The result should look like the figure below.

![](https://iili.io/FMJMn1.png)
"""

# your code
ip = df[df["tier"] == 1]
ip_ = ip["par_mean"]
oes = df[df["tier"] == 2]
oes_ = oes["par_mean"]
hspu = df[df["tier"] == 3]
hspu_ = hspu["par_mean"]
hspr = df[df["tier"] == 4]
hspr_ = hspr["par_mean"]
spu = df[df["tier"] == 5]
spu_ = spu["par_mean"]
spr = df[df["tier"] == 6]
spr_ = spr["par_mean"]
y__ =[spu_,spr_,hspu_,hspr_,oes_,ip_]

fig, ax = plt.subplots(figsize=(19,6))
x_names = [ "Selective public", "Selective private", "Highly selective public", "Highly selective private", "Other elite schools (public and private)","Ivy Plus"]
ax.boxplot(y__, labels=x_names)

ylocs = np.linspace(0, df["par_mean"].max(), 10)
ticks_labels = [f"${yloc/1000:.0f}K" for yloc in ylocs]
ax.set_yticks(ylocs)
ax.set_yticklabels(ticks_labels)

plt.grid(b = True, color = "grey", linestyle = "-", linewidth = 0.3)
plt.title("Parent Income Distribution by Collage Tier")
plt.show()

"""### Q2: Mean Child Rank vs. Age at Income Measurement by College Tier

In this question, you are going to display how the mean student income rank changes as the age of income measurement changes for the selected college tiers. In the dataset, we have students born between 1980 and 1991. In **2014**, their income level is measured. In the dataset, the `k_rank` column stores the student income rank.

- First, find the age of each cohort by subtracting the birth years from the year of measurement and store them in a new column named `measurement_age`.

- Group the dataframe by `tier_name` and `age`, and find the mean student income rank for each group.

- For the listed tier names below, display the change of mean student income rank with respect to the age of measurement as a line chart.

`Ivy Plus, Other elite schools (public and private), Highly selective public, Highly selective private, Selective public, Selective private`

The result should look like the figure below.

![](https://i.ibb.co/FJFZHX6/dd-3.png)

*Hint: You may use the unstack function alongise transposition.*

*Please visit the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html) for the details on unstack, and [this link](https://cmdlinetips.com/2020/05/fun-with-pandas-groupby-aggregate-multi-index-and-unstack/) for the use cases.*


"""

# your code
dfd = df
dfd['age'] = 2014 - dfd['cohort']
dfd = df[["par_mean", "tier_name","k_rank","age"]]
dfd = dfd.loc[df["tier_name"].isin(x_names)]
dfd = dfd.rename(columns={"tier_name":"Tier"})
dfd = dfd.groupby(["age","Tier"])['k_rank'].mean().unstack()
dfd.plot(figsize= (17,7), grid=True, style = 'D-')
plt.xlabel("Age of Income Measurement", size=10)
plt.ylabel("Mean Student Income Rank", size=10)
plt.title("Mean Child Rank vs. Age at Income Measurement By Collage Tier", size = 15)
plt.show()

"""## Mobility Rate

The researchers analyzed the role of colleges for students to progress their income level, especially the students coming from lower quintiles that end up in higher quintiles in their adulthoods. To this end, they derive a new metric named `mobility rate`. 

> "The fraction of students who come from bottom quintile and end up in top quintile"

![](https://i.ibb.co/rpTgXq0/pl.png)

In the dataset `kq5_cond_parq1` column stores the success rate of each cohort; while `par_q1` column stores the access rates.

In addition to defining the success rate as P(Child in Q5 | Parent in Q1), the researchers also developed the same rate with respect to student income percentiles: P(Child in **P1** | Parent in Q1) stands for the students who come from bottom quintile and end up in top 1% percentile.  And `ktop1pc_cond_parq1` column stores those values for each cohort.

### Q1: Calculating the Mobility Rate

In this question, you are going to calculate the mobility rate for each college and then find the top 10 colleges with the highest mobility rates.

- For each cohort, in other words each row, calculate the mobility rate with both `kq5_cond_parq1` and `ktop1pc_cond_parq1` and store them in columns named `mobility_rate_q5` and `mobility_rate_p1`, respectively.
  - `kq5_cond_parq1` * `par_q1` -> `mobility_rate_q5`
  - `ktop1pc_cond_parq1` * `par_q1` -> `mobility_rate_p1`

- Group the dataframe with respect to the colleges and find the mean of `mobility_rate_q5, mobility_rate_p1, kq5_cond_parq1, par_q1` columns. 

- First, sort the resulting groups, i.e. colleges, with respect to `mobility_rate_q5` and display the top 10 rows as a dataframe.

- And lastly, sort the resulting groups with respect to `mobility_rate_p1` and display the top 10 rows as a dataframe.
"""

# your code
df["mobility_rate_q5"] = df["kq5_cond_parq1"] * df["par_q1"]
df["mobility_rate_p1"] = df["ktop1pc_cond_parq1"] * df["par_q1"]

#I grouped by the values
dfg = df.groupby(by="name").mean()
dfmq5 = dfg[['mobility_rate_q5']]
dfmp1 = dfg[['mobility_rate_p1']]

#I sorted the two datasets accordingly
dfs = dfmq5.sort_values('mobility_rate_q5', ascending=False)
dfss = dfmp1.sort_values('mobility_rate_p1', ascending=False)

#I displayed the values
display(dfs.head(10))
display(dfss.head(10))

"""### Q2: Success vs. Access Rates by College Tier

And finally, you are going to check how success and access rates change for different college tiers. In this question, you are going to focus on two college tiers: `Ivy Plus` and `Two-year for-profit`. In addition, you are going to display this relationship using only the success rate definition 2: P(Child in P1 | Parent in Q1).

- Group the dataframe by college and find the mean of success and access rates for each college.
  - Success rate: 
    - Definition 2: P(Child in P1 | Par in Q1) -> ktop1pc_cond_parq1
  - Access rate: P(Par in Q1) -> par_q1

- Display a scatter plot in which access rates are encoded in x-axis and success rates in y-axis.

- At the end, each dot on the figure would represent a college. Highlight `Ivy Plus` and `Two-year for-profit` with distinct color for separability.

The result should look like the figure below.

![](https://iili.io/FMJ6cG.png)
"""

# your code
dfl = df
dfl = dfl[["tier_name","ktop1pc_cond_parq1", "par_q1","name"]]
dfl = dfl.loc[dfl["tier_name"].isin(['Ivy Plus','Two-year for-profit'])]
dfq = dfl.groupby(["par_q1","tier_name"])["ktop1pc_cond_parq1"].mean().unstack()

dfq.plot(figsize= (17,7), grid=True, style = 'o')

plt.grid()
plt.grid()
plt.ylabel("Success Rate", size=10)
plt.xlabel("Access Rate: Percent of Parents in Bottom Quintile", size=10)
plt.title("Access vs. Succes Rate by Collage Tier", size = 15)
plt.show()