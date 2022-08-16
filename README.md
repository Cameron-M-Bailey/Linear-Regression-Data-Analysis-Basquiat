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



