# Manual Testing

[Back to README](README.md)

The purpose of this document is to summarise the process, results, bugs and fixes as part of testing the Fresh Casts website.

Where a feature or functionality requires the support of multiple html files, for example the mobile/main-navs supporting the index page, I have tested the homepage page in its entirety, including the footer (as opposed to testing this files separately).

All tests were performed using the live environment deployed from Heroku.


<br>


## User Story Testing

The objective of this test is to validate that the user requirements have been delivered for the MVP release.
Further details of the Epics, Features and User Story tasks can be found either in the [GitHub Projects Kanban Board](https://github.com/users/RickofManc/projects/4), as an overview within the Design Thinking section of the [README](README.md) or within the Fresh_Casts_Planning excel file in the [GitHub Repo](https://github.com/RickofManc/fresh-casts).

<br>




<br>


## Page Validation

This test aims to check all features and links from across the site are working as designed and developed.

To perform the test I used a Chrome browser, and validated each page from a mobile and desktop perspective using the inbuilt developer tool as some features were unique to a particular screen size.

<br>



<br>

## Responsiveness

To test the websites layout and content remains well structured and accessible across differing screen sizes, I used Chrome's Developer Tools to virtualise how the website and all its pages look and feel. In consideration that I opted to use Bootstrap which provides standard media queries for screen sizes from XS through to XL, I selected the following screens to test on; iPhone 4, iPhone SE, Samsung Galaxy S8, iPad, iPad Pro, Laptop at 1366x768, Monitor at 1920x1080 and iMac 5K.

<br> 



<br>

## Accessibility 

Key to any successful website is ensuring its accessibility. As well as using Chrome's Developer Tools to test each html page, I also used the [WAVE online assessment tool](https://wave.webaim.org/) as I feel this provides a deeper level of insight and is clearer in highlighting where improvements are required.
To achieve a pass, each page had to have 0 Errors and 0 Contrast Errors from WAVE, or +90% from Chrome's Developer Tools.

Summary of the results;
* When using WAVE, it was not possible to run a test on the pages where authentication was required; add_post.html, delete_post.html, edit_profile.html and update_post.html. In this scenario Chrome's Developer Tools helped in providing the assessment.

<br>

| File path                                                               | File Type | Result |
| ----------------------------------------------------------------------- | --------- | --------- |
| templates/account/login.html                                            | HTML      | PASS      |
| templates/account/logout.html                                           | HTML      | PASS      |
| templates/404.html                                                      | HTML      | PASS      |
| templates/500.html                                                      | HTML      | PASS      |
| templates/about.html                                                    | HTML      | PASS      |
| templates/accessibility\_statement.html                                 | HTML      | PASS      |
| templates/add\_post.html                                                | HTML      | NP        |
| templates/categories.html                                               | HTML      | PASS      |
| templates/change-password.html                                          | HTML      | PASS      |
| templates/contact.html                                                  | HTML      | PASS      |
| templates/copyright\_statement.html                                     | HTML      | PASS      |
| templates/delete\_post.html                                             | HTML      | NP        |
| templates/edit\_profile.html                                            | HTML      | NP        |
| [https://fresh-casts.herokuapp.com](https://fresh-casts.herokuapp.com/) | HTML      | PASS      |
| templates/post\_detail.html                                             | HTML      | PASS      |
| templates/sign\_up.html                                                 | HTML      | PASS      |
| templates/update\_post.html                                             | HTML      | NP        |
| templates/user\_agreement.html                                          | HTML      | PASS      |

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



#### **Accessibility**

The website has been thoroughly tested throughout all pages using the [Wave (Web Accessibility Evaluation Tool)](https://wave.webaim.org/). In general all pages performed well with 0 Errors identified.

A general theme was identified as Alerts where 'Adjacent links go to the same URL.' was noted. An example of this is within the 'Sign Up' page where a link is offered within the text to navigate to the 'Sign In' page if you already have an account. As the Nav-Menu and Footer offer the same link an Alert was raised. Consideration was given and where deemed necessary, workable links have been removed to avoid additional navigation and repetition for keyboard and screen reader users.




#### **Lighthouse** 


Using Lighthouse testing within Chrome Developer Tools, the website has been tested for use on Desktop and Mobile devices. 
The website scored well across all criteria, however further work was required to;
- improve the contrast of the background to foreground for Accessibility,
- ensure there was sufficient spacing between Footer links for mobile users,
- transform all future images uploaded to webP format and 300x300px in size to improve page loading times.
Site wide research to improve Best Practices is required to add security where front-end JavaScript libraries are being used, in this case, jQuery as part of the Bootstrap use which scored a 3 for Vulnerability Count."																	
																	
Testing occurred using Lighthouse within Chrome Dev Tools on 4 July 2022 with the following results:



#### **Feature**

Testing in Development and Production has been performed to ensure all the committed features for the MVP are working as designed. A table of results is available below.

