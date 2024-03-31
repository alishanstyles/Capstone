# Obesity and Cardiovascular Risk Data Analysis

## Problem Statement 
-This data can be used to identify the level of obesity of an individual and create a system that monitors the level of obesity. This prediction model can help those who are interested in achieving a healthier weight to identify the factors that contribute to weight and obesity. 
-The data looks at individuals in Columbia, Peru, and Mexico and the columns consist of age, gender, height and weight as well the frequency of physical activity, consumption of food between meals, consumption of alcohol, usage of technology devices and more. These are the factors that contribute to weight gain and obesity.

## The Modeling Process
I believe my model will generalize to new data because it performed well to data that it has not seen. I demonstrated feature engineering by selecting features relevant to the obesity levels. I also used visualizations such as a heat map to gain insight on the features with significant correlation to the target and improve the model. The baseline score was 16. I created a classificationn model using Height, Gender, Physical Activity Frequency (FAF), Weight, Time Using Technology Devices(TUE) as features. Using these features the test score for K Nearest Neighbors was 83. The test scores for Logistic Regression was 87 and the test score for Random Forest was 94. 

## Data Dictionary 
| Abbreviation   | Full Form                                 | Types |
|:---------------|-------------------------------------------|--------------
| FAVC           | Frequent consumption of high caloric food | Bool     |
| FCVC           | Frequency of consumption of vegetables    | Float    |
| NCP            | Number of main meals                      | Integer  |
| CAEC           | Consumption of food between meals         | Object   |
| CH20           | Consumption of water daily                | Float    |
| CALC           | Consumption of alcohol                    | Object   |
| SCC            | Calories consumption monitoring           | Bool     |
| FAF            | Physical activity frequency               | Float    |
| TUE            | Time using technology devices             | Float    |
| MTRANS         | Transportation used                       | Bool     |
| Age            | Age of participant                        | Float    |
| Gender         | Gender of Participant                     | Integer  |
| Height         | Height of participant                     |Float     |
| Weight         | Weight of participant                     |Float     |
|family_history_with_overweight | If the participant family history with being over weight |  Object |
|NObeyesdad      | Level of Obesity                          | Object   |
|SMOKE           | Does the participant smoke                | Bool     |


## Executive Summary

### Data Cleaning Steps
I replaced female and male with 1 and 0 as well as true and false with 1 and 0. I created another column called Weight Category with all of the obesity levels and turned them from categorical to numerical making the obesity levels able to go into a heat make. I also created dummy columns for transportation used, consumption of alcohol, calories consumption monitoring, smoke, consumption of food between meals, frequent consumption of high caloric food, family history with overweight and gender. 

### Key Visualizations
Include key visualizations that highlight important aspects of the data. Use graphs, charts, or any other visual representation to make your points.

#### Visualization 1:['Distribution of Obesity Levels by Gender']
[Obesity Type II and Obesity Type I is most common in men. While Obesity Type III and insufficient weight is most common in women.]

[Obesity and Cardiovascular Risk Data Analysis](counttplot.png)

#### Visualization 2:['Weight Based on Age']
[Obesity Type III is more common in ages 20-30 and ranges from 100 - 160 kilograms. Obesity Type II is ranges between ages 20-45.]

[Obesity and Cardiovascular Risk Data Analysis](scatterplot.png)

## Conclusions/Recommendations

I would recomend more physical activities such as walking. For instance walking instead of driving or taking public transportation (when able) to get in some physical activity to help combat weight gain and obesity. Based on the data those who walk more and are more physically active have a lower weight and thus is less likely to be obese. I would also recommond not eating or not eating as much between meals. Those who consume less high caloric foods have a lower weight than those who consume more high caloric foods. Based on this would recommend consuming less high caloric foods to estabish a health weight. 

## Additional Information
For further analysis I think having a column for location  would be nice. Even though we know the data is from individuals in Mexico, Peru, and Columbia it would be helpful to see the obesity levels and eating habits in each location. I believe it would also be good to have information on any physical or medical limitations so we can see what the average weight and obesity level is for each limitation as well as knowing the average calories consumed in a day.  
