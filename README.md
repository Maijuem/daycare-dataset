# daycare-dataset
##Background
This project analyzes the Nursery dataset—an open research dataset, not real confidential childcare records. The idea stemmed from practical experience working as a daycare assistant, which led to reflections on how People Analytics, a topic I have researched and read extensively about, could apply in early childhood settings. While real personnel data is usually confidential, the Nursery dataset offers a safe way to apply machine learning tools to questions relevant for daycare and education settings.

The dataset originates from a decision model designed in Ljubljana, Slovenia in the 1980s, used for ranking nursery school applications. It contains only synthetic data and does not include personal or sensitive information; its purpose is to support research into transparent, equitable admissions processes and educational support.

###Methodology
Exploratory Analysis: Used Python to inspect missing values, clean the data, and visualize basic distributions. The dataset is complete and did not require much cleaning.

Segmentation and Clustering: Applied k-means clustering and visualization to better understand demographic and family attributes reflected in the data.

Modeling: Built logistic regression and decision tree models. These demonstrate how classification could assist admission decisions or prioritize support for children, even though such automated systems are not used in Finland, where access is universal.

##Findings
Due to its synthetic, balanced generation, the dataset does not reveal meaningful, real clusters.

Segments are distributed evenly, as designed.

Decision tree modeling produces the most usable approach for future classification.

## Limitations
The data is entirely synthetic (12,960 records, eight categorical variables).

All conclusions are for demonstration and learning, not operational decision-making.

The analysis is intended to illustrate how data science methods could examine needs and urgency for groups—not to discriminate, but to enhance understanding and equitable support.

## Notes
This work is a demonstration of applying modern data science and People Analytics to an educational dataset. All code and models are educational and for reference only. For real applications, ethical and privacy requirements must be prioritized.
