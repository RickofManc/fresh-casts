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
* The test highlight multiple links to the same page. This was prevalent on the homepage where there was a link to categories in the navbar drop-down menu, and another within the post details in the homepage page list view. To improve the experience for users with screen readers I opted to remove the category name and link from each post, and instead allow users to navigate using the navbar menu only.

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

Writing well formed, quality code is essential for the future development of this, or any website. To support this aim I have used industry standard tools [list below] to validate every line of code using the input method. As well as using these tools, using GitPod as IDE allowed me to utilise the inbuilt code checkers such as Pycodestyle for Python. The 404 and 500 error pages passed the test using the direct input method as opposed to the URL as the page was not visible to the W3 Validator via this method.

* W3 Validator for HTML
* W3 Jigsaw for CSS
* CI Python Linter for Python

To gain passes across the code base I had to address minor issues such as;

* Python - General formatting and resolving E501 line length errors.
* Python - Adding new lines to the end of Python files to resolve W292 errors.
* Python - All python files were reporting "Django was not configured. For more information run pylint --load-plugins=pylint_django --help-msg=django-not-configured" on investigation and support from [Stack Overflow](https://stackoverflow.com/questions/65761250/pylint-django-raising-error-about-django-not-being-configured-when-thats-not-th), I added code to support the pylint plugin within the settings.json file. This removed the warning message. 
* Python - Reported from pycodestyle on blog/tests_models.py and tests_views.py files; Class method setUpTestData should have 'cls' as first argument instead of 'self'. I researched this issue and found other developers noting this was a style issue, and that the tests in question were effective when using 'self'. The warning message was removed following the fix above to configure the pylint plugin differently.
* Python - Reported from pycodestyle on the blog/views.py file on four occasions 'Number of parameters was 4 (...) and is now 5 in overridden (...) method'. The code past the CI Python Linter, and functionally work as designed. Whilst investigating the issue I noted it was no longer trigger following the fix above to configure the pylint plugin differently.
* HTML - Removing unnecessary trailing slashes from elements e.g. <br/>.
* HTML - Some posts were highlighting an additional </p> tag however on investigation this was dependent on how the text for the content field has been input.


The following issue was identified and not resolved so carries an 'EXC' which means passed with an acceptable exception.

* settings.py - E501 error as lines for AUTH_PASSWORD_VALIDATORS breach 79 characters. I attempted to split the code over two lines however this triggered other errors. As the code is functioning I have chosen to allow this exception for the MVP.

<br>

| File path                                                               | File Type | HTML | CSS  | JavaScript | Python | GitPod errors |
| ----------------------------------------------------------------------- | --------- | ---- | ---- | ---------- | ------ | ------------- |
| blog/admin.py                                                           | PY        |      |      |            | PASS   | 1             |
| blog/apps.py                                                            | PY        |      |      |            | PASS   | 1             |
| blog/context\_processors.py                                             | PY        |      |      |            | PASS   | 1             |
| blog/forms.py                                                           | PY        |      |      |            | PASS   | 1             |
| blog/models.py                                                          | PY        |      |      |            | PASS   | 1             |
| blog/tests\_admin.py                                                    | PY        |      |      |            | PASS   | 1             |
| blog/tests\_forms.py                                                    | PY        |      |      |            | PASS   | 1             |
| blog/tests\_models.py                                                   | PY        |      |      |            | PASS   | 1             |
| blog/tests\_views.py                                                    | PY        |      |      |            | EXC    | 1             |
| blog/urls.py                                                            | PY        |      |      |            | EXC    | 1             |
| blog/views.py                                                           | PY        |      |      |            | EXC    | 3             |
| contact/admin.py                                                        | PY        |      |      |            | PASS   | 1             |
| contact/apps.py                                                         | PY        |      |      |            | PASS   | 1             |
| contact/forms.py                                                        | PY        |      |      |            | PASS   | 1             |
| contact/models.py                                                       | PY        |      |      |            | PASS   | 1             |
| contact/urls.py                                                         | PY        |      |      |            | PASS   | 1             |
| contact/views.py                                                        | PY        |      |      |            | PASS   | 1             |
| fresh\_casts/settings.py                                                | PY        |      |      |            | EXC    | 1             |
| fresh\_casts/urls.py                                                    | PY        |      |      |            | PASS   | 1             |
| member/admin.py                                                         | PY        |      |      |            | n/a    | 1             |
| member/apps.py                                                          | PY        |      |      |            | PASS   | 1             |
| member/forms.py                                                         | PY        |      |      |            | PASS   | 1             |
| member/models.py                                                        | PY        |      |      |            | n/a    | 1             |
| member/tests.py                                                         | PY        |      |      |            | n/a    | 1             |
| member/urls.py                                                          | PY        |      |      |            | PASS   | 1             |
| member/views.py                                                         | PY        |      |      |            | PASS   | 1             |
| static/css/style.css                                                    | CSS       |      | PASS |            |        | PASS          |
| templates/account/login.html                                            | HTML      | PASS |      |            |        | PASS          |
| templates/account/logout.html                                           | HTML      | PASS |      |            |        | PASS          |
| templates/404.html                                                      | HTML      | PASS |      |            |        | PASS          |
| templates/500.html                                                      | HTML      | PASS |      |            |        | PASS          |
| templates/about.html                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/accessibility\_statement.html                                 | HTML      | PASS |      |            |        | PASS          |
| templates/add\_post.html                                                | HTML      | PASS |      |            |        | PASS          |
| templates/base.html                                                     | HTML      | PASS |      |            |        | PASS          |
| templates/categories.html                                               | HTML      | PASS |      |            |        | PASS          |
| templates/change-password.html                                          | HTML      | PASS |      |            |        | PASS          |
| templates/contact.html                                                  | HTML      | PASS |      |            |        | PASS          |
| templates/copyright\_statement.html                                     | HTML      | PASS |      |            |        | PASS          |
| templates/delete\_post.html                                             | HTML      | PASS |      |            |        | PASS          |
| templates/edit\_profile.html                                            | HTML      | PASS |      |            |        | PASS          |
| [https://fresh-casts.herokuapp.com](https://fresh-casts.herokuapp.com/) | HTML      | PASS |      |            |        | PASS          |
| templates/post\_detail.html                                             | HTML      | EXC  |      |            |        | PASS          |
| templates/sign\_up.html                                                 | HTML      | PASS |      |            |        | PASS          |
| templates/update\_post.html                                             | HTML      | PASS |      |            |        | PASS          |
| templates/user\_agreement.html                                          | HTML      | PASS |      |            |        | PASS          |

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

