# Linear-Regression-Data-Analysis-Basquiat
### An analysis of Basquiat’s top selling works & a multiple linear regression to predict prices.
# Objective 
This project analyzes Basquait’s top art pieces with the highest hammer prices (sale prices in auctions). Aspects such as dimensions (length, width, area), year created, number of unique colors, and others, were explored as features.

A multiple linear regression was implemented to estimate and predict hammer prices for Basquiat’s works. This can be used by art collectors to estimate their maximum bids for auctions, attain values for price negotiations, predict high-value pieces for maximal return on investment, and predict the value of their current Basquiat collection. 
# Dataset 
The dataset contains the hammer prices in millions (USD) and other attributes of Basquiat’s top-selling paintings & drawings. Data was manually compiled from Artprice.com. Unique Colors, Contrast Score, and Brightness Score were determined with functions utilizing computer vision from Stack Overflow. Functions used and credit given to the appropriate contributors can be found in the Basquiat Artwork Evaluator Repository. Features include: 

<b>Title:</b> title of work<br>
<b>Type:</b>  type of art form<br>
<b>Primary Medium:</b>  primary medium used<br>
<b>Year Created:</b>  year work was created <br> 
<b>Length:</b>  length in inches (14--145)<br>
<b>Width:</b>  width in inches (11--211)<br>
<b>Area:</b>  area of work inches (154--21025)<br>
<b>Size:</b>  size of work (small, medium, large)<br>
<b>Hammer Price:</b>  selling price of work in millions (USD)<br>
<b>Seller:</b>  auction house who sold work<br>
<b>Seller City:</b>  city work sold<br>
<b>Seller Country:</b>  country work sold<br>
<b>Month:</b>  month work sold<br> 
<b>Year:</b>  year work sold<br>
<b>Unique Colors:</b>  number of unique colors in work (14392--592217)<br>
<b>Contrast Score:</b>  average contrast in work (2.50--46.46)<br>
<b>Brightness Score:</b>  average brightness in work (45.30--243.90)<br>

Low Unique Colors             |  High Unique Colors
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/104586192/184936789-dfe3d36e-2eec-450d-b6c8-28ae878517aa.jpeg" width="200" height="200">|<img src="https://user-images.githubusercontent.com/104586192/184937292-2186dec2-9616-4e9e-9ddf-05b70b630408.jpeg" width="200" height="200">


Low Contrast Score           |  High Contrast Score
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/104586192/184940640-cd4467f4-9d91-4a3c-bebd-a4bc1cb03983.jpeg" width="200" height="200">|<img src="https://user-images.githubusercontent.com/104586192/184938361-dd57f894-c761-4fd8-861e-2143aa1e6e45.jpeg" width="200" height="200">

Low Brightness Score           |  High Brightness Score
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/104586192/184939423-e7c1e973-e0da-4e4a-a47c-1d534a3b528f.jpeg" width="200" height="200">|<img src="https://user-images.githubusercontent.com/104586192/184940269-25ba4b83-81cf-4374-b186-11a50913084f.jpeg" width="200" height="200">

<b>Credit:</b> Photos from Artprice Images®

# The Process
## Data Cleaning 

```
Excel= 

#Duplicate Slide to ensure no data is lost during cleaning. 

#Convert 'Mixed Media' types to 'Painting' due to limited number and primary medium being acrylic paint.
=SUBSTITUTE([cell], "Mixed Media","Painting") 

#Ensure area has no missing or irregular values 
=MIN([Area column]) and =MAX([Area column])

#Extract year from Year Sold Date 
=RIGHT([cell],4)

#Split paintings & drawings into small, medium, and large.
=IF([cell]<=1877,"Small",IF(AND([cell]>=1878,[cell]<=12312),"Medium",IF([cell]>=12313,"Large","Null")))
```
## Baseline Model

A naïve model was built to serve as a benchmark for trained model. 

<img width="425" alt="Screen Shot 2022-08-16 at 1 49 13 PM" src="https://user-images.githubusercontent.com/104586192/184945590-bd114016-7600-44b7-aad8-b51917c535be.png">

<b>Mean Absolute Error:</b> 9.007 <br>
<b>Mean Squared Error:</b> 217.589<br>
<b>Root Mean Square Error:</b> 14.751<br>

## Exploratory Data Analysis

Hammer Price is highly correlated with Area and Number of Unique Colors as well as slightly correlated with Contrast Score. 

<img width="750" alt="Screen Shot 2022-08-16 at 1 56 18 PM" src="https://user-images.githubusercontent.com/104586192/184946886-e69f9ac7-88d6-4344-b29b-4c7ab885bed2.png">

On average, paintings are worth 5x drawings. 

<img width="402" alt="Screen Shot 2022-08-16 at 2 02 13 PM" src="https://user-images.githubusercontent.com/104586192/184947991-0923cbe9-9a59-4c39-9bcb-bbd6231d8cf5.png">

On average, Basquiat's most popular medium, Acrylic, goes for the highest Hammer Price. This is followed by Oilstick, Colored Pencils, and Pastels, respectively. 

<img width="757" alt="Screen Shot 2022-08-16 at 2 04 39 PM" src="https://user-images.githubusercontent.com/104586192/184948419-5e9d61d9-7d0d-4f07-a2b1-822c5f258cab.png">

His most popular, highest selling works were created early career in his career from 1981-3, which make up about 83% of total sales. 1982 is his most popular year making up 52% of total sales. 

<img width="760" alt="Screen Shot 2022-08-16 at 2 18 01 PM" src="https://user-images.githubusercontent.com/104586192/184950710-cb8cb208-cab4-4b1c-b02f-b17ce9ba9fc2.png">

### Color Features
A high number of unique colors has the best correlation with a high Hammer Price.

<img width="415" alt="Screen Shot 2022-08-16 at 3 12 54 PM" src="https://user-images.githubusercontent.com/104586192/184962895-120fe941-5dc4-4420-b7d3-0309b38b9fe0.png">

Contrast Score has a slight positve correlation with Hammer Price.

<img width="411" alt="Screen Shot 2022-08-16 at 3 13 34 PM" src="https://user-images.githubusercontent.com/104586192/184963006-73e06533-42ff-4752-98e5-892956befc9d.png">

Brightness Score actually negatively impacts Hammer Price.

<img width="403" alt="Screen Shot 2022-08-16 at 3 13 53 PM" src="https://user-images.githubusercontent.com/104586192/184963051-8cf0c40f-3f69-43b6-9439-a781d3d4c7c5.png">


## Preprocessing
### Remove outliers from features correlated with Hammer Price 
```
#Remove outliers from Area which do not follow general trend of data.
df.drop(df[df['Area (in)'] > 20000].index,axis=0,inplace=True)
df.drop(df[df['Hammer Price (USD in millions)']>80].index,axis=0,inplace=True)
```
<img width="432" alt="Screen Shot 2022-08-16 at 2 34 45 PM" src="https://user-images.githubusercontent.com/104586192/184953542-4954bc07-53a3-4a37-9b3f-fac7c727bbc3.png">

<img width="427" alt="Screen Shot 2022-08-16 at 2 33 38 PM" src="https://user-images.githubusercontent.com/104586192/184953295-696d4ac2-4465-455e-8d79-1bdbea5e3783.png">

```
#Remove outliers from Unique Colors which do not follow general trend of data.
df.drop(df[df['Hammer Price (USD in millions)']>70].index,axis=0,inplace=True)
```

<img width="418" alt="Screen Shot 2022-08-16 at 2 39 13 PM" src="https://user-images.githubusercontent.com/104586192/184954269-7dec2e57-13e0-4457-ba17-3cdc851a9dd4.png">

<img width="411" alt="Screen Shot 2022-08-16 at 2 39 23 PM" src="https://user-images.githubusercontent.com/104586192/184954300-c3265de0-90f7-4e34-bf28-0618ce430451.png">

```
#Remove outliers from Contrast Score which do not follow general trend of data.
df.drop(df[(df['Contrast Score']<20) & (df['Hammer Price (USD in millions)']>30)].index,axis=0,inplace=True)
```
<img width="404" alt="Screen Shot 2022-08-16 at 2 43 53 PM" src="https://user-images.githubusercontent.com/104586192/184955097-f361406f-609a-4a9a-8696-20963ade3360.png">

<img width="404" alt="Screen Shot 2022-08-16 at 2 44 20 PM" src="https://user-images.githubusercontent.com/104586192/184955186-959aa2c1-3d81-4f32-9b1d-54311c8f78f1.png">

### Remedy right-skewed data

```
#View current distrubtion of data.
hammer_price = (df['Hammer Price (USD in millions)'])
hammer_price.skew() #2.01
sns.displot(x=hammer_price,data=df,kde=True)
```
<img width="370" alt="Screen Shot 2022-08-16 at 2 52 57 PM" src="https://user-images.githubusercontent.com/104586192/184957621-b63860db-7b35-41e0-be44-ae4145b46b3b.png">

```
#Transform data into normal distrubtion.
price_log = np.log(df['Hammer Price (USD in millions)'])
price_log.skew() #-0.32

#Confirm distribution is normally distributed. 
sns.displot(x=price_log,data=df,kde=True)
```
<img width="358" alt="Screen Shot 2022-08-16 at 2 56 36 PM" src="https://user-images.githubusercontent.com/104586192/184959088-1a1a52a0-d227-4fd3-b263-1a17d2443ce8.png">

### Feature Engineering for Categorical Data 

```
#Drop unessacary columns.
df.drop(['Title','Length (in)','Width (in)','Seller Country','Month'],axis=1,inplace=True)

#Converting our categorial variables 
art_type = pd.get_dummies(df['Type'],drop_first=True)
primary_medium = pd.get_dummies(df['Primary Medium'],drop_first=True)
size = pd.get_dummies(df['Size'],drop_first=True)
seller = pd.get_dummies(df['Seller'],drop_first=True)
seller_city = pd.get_dummies(df['Seller City'],drop_first=True)

#Drop columns which have already been converted into dummies. 
df.drop(['Type','Primary Medium','Size','Seller','Seller City'],axis=1,inplace=True)

#Add dummies to the original DataFrame
df = pd.concat([df,art_type,primary_medium,size,seller,seller_city],axis=1)
```

# Build Linear Regression Model

```
#Split data into train and test data. 
X_train, X_test, y_train, y_test = train_test_split(df.drop('Hammer Price (USD in millions)',axis=1), price_log, test_size=0.30)

#Standardize and fit our training data.
scaler = StandardScaler()
scaler.fit(X_train)

#Transform our training and test data. 
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Train our model
lm = LinearRegression()
lm.fit(X_train,y_train)

#Test our model
predictions = lm.predict(X_test)

#Results 
plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
```
<img width="400" alt="Screen Shot 2022-08-16 at 3 08 52 PM" src="https://user-images.githubusercontent.com/104586192/184962167-0ffdec62-82e6-4dd7-ad51-68afc1748b13.png">

<b>Mean Absolute Error:</b> 0.473 <br>
<b>Mean Squared Error:</b> 0.394<br>
<b>Root Mean Square Error:</b> 0.638<br>

*Compared to our baseline model this is a vast improvement with a MSE of about 0.4.*

# Key Takeaways
To view the interactive dashboard, please visit my Tableau Public profile <a href="https://public.tableau.com/app/profile/cameron6348" target="_blank">here</a>.
                                                    
                                                

