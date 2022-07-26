# **Thunderbird and Whale Bookstore System- Project Portfolio 3 - Python.**

The Thunderbird and Whale bookstore system is based on the notorious bookstore that Bella Swan is seen to visit in Twilight. It's situated in the town of Forks which has a very simplistic and calm nature surrounding the town- similarly, the app system I created also does not have an overload of information, The app is simply useful as it allows the owners of the bookstore to effectively and quickly recieve data on how many books the need to order into the shop at the beginning of the new week by calculating how many books were sold, ordered and the difference between these figures.

The live site is available for viewing here - <a href="https://***" target="_blank" rel="noopener">Thunder and Whale Bookstore System.</a>

![Thunderbird and Whale responsive design](assets/images/readme-images/responsiveness.png)

# Contents

* [**Objective**](<#objective>)
* [**User Experience UX**](<#user-experience-ux>)
    * [Design Prototype](<#design-prototype>)
    * [System Structure](<#system-structure>)
    * [Python Logic](<#python-logic>)
    * [Data](<#data>)
    * [Design Choices](<#design-choices>)
    * [Colour Scheme](<#colour-scheme>)
* [**Features**](<#features>)
    * [Startup](<#startup>)
    * [Welcome Text](<#welcome-text>)
    * [Input Instructions](<#input-instructions>)
    * [Feedback](<#feedback>)
    * [Updates](<#updates>)
    * [Results](<#results>)
* [**Future Features**](<#future-features>)
    * [Last Restock Comparisons](<#last-restock-comparisons>)
* [**Technologies Used**](<#technologies-used>)
* [**Python Packages**](<#python-packages>)
* [**Testing**](<#testing>)
* [**Deployment To Heroku**](<#deployment-to-heroku>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)

# Objective

For my third project I wanted to create something simple, useful and something that still related to one of my passions. As a huge Twilight fan and bookworm that would love to own a book shop this simple but effective system is perfect. I believe this system of calculating future orders needed is also something that can be used by all business, just differin g in scale, therefore it is simple but highly effective.

[Back to Contents](<#contents>) 

# User Experience (UX)

## Design Prototype

I used Figma to design a very basic wireframe as I knew this command line application would be simple in its appearance. The system still ended up being slightly different with a dark brown background being used as opposed to a dark green and a button instead of a title above the terminal. However, I still preserved the simplistic and cozy theme of the site.

![Figma Design Prototype](assets/images/readme-images/Figma.png)

[Back to Contents](<#contents>)

## System Structure

The very simple Thunderbird and Whale Bookstore system simply contains a command line interface where the user is guided on what data they will need to input. Just above the interface is a 'Run System' button which allows for the site to be reloaded.

## Python Logic

I used the paint app on Windows to create a simple flowchart to showcase my python logic and how the system will process the data input and reach the final result message.

![Python Flow Chart](assets/images/readme-images/project%203%20flow.png)

## Data

For this site, Google Sheets was used to store the data, update the data and compare the data. The [Google Sheet](https://docs.google.com/spreadsheets/d/1jorvEpWdPbdxXYKE7Tm0hVA3ahgTq5oP5v7CksHYmNc/edit#gid=1680754323) has three different worksheets, with one containing the data for the amound of books sold, another with the amount of books ordered and lastly a worksheet storing the difference between the two former worksheets so the bookstore can see if there was a surplus of data or not.

![Google Sheets](assets/images/readme-images/sold.png)
![Google Sheets](assets/images/readme-images/ordered.png)
![Google Sheets](assets/images/readme-images/difference.png)

## Colour Scheme
-  Aligning with the gloomy and very cozy nature of the Twilight Saga movies, and the Thunderbird and Whale bookstore in the movie I kept the colours very cozy, and dark, reflecting the colours of nature as Twilight contains a large amount of nature imagery.
- Therefore, I decided to go for a dark brown for the background colour and I used a forest green for the 'Run System' button. The interface being black complients these colour well, with the white of the text allowing for efficient contrast for accessibility purposes.

[Back to Contents](<#contents>)

# Features

## Start Up

* When the site is first loaded the user will see is the interface with the Run System button above it. There will be a message letting the user know that the start up command is running.

![Start Up Image](assets/images/readme-images/start%20up.png)

## Welcome Text

* The site also provides the user with a fun and lively welcome text which briefly informs the user of what the system is about and what the interface will need help with.

![Welcome Text](assets/images/readme-images/start%20up.png)

## Input Instructions

* On the screen is also instructions prompting the user to input the amount of each book that was sold the previous day, at the bottom the user can input their data.

![Input Instructions](assets/images/readme-images/start%20up.png)

## Feedback

* If the user enters invalid data, by not entering the correct amount of numbers or by not entering a number at all and accidently entering a word for example, the system will present the user with a message letting them know of this so they know what they did wrong and can try again with the correct data.

![Feedback](assets/images/readme-images/invalid%20values%20msg.png)
![Feedback](assets/images/readme-images/word%20not%20number.png)

## Updates

* If the data is valid, the user will be met with a message clarifying this. The interface will then update each worksheet consecutively and print a message to the user as each updates so that the user knows what is happening, that it has happened and that their worksheets have successfully been updated.

![Update](assets/images/readme-images/valid%20data.png)

## Results 

* Finally, the final outcome of how many of each book is needed to be ordered by the bookstore owner is printed, each book followed by the amount that needs to be ordered, or if there actually are books that need to be ordered less. The bookstore owner has done this in a fast, simple and reliable system.

![Results](assets/images/readme-images/results.png)

[Back to Contents](<#contents>)

## Future Features

### Last Restock Comparisons

* In future versions I would allow for the user to see a comparison between the stock needed for this week and last week so the owner can know which books are rising in popularity, falling in popularity, what people are preferring to buy and how they can change their ordered to reflect this data and cause a greater profit.

## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality of the website.
* [a11y](https://color.a11y.com/Contrast/) - Used to test the contrast and accessibility.
* [GitHub](https://github.com/) - Used to host and deploy the website.
* [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - Used to test responsiveness and debug.
* [Am I Responsive?](https://ui.dev/amiresponsive) - USed to test responsiveness of website.
* [Figma](https://www.figma.com/files/recent?fuid=1098191112256560055) - USed to create design prototype.
* [Google Sheets](https://www.google.co.uk/sheets/about/) - Used to host the application data.

## Python Packages

* [GSpread](https://pypi.org/project/gspread/) - Used to transfer data between google sheets.



