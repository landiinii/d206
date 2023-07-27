# D206 Report
 Landen Bailey -- WGU -- MSDA
# Part I: Research Question

## A. Question or Decision
  What effect do the different demographics of a customer have on their likelihood to churn?

## B. Describe the Variables 
Describe all variables in the data set (regardless of the research question) and indicate the data type for each variable. Use examples from the data set to support your claims.

### Identifiers
* ID / CaseOrder - 
  * integer
  * ID and CaseOrder are duplicate columns that represent the same **integer** attribute. This integer should be non zero, non null, and represents the order by which the different rows were originally assembled.
* Customer_id - 
  * varchar(7) NOT NULL
  * Customer ID is a unique text value that contains both letters and numbers following a standard format of 1 capital letter character followed by 5-6 integer characters. This value represents the customer as a whole and can be used to connect this data and subsequent analysis to other data/analyses collected by the company on a customer level.
  * Examples: "K409198", "S120509", "D90850", "W303516"
* Interaction - 
  * varchar(36)
  * The interaction ID is a UID/GUID which is a text string of hex values 36 characters in length divided into 5 sections. The first section is an 8 character hex value, followed by 3 sections of 4 character hex values, and ending with a 12 character hex value section. The sections are all divided by a dash (-) character. The valid character values in a hex string are 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f. Letters can be either upper or lower case. 
  * Example: "1937a759-91b7-4390-80f1-6f8e7d81e058" 

### Demographics
* City - 
  * varchar()
  * City name represents the city where the customers live within their state of residence. There are no technical limits on city names so they could hypothetically include non-letter characters including spaces, apostrophes, periods etc. Values should be non null and non empty strings, but otherwise any text value within a realistic length (256 bits being the default for postgresql databases) should be considered valid. Duplicates are permitted and expected. 
  * Example: "Birmingham"
* State - 
  * varchar(2)
  * State represents the US state where the customer lives, and this field identifies that state with the 2 letter standard abbreviation for it. Each entry should only contain 2 alpha characters like the following 
  * Examples: "OR", "CA", "TX"
* County - 
  * varchar()
  * County represent the county of the customers residence, It will have all the same field restrictions as the city field such as is seen here: 
  * Examples: "Cumberland"
* Zip - 
  * string(5)
  * Zip code is a 5 digit code that identifies a standard size region within a city. Although the codes are comprised completely of integer digits, they are stored as a string inorder to best maintain leading 0 values that some may have. 
  * Examples: "60926"
* Lat / Lng - 
  * float(8, 5)
  * Latitude and Longitude are two separate fields that are stored as numeric values of -180 to 180 with 5 digits after the decimal point. 
  * Examples: "40.57234", "-87.80962"
* Population - 
  * integer
  * The population of the customer within a mile radius represented as a positive, non null integer value. 
  * Example: 3582
* Area - 
  * varchar(8) NOT NULL
  * An enumerated string value from the posible values of rural, urban, suburban. Values can not be null, or any other character combination besides those in that list.
  * Examples: "rural", "urban", "suburban"
* Timezone - 
  * varchar() NOT NULL
  * A string value identifying the time zone where the customer lives
  * Example: "America/Chicago"
* Job - 
  * varchar()
  * The occupation title of the customer stored as a string. Can contain any characters and can possibly be null/empty. 
  * Example: "Academic librarian"
* Children - 
  * integer
  * A possibly null non negative integer representing the number of children living in the customers household.
  * Example: 4
* Age - 
  * small integer
  * The age of the customer, Stored as a smallint because no human can realistically live to be a thousand years. realistic range is 18-100, ages below 18 even if not beyond standard deviations should be considered outliers
  * Example: 44
* Education - 
  * varchar()
  * The highest degree of education completed by the customer. 
  * Example: "Master's Degree"
* Employment -
  * varchar()
  * One of a very few values highlighting the employment status of the individual, whether or not they have a job, and how much they work.
  * Examples: "Part Time", "Student"
* Income -
  * float() (2 decimal places)
  * A numeric value representing the amount of money in USD earned by the customer in their profession. 
  * Example: 38100.00
* Marital -
  * varchar()
  * One of a handful of options that defines the martial status of the customer, whether every married, and if currently married.
  * Example: "Widowed"
* Gender -
  * varchar()
  * Represents the self identified gender of the customer with an option to express a preference not to identify their gender.
  * Example: "Male", "Female", "Prefer not to answer"
* Techie -
  * boolean
  * Whether the customer considers themself to be technically savvy. 
  * Example: Yes, No


### Experience Metrics
* Churn
  * boolean
  * Whether the customer has terminated their contract with the company in the last month. 
  * Example: Yes, No
* Outage_sec_perweek
  * float() positive
  * Average number of seconds the network connection is out of service as experienced by the customer per week
  * Example: 6.972566093
* Email
  * integer
  * Non negative value representing the number of emails sent to the customer from any department within the company in the last year
  * Example: 10
* Contacts
  * integer
  * Non negative, not null but possibly 0 value representing the number of times the customer reached out to the company for support within the last year
  * Example: 1
* Yearly_equip_failure
  * integer
  * Non negative, not null but possibly 0 value representing the number of times the customer's equipment failed and had to be replaced within the last year
  * Example: 1


### Contract Metrics
* Contract
  * varchar()
  * The term of contract the customer selected at enrollment
  * Example: "Month-to-Month"
* Port_modem -
  * boolean
  * Whether or not the customer has a port modem
  * Example: Yes, No
* Tablet -
  * boolean
  * Whether or not the customer has a tablet
  * Example: Yes, No
* InternetService - 
  * varchar()
  * Nullable string that identifies the internet plan if any the customer has in their contract
  * Example: "Fiber Optic", "DSL"
* Phone -
  * boolean
  * Whether or not the customer has a phone service with the company
  * Example: Yes, No
* Multiple -
  * boolean
  * Whether or not the customer has multiple phone lines with the company
  * Example: Yes, No
* OnlineSecurity -
  * boolean
  * Whether or not the customer has online security service with the company
  * Example: Yes, No
* OnlineBackup -
  * boolean
  * Whether or not the customer has online backup service with the company
  * Example: Yes, No
* DeviceProtection -
  * boolean
  * Whether or not the customer has device protection with the company
  * Example: Yes, No
* TechSupport -
  * boolean
  * Whether or not the customer has tech support included in their contract with the company
  * Example: Yes, No
* StreamingTV -
  * boolean
  * Whether or not the customer has streaming TV included in their contract with the company
  * Example: Yes, No
* StreamingMovies -
  * boolean
  * Whether or not the customer has Streaming Movies included in their contract with the company
  * Example: Yes, No
* PaperlessBilling -
  * boolean
  * Whether or not the customer has elected for paperless billing
  * Example: Yes, No
* PaymentMethod
  * varchar()
  * The selected method used by the customer to pay the monthly bill
  * Example: "Mailed Check"
* Tenure
  * float()
  * Decimal number representing the number of months the customer has been with the company. Decimal represents fraction of the month or days
  * Example: 13.01149229
* MonthlyCharge
  * float()
  * The monthly charge to the customer in USD that represents an average per customer
  * Example: 118.3668439
* Bandwidth_GB_Year
  * float()
  * average amount of data used per year by the customer
  * Example: 1840.014467

### Survey Responses
* item1 / item2 / item3 / item4 / item5 / item6 / item7 / item8
  * small integer
  * The response by the customer to the specified question. Options values ranges 1-8
  * Example: 2

# Part II: Data-Cleaning Plan

## C.  Explain the plan for cleaning the data by doing the following:

###  Plan 
The plan for assessing and then cleaning the data will be done in 2 steps:
* Step 1 involves checking each of the columns to assure that all the data points within those columns meet the restrictions of their column definition. This is to say that they are all the correct data type and there are not any null values where there shouldn't be Step 1 will be completed for every column regardless of its relevance to the research question because if invalid values are found in any column it is possible that that collection of that entire row of data is inaccurate, so if any rows need to be thrown out they will be removed and the inaccuracies will not perpetuate to the result of the analysis. If and when any invalid values are discovered through these techniques they will be either rejected from further exploration where important or they will be filled in with the average (either mean or mode as sensical) of the column.
* Step 2 will only be done on the columns actually relevant to the research question. In this case those include the demographic columns referenced above, and the churn value. Step 2's analysis of the data will look for major outiers (this could be seen either as an invalid or unrealistic value in enumerated variables or finite systems, or as values unreasonable based on the definition of the variables representation, or in normalized and infinite distributions anything beyond 3 standard deviations). 

###  Justify your approach for assessing the quality of the data, including the following:
* The data in this churn set is defined across a large variety of data types. As such a very column specific approach is necesarry to ensure the individual accuracy of each value with regards to its intended representation. Likewise, many analises of this dataset will depend on accurate values in the scopes of their relation to each other across each row. My 2 step approach will ensure data accuracy across both of these requirements and provide for the highest confidence of accuracy in all forthcoming analyses.

###  Justify your selected programming language and any libraries and packages that will support the data-cleaning process.
I will be using Python to complete this cleaning. There are various relevant packages that could be used to help in this process such as airflow to include diagraming and orchestration of the cleaning process to allow for a broader spectrum of skill levels to be able to perform the same cleaning on future datasets. It is also possible to just rely on native python functionalities and standard libraries (suchs as csv, io, strings, etc) to perform the complete cleaning which allows for greater control over the entire code process and creates more opportunities for optimization and customization of checks. However for a much simpler approach to the data cleaning and to provide much more legible and reuasable code, I will integrate the Pandas library, and operate on the data as a dataframe. This is a best of both worlds approach combining the readability and reuasability of airflow, with the customization and speed of a native solution. 

### Provide the annotated code you will use to assess the quality of the data in an executable script file.


# Part III: Data Cleaning

## D.  Summarize the data-cleaning process by doing the following:

1.  Describe the findings for the data quality issues found from the implementation of the data-cleaning plan from part C:
    * Step one found 4 main issues to account for:
      * Data Types. Specifically strings. Most columns in the data set are numbers, and a simple dtype check revealed that they were properly stored as such. There were a handful of columns that are stored as strings, and those had to be checked directly because while python is okay storing a number as a string, our data quality checks needed to make sure they were not incorrectly assigning columns to the wrong types. There was only 1 issue found here in the zip codes. Despite being digits, Zip codes have to be stored as strings to maintain leading 0s. Python was reading it as a number. So it has to be manually accounted for.
      * String lengths. Many of these strings we just checked have very specific requirements for lengths of the strings. Take zip codes for example again, each of them has to be exactly 5 digits long to be correct. This and various other string based columns were checked and ensured that all values were the proper length. No issues were found here, but they would be removed in the script if any are found running this cleaning on future data sets. 
      * Null values demonstrating improper collection. There are a couple of columns that if they are showing null values, it demonstrates a failure on the systems ability to properly provide accurate data about the customer. One example of this is the Bandwidth_GB_Year column. If our systems are unable to process the amount of data a customer has used, something has gone wrong and this customers data is not accurate. Situations of reporting 0 usage would not be identified as a null value. So null values demostrate something is wrong with this customer's data at a fundamental level. Similarly when the phone number is null or when the tech support column is null. These are crucial columns to the businesses functionality, missing them means the input/collection process for that row failed at some point and for any of these rows the whole rows should be disregarded completely. There were null values found in the following columns falling under this category: "Bandwidth_GB_Year", "Phone", "TechSupport"
      * Null values demonstrating inapplicability to the customer. There were also null values found in the following columns: "Children", "Techie", "Income", "Tenure", "Age", and "InternetService". These columns however have reasonable causes for which the values might be null and properly represent a realistic circumstance. The income for example. A student not working a job does not have any income. Should this have been reported as a 0? Maybe, but it depends on the analysis you want done. Perhaps it is desired that the income only of those with income is considered, and so those without income are marked as null so to not effect the mean of the rest with many 0 values. The income for these with null values in this circumstance will be filled in with the mean of all of the other values, similarly the other columns that are mentioned here will be filled in with either an average or the most reasonable default value so as to not effect the analysis further on and still represent a most realistic aggregation. 
    * Step two checked for three primary situations across the demographics columns:
      * First it checked for numeric values beyond an acceptable standard deviation of 3. There were three columns it did this for, the income, population, and children columns. All of which if there existed customers with values in these columns beyond 3 standard deviations the chances of it being improperly recorded are very high, but also even if the metric is legitamate, it would represent a customer in such a unique circumstance that they could not be reliably predicted for. So all of those rows were removed. 
      * Next it checked for numeric values that have to fall within a certain range to be legitamate and not so absurd as to represent a unique circumstance. Lat and Lng both have to be between -180 and +180 and age has to be between 18 and 100. The script would filter out anything not in those ranges.
      * Lastly it checked for enumerative values from the applicable collumns so that definitially invalid values could be filtered out.

2.  Justify your methods for mitigating the data quality issues in the data set.
    * The methods I used for diminishing bad data from getting into my analysis set are very standard across the industry. Many methods were applied on a columns by column basis and the justification for using one method over the other for a particular column I described already above. But generally speaking rows were removed if the improper or extreme data points were found in a column, the unreliability of which column represented untrustworthy data across the entire row. And values were filled in with some kind of average or default if the invalidation of that column did not represent untrtustowrthy data elsewhere in the row.

3.  Summarize the outcome from the implementation of each data-cleaning step.
      * First thing we checked for was that columns of string data type all properly expressed text objects and not numerical values where it would be otherwise inappropriate. No rows or columns had issue with this requirement so nothing was removed here.
      * Next we checked that string object columns with definitional value length restrictions all met those restrictions. It was here that the mis-stored zipcodes came to light as many zipcodes reported shorter lengths than expected. Correcting the datatype on the zip codes solved this issue and in the end no rows were removed for incorrect lengths of restricted string types. 
      * Next step was to drop rows with null values in columns that made the entire row unusable. This was our biggest culler of rows, taking us from 10,000 rows to now 7280 valid rows. 
      * The step after that was to fill in the other columns with null values with the most appropriate average or default value. This did not reduce the size of our data table, but it did update thousands of rows. 
      * Step 5 now was only focused on the demographic columns, specifically the columns with infinite spectrum numeric values, and it removed rows with values in any of these columns more than 3 standard deviations above or below their respective average. This step also removed a couple hundred rows and left the set size at now only 6775 valid rows. 
      * Step 6 addressed potential issues with restrained numerical columns, which if found none of, and no columns were removed. 
      * Step 7 ensured that the values returned in restricted option sttring columns were appropriate for that columns and the pending analysis that would use the values in these columns. A couple more rows were removed here for invalid or vague values leaving a total valid dataset size of 6619 updated and validated rows. 

4.  Provide the annotated code you will use to mitigate the data quality issues—including anomalies—in the data set in an executable script file.

5.  Provide a copy of the cleaned data set as a CSV file.

6.  Summarize the limitations of the data-cleaning process.

7.  Discuss how the limitations summarized in part D6 could affect the analysis of the question or decision from part A.



## E.  Apply principal component analysis (PCA) to identify the significant features of the data set by doing the following:

1.  Identify the total number of principal components and provide the output of the principal components loading matrix.

2.  Justify the reduced number of the principal components and include a screenshot of a scree plot.

3.  Describe how the organization would benefit from the use of PCA.



# Part IV. Supporting Documents

## G.  Acknowledge web sources
* https://docs.python.org/3/library/csv.html
* https://linuxhint.com/inline-if-else-statement-python/
* https://docs.python.org/3/library/functions.html#func-range
* https://www.w3schools.com/python/python_for_loops.asp
* https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/#
* https://www.w3schools.com/python/ref_string_isalpha.asp
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
* https://www.statology.org/pandas-filter-by-boolean-column/