# Regression-Data-Analysis-Basquiat
### An analysis of Basquiat’s top selling works & a linear regression and k-NN model to predict prices.
# Objective 
This project analyzes Jean Michel Basquait’s top art pieces with the highest hammer prices (sales price in auctions). Aspects such as dimensions (length, width, area), year created, number of unique colors, and others, were explored as features.

A multiple linear regression was implemented to estimate and predict hammer prices for Basquiat’s works. This can be used by art collectors and galleries to estimate their maximum bids for auctions, attain values for price negotiations, predict high-value pieces for maximal return on investment, and predict the value of their current Basquiat collection. 
# Dataset 
The dataset contains the hammer prices in millions (USD) and other attributes of Basquiat’s top-selling paintings & drawings. Data was manually compiled from Artprice.com. Unique Colors, Contrast Score, and Brightness Score were determined with functions utilizing computer vision from Stack Overflow. Functions used and credit given to the appropriate contributors within the Basquiat Artwork Evaluator repository. Features include: 

<b>Title:</b> title of work<br>
<b>Type:</b>  type of art form<br>
<b>Primary Medium:</b>  primary medium used<br>
<b>Year Created:</b>  year work was created <br> 
<b>Length:</b>  length in inches (14--145)<br>
<b>Width:</b>  width in inches (11--211)<br>
<b>Area:</b>  area of work in inches (154--21025)<br>
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

#Duplicate slide to ensure no data is lost during cleaning. 

#Convert 'Mixed Media' types to 'Painting' due to limited count and primary medium being acrylic paint.
=SUBSTITUTE([cell], "Mixed Media","Painting") 

#Ensure area has no missing or irregular values 
=MIN([Area column]) and =MAX([Area column])

#Extract year from Year Sold Date 
=RIGHT([cell],4)

#Split paintings & drawings into small, medium, and large.
=IF([area]<=1877,"Small",IF(AND([area]>=1878,[area]<=12312),"Medium",IF([area]>=12313,"Large","Null")))
```
## Exploratory Data Analysis

Hammer Price is highly correlated with Area and Number of Unique Colors as well as slightly correlated with Contrast Score. 

<img width="750" alt="Screen Shot 2022-08-16 at 1 56 18 PM" src="https://user-images.githubusercontent.com/104586192/184946886-e69f9ac7-88d6-4344-b29b-4c7ab885bed2.png">

```python3
# Drop features highly correlated to each other or redundant
df.drop(['Width','Length','Size'],axis=1,inplace=True)
```

On average, paintings are worth 5x drawings. 

<img width="402" alt="Screen Shot 2022-08-16 at 2 02 13 PM" src="https://user-images.githubusercontent.com/104586192/184947991-0923cbe9-9a59-4c39-9bcb-bbd6231d8cf5.png">

On average, Basquiat's most popular medium, Acrylic, goes for the highest Hammer Price. This is followed by Oilstick, Colored Pencils, and Pastels, respectively. 

<img width="757" alt="Screen Shot 2022-08-16 at 2 04 39 PM" src="https://user-images.githubusercontent.com/104586192/184948419-5e9d61d9-7d0d-4f07-a2b1-822c5f258cab.png">

His highest selling works were created early career in his career from 1981-3, which make up about 83% of total sales. 1982 is his most popular year making up 52% of total sales. 

<img width="760" alt="Screen Shot 2022-08-16 at 2 18 01 PM" src="https://user-images.githubusercontent.com/104586192/184950710-cb8cb208-cab4-4b1c-b02f-b17ce9ba9fc2.png">

### Color Features
A high number of unique colors has the best correlation with a high Hammer Price.

<img width="415" alt="Screen Shot 2022-08-16 at 3 12 54 PM" src="https://user-images.githubusercontent.com/104586192/184962895-120fe941-5dc4-4420-b7d3-0309b38b9fe0.png">

Contrast Score has a slight positve correlation with Hammer Price.

<img width="411" alt="Screen Shot 2022-08-16 at 3 13 34 PM" src="https://user-images.githubusercontent.com/104586192/184963006-73e06533-42ff-4752-98e5-892956befc9d.png">

Brightness Score actually negatively impacts Hammer Price.

<img width="403" alt="Screen Shot 2022-08-16 at 3 13 53 PM" src="https://user-images.githubusercontent.com/104586192/184963051-8cf0c40f-3f69-43b6-9439-a781d3d4c7c5.png">


## Preprocessing
### Remove outliers from features positively correlated with Hammer Price 
```python3
#Remove outliers from Area which do not follow general trend of data.
df.drop(df[df['Area (in)'] > 20000].index,axis=0,inplace=True)
df.drop(df[df['Hammer Price']>80].index,axis=0,inplace=True)
```
<img width="432" alt="Screen Shot 2022-08-16 at 2 34 45 PM" src="https://user-images.githubusercontent.com/104586192/184953542-4954bc07-53a3-4a37-9b3f-fac7c727bbc3.png">

<img width="427" alt="Screen Shot 2022-08-16 at 2 33 38 PM" src="https://user-images.githubusercontent.com/104586192/184953295-696d4ac2-4465-455e-8d79-1bdbea5e3783.png">

```python3
#Remove outliers from Unique Colors which do not follow general trend of data.
df.drop(df[df['Hammer Price']>70].index,axis=0,inplace=True)
```

<img width="418" alt="Screen Shot 2022-08-16 at 2 39 13 PM" src="https://user-images.githubusercontent.com/104586192/184954269-7dec2e57-13e0-4457-ba17-3cdc851a9dd4.png">

<img width="411" alt="Screen Shot 2022-08-16 at 2 39 23 PM" src="https://user-images.githubusercontent.com/104586192/184954300-c3265de0-90f7-4e34-bf28-0618ce430451.png">

```python3
#Remove outliers from Contrast Score which do not follow general trend of data.
df.drop(df[(df['Contrast Score']<20) & (df['Hammer Price']>30)].index,axis=0,inplace=True)
```
<img width="404" alt="Screen Shot 2022-08-16 at 2 43 53 PM" src="https://user-images.githubusercontent.com/104586192/184955097-f361406f-609a-4a9a-8696-20963ade3360.png">

<img width="404" alt="Screen Shot 2022-08-16 at 2 44 20 PM" src="https://user-images.githubusercontent.com/104586192/184955186-959aa2c1-3d81-4f32-9b1d-54311c8f78f1.png">

### Remedy right-skewed data

```python3
#View current distrubtion of our y-value (Hammer Price).
hammer_price = (df['Hammer Price'])
hammer_price.skew() #2.01
sns.displot(x=hammer_price,data=df,kde=True)
```
<img width="370" alt="Screen Shot 2022-08-16 at 2 52 57 PM" src="https://user-images.githubusercontent.com/104586192/184957621-b63860db-7b35-41e0-be44-ae4145b46b3b.png">

```python3
#Transform y-value (Hammer Price) into normal distrubtion.
price_log = np.log(df['Hammer Price'])
price_log.skew() #-0.32

#Confirm distribution is normally distributed. 
sns.displot(x=price_log,data=df,kde=True)
```
<img width="358" alt="Screen Shot 2022-08-16 at 2 56 36 PM" src="https://user-images.githubusercontent.com/104586192/184959088-1a1a52a0-d227-4fd3-b263-1a17d2443ce8.png">

### Transforming Categorical Data 

```python3
# Drop unnecessary and redundant columns 
df.drop(['Title','Seller Country'],axis=1,inplace=True)

#Converting our categorial variables 
predictors_df = df.drop(['Hammer Price'],axis=1)
target_df = df['Hammer Price']
predictors_df = pd.get_dummies(predictors_df, drop_first = True)
```
### Normalizing Data 

```python3
z_score_norm = preprocessing.StandardScaler()
predictor_df_normalized = z_score_norm.fit_transform(predictors_df)
predictor_df_normalized = pd.DataFrame(predictor_df_normalized, columns = predictors_df.columns)
```


# Build Linear Regression Model

```python3
X = predictor_df_normalized
y = target_df.reset_index(drop = True)
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)
linear_model = LinearRegression()
linear_model = linear_model.fit(train_X, train_y)

# print performance metrics on training set
predicted_y_training = linear_model.predict(train_X)
print(regressionSummary(train_y, predicted_y_training))
print('Adjusted R-Squared',adjusted_r2_score(train_y, predicted_y_training, linear_model))

```

<img width="448" alt="Screen Shot 2022-11-07 at 12 59 57 PM" src="https://user-images.githubusercontent.com/104586192/200381853-2b4442de-84fa-4229-a6fb-2a6a8f2961df.png">

```python3

# test model on test data
predicted_y_test = linear_model.predict(test_X) 

# print performance metrics on test set
regressionSummary(test_y, predicted_y_test)
```

<img width="450" alt="Screen Shot 2022-11-07 at 1 00 22 PM" src="https://user-images.githubusercontent.com/104586192/200381961-13c5d08d-0b11-4076-b2fc-d4858a26c87e.png">

Relatively good performance metrics, so we are confident the model is a good fit. Based on the low variance between the train and test metrics, I am confident the model is not overfit.

# Build k-NN Model

Let's compare it to a k-NN model. 

```python3
X = predictor_df_normalized
y = target_df.reset_index(drop = True)
train_X_prediction, test_X_prediction, train_y_prediction, test_y_prediction = train_test_split(X, 
                                                            y, test_size=0.3)
 
 # let's find the optimal k value
results = []
for k in range(1, 30):
    knn = KNeighborsRegressor(n_neighbors=k).fit(train_X_prediction, train_y_prediction)
    results.append({
        'k': k,
        'RMSE': round(mean_squared_error(test_y_prediction, knn.predict(test_X_prediction)) ** 0.5, 4)
    })

# Convert results to a pandas data frame
results = pd.DataFrame(results)
print(results)
```
<img width="829" alt="Screen Shot 2022-11-07 at 1 00 58 PM" src="https://user-images.githubusercontent.com/104586192/200382069-f1d1c46c-6134-45f0-acf7-ea2ade2a3548.png">

```python3
# Optimal k = 14
knn_p = KNeighborsRegressor(n_neighbors=14).fit(train_X_prediction, train_y_prediction)
predicted_y_training3 = knn_p.predict(train_X_prediction)
print("Root Mean Squared Error (RMSE): ", round(mean_squared_error(train_y_prediction, predicted_y_training3) ** 0.5, 4))
```
k-NN model at k=14 performs slightly better and thus should be deployed over the linear regression model.


# Key Takeaways
- Overall, acrylic paintings hold the most value for Basquiat's artwork, the only exception is an Untitled 1981 Oilstick piece which sold for $23.5 million.
- Paintings from Basquiat's early career (1981-3) are considered the most valuable and coveted with 1982 being considered his best works.
- Although drawings are significantly less valuable than his paintings, oilstick and ink drawings will still net decent hammer prices with the highest priced drawing being worth $13.1 million. 
- Basquiat's artwork with a variety of unique colors and high contrast (high difference between its lightest and darkest shades) will be worth slightly more than those without these features; brighter artworks seem to be worth slightly less. 
- Basquiat sales fluctuate every couple of years, but 2021 saw a massive spike in sales due to the height of the #BlackLivesMatter movement and becoming a popular collaborator with large brands.

To view the interactive dashboard, please visit my Tableau Public profile <a href="https://public.tableau.com/app/profile/cameron6348">here</a>.

<img width="1002" alt="Screen Shot 2022-08-22 at 5 15 45 PM" src="https://user-images.githubusercontent.com/104586192/186020526-a4366169-127b-44b5-8c26-29b857ee66a9.png">

<img width="641" alt="Screen Shot 2022-08-22 at 5 14 08 PM" src="https://user-images.githubusercontent.com/104586192/186020363-a6f978ec-6e6d-40a7-8fde-980b1bc5367e.png">

<img width="665" alt="Screen Shot 2022-08-17 at 7 19 01 PM" src="https://user-images.githubusercontent.com/104586192/185260117-ddcc4269-a314-4db1-9383-579fc7d04af7.png">

             

