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
* relevant techniques  
* specific steps needed to assess the quality of the data in the data set.

###  Justify your approach for assessing the quality of the data, including the following:
* characteristics of the data being assessed
* the approach used to assess the quality of the data

###  Justify your selected programming language and any libraries and packages that will support the data-cleaning process.

### Provide the annotated code you will use to assess the quality of the data in an executable script file.

# Part IV. Supporting Documents

## G.  Acknowledge web sources
* https://docs.python.org/3/library/csv.html
* 