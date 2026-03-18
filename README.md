# Procrastination Analysis – Multi-Source Data Study (Power BI)

This project analyzes procrastination-related content using multiple data sources
(Udemy courses, YouTube videos, and academic survey results) in order to understand
which type of content attracts more attention, engagement, and user reaction.

The goal of the project is not only visualization, but also to simulate a realistic
decision-support scenario where data can be used to design better educational
or productivity-related content.

The data preparation process was done in Python and Kaggle, and the final analysis
was built in Power BI.

Kaggle notebook used for data preparation:
https://www.kaggle.com/code/lrhmanelliverdiyev/ai-prompting-for-procrastination/edit



## DATA SOURCES

This project combines three different data sources.

1. Udemy course data
   Course information was collected and filtered in order to analyze how users react
   to different course categories, prices, durations, and popularity indicators.

2. YouTube video statistics
   Data was collected using the YouTube API.
   The script searches for videos related to the keyword "Procrastination"
   and retrieves statistics such as:

* views
* likes
* comments
* channel name
* publish date
* video URL

The collected data was exported to CSV and used in Power BI.

3. Academic procrastination survey

Dataset name:
Results of the Procrastination survey with bar charts

Source:
Loughborough University dataset repository

Link:
https://repository.lboro.ac.uk/articles/dataset/Results_of_the_Procrastination_survey_with_bar_charts/26871163?file=48883480

This dataset contains survey results related to procrastination behavior,
including demographic information, psychological factors,
and study habits.

The original dataset contains many questions,
but only the most relevant variables were selected
for the final tree analysis.



## DATA PREPARATION

Data preparation was done in Python and Kaggle.

Steps included:

* cleaning CSV files
* formatting numeric values
* collecting API data
* filtering relevant columns
* exporting structured datasets for Power BI

The full preparation workflow can be seen in the Kaggle notebook.



## DASHBOARD OVERVIEW

The Power BI report contains three main pages.

Each page represents a different analytical perspective.


## PAGE 1 — UDEMY COURSE ANALYSIS

This page analyzes Udemy courses related to productivity, focus, and procrastination.

Udemy allows users to search courses by category,
so the analysis starts from the assumption that category choice
strongly influences user behavior.

The card in the top left shows the total number of subscribers
for each category, which helps to understand
which topics attract the most attention.

The chart below compares:

* course price
* number of reviews
* course length

This allows us to see whether longer courses, cheaper courses,
or more expensive courses receive more engagement.

When a course title is selected:

* detailed information appears in the cards above
* course URL is shown
* instructor information is shown
* headline is shown
* subscriber count is updated

This simulates a realistic scenario where we want to know
how a user reacts after selecting a course.



## PAGE 2 — YOUTUBE VIDEO ANALYSIS

This page analyzes the top 50 YouTube videos related to procrastination.

Because YouTube content is free,
price cannot be used as a metric.

Instead, engagement was measured using:

* views
* likes
* comments

Comments were used as an indicator of active user reaction.

A pie chart shows how many comments each channel receives
from procrastination-related videos.

This helps identify which creators generate the most discussion.

A bar chart shows all videos sorted by views and likes.

When a video is selected:

* URL is displayed
* description is displayed
* video information is shown

This allows quick comparison between different types of content.



## PAGE 3 — SURVEY TREE ANALYSIS

The third page analyzes academic survey results from
the Loughborough University procrastination study.

The original dataset contains around 20 questions,
but only the most relevant ones were selected.

A decomposition tree was created to explore relationships between:

* gender
* age
* mental state
* frequency of procrastination
* study habits
* time management problems

This visualization makes it possible to follow
how different answers lead to different behavioral patterns.

The tree structure helps to understand
which factors are most connected to procrastination.



## CONCLUSION

This project demonstrates how data from different sources
can be combined into a single analytical model.

The goal is to simulate a real decision-support scenario
where data helps to understand user behavior
and design better educational or productivity content.

Tools used:

* Python
* Kaggle
* YouTube API
* CSV / Excel
* Power BI
