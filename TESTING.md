# Manual Testing

[Back to README](README.md)

The purpose of this document is to summarise the process, results, bugs and fixes as part of manually testing the Fresh Casts website.

Where a feature or functionality requires the support of multiple html files, for example the mobile/main-navs supporting the index page, I have tested the homepage page in its entirety, including the footer (as opposed to testing this files separately).

All tests were performed using the live environment deployed from Heroku.



## Manual Testing 



<br>


## User Story Testing


<br>


## Page Validation


<br>


## Responsiveness



<br> 


## Accessibility 



<br>

 
## Performance





<br>


## Browser




<br>


## Device




<br>


## Code





<br>


### Automatic Testing

Django testing tools have been used to perform basic automated testing on Fresh Casts Python code, primarily for template rendering and some user functionality.

Tests were run using the local SQLite3 database as opposed to the production PostgreSQL database.

Test scripts were written for the following blog app files;

- models.py
- views.py
- forms.py
- admin.py

Whilst further testing is required to achieve 100%, the results thus far are highlighted in the summary report below:

<p align="center">
    <img src="readme-images/fresh-casts-blog-app-automated-testing.png" alt="Django Testing Results"/>
    </p>

<br>



## Bugs




<br>



<br>

#### **Browser**

To ensure site visitors can view and use Fresh Cast features on differing browsers, testing was performed on the test scenarios listed below.

To achieve a 'Pass' the following criteria had to be met across all website pages;
1. All buttons provide user feedback on hover and execute correctly when clicked
2. All colours load and displayed correctly
3. All elements retain integrity
4. Fonts and images load
5. Navigation is not impacted and nav-menu collapses as intended

<p align="center">
    <img src="readme-images/fresh-casts-browser-testing.png" alt="Browser Testing Results"/>
    </p>

<br>

#### **Device**

To ensure site visitors can view and use Fresh Cast on differing devices, testing was performed on the test scenarios listed below.
This physical testing is in addition to the continual device testing as part of UX development using Chrome Developer tools.
				
To achieve a 'Pass' the following criteria had to be met across all website pages;				
1. All buttons provide user feedback on hover and execute correctly when clicked				
2. All colours load and displayed correctly				
3. All elements retain integrity				
4. Fonts and images load				
5. Navigation is not impacted and nav-menu collapses as intended				

<p align="center">
    <img src="readme-images/fresh-casts-device-testing.png" alt="Device Testing Results"/>
    </p>

<br>

#### **Accessibility**

The website has been thoroughly tested throughout all pages using the [Wave (Web Accessibility Evaluation Tool)](https://wave.webaim.org/). In general all pages performed well with 0 Errors identified.

A general theme was identified as Alerts where 'Adjacent links go to the same URL.' was noted. An example of this is within the 'Sign Up' page where a link is offered within the text to navigate to the 'Sign In' page if you already have an account. As the Nav-Menu and Footer offer the same link an Alert was raised. Consideration was given and where deemed necessary, workable links have been removed to avoid additional navigation and repetition for keyboard and screen reader users.


<p align="center">
    <img src="readme-images/fresh-casts-wave-testing.png" alt="WAVE Testing Results"/>
    </p>

<br>


#### **Lighthouse** 


Using Lighthouse testing within Chrome Developer Tools, the website has been tested for use on Desktop and Mobile devices. 
The website scored well across all criteria, however further work was required to;
- improve the contrast of the background to foreground for Accessibility,
- ensure there was sufficient spacing between Footer links for mobile users,
- transform all future images uploaded to webP format and 300x300px in size to improve page loading times.
Site wide research to improve Best Practices is required to add security where front-end JavaScript libraries are being used, in this case, jQuery as part of the Bootstrap use which scored a 3 for Vulnerability Count."																	
																	
Testing occurred using Lighthouse within Chrome Dev Tools on 4 July 2022 with the following results:


<p align="center">
    <img src="readme-images/fresh-casts-lighthouse-testing.png" alt="Lighthouse Testing Results"/>
    </p>

<br>


#### **Feature**

Testing in Development and Production has been performed to ensure all the committed features for the MVP are working as designed. A table of results is available below.


<p align="center">
    <img src="readme-images/fresh-casts-feature-testing.png" alt="Feature Testing Results"/>
    </p>

<br>


### Automatic Testing

Django testing tools have been used to perform basic automated testing on Fresh Casts Python code, primarily for template rendering and some user functionality.

Tests were run using the local SQLite3 database as opposed to the production PostgreSQL database.

Test scripts were written for the following blog app files;

- models.py
- views.py
- forms.py
- admin.py

Whilst further testing is required to achieve 100%, the results thus far are highlighted in the summary report below:

<p align="center">
    <img src="readme-images/fresh-casts-blog-app-automated-testing.png" alt="Django Testing Results"/>
    </p>

<br>
