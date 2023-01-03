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

To perform the test I used a Chrome browser, and validated each page from a mobile and desktop perspective.

<br>



<br>


## Responsiveness

To test the websites layout and content remains well structured and accessible across differing screen sizes, I used Chrome's Developer Tools to virtualise how the website and all its pages look and feel. In consideration that I opted to use Bootstrap which provides standard media queries for screen sizes from XS through to XL, I selected the following screens to test on; iPhone 4, iPhone SE, Samsung Galaxy S8, iPad, iPad Pro, Laptop at 1366x768, Monitor at 1920x1080 and iMac 5K.

Testing identified one fail when testing on an iPhone where the post text was located under the image and not to the right as per the category view. Furthermore some of the posts started slightly off the screen to the left. Resolution was to compare the homepage with the category view and remove unnecessary padding from the cards, whilst maintaining an min-width image size when required at +992px screen width.

<br> 

| File path                                                               | Mobile | Tablet | Desktop |
| ----------------------------------------------------------------------- | ------ | ------ | ------- |
| templates/account/login.html                                            | PASS   | PASS   | PASS    |
| templates/account/logout.html                                           | PASS   | PASS   | PASS    |
| templates/404.html                                                      | PASS   | PASS   | PASS    |
| templates/500.html                                                      | PASS   | PASS   | PASS    |
| templates/about.html                                                    | PASS   | PASS   | PASS    |
| templates/accessibility_statement.html                                  | PASS   | PASS   | PASS    |
| templates/add_post.html                                                 | PASS   | PASS   | PASS    |
| templates/categories.html                                               | PASS   | PASS   | PASS    |
| templates/change-password.html                                          | PASS   | PASS   | PASS    |
| templates/contact.html                                                  | PASS   | PASS   | PASS    |
| templates/copyright_statement.html                                      | PASS   | PASS   | PASS    |
| templates/delete_post.html                                              | PASS   | PASS   | PASS    |
| templates/edit_profile.html                                             | PASS   | PASS   | PASS    |
| [https://fresh-casts.herokuapp.com](https://fresh-casts.herokuapp.com/) | FAIL   | PASS   | PASS    |
| templates/post_detail.html                                              | PASS   | PASS   | PASS    |
| templates/sign_up.html                                                  | PASS   | PASS   | PASS    |
| templates/update_post.html                                              | PASS   | PASS   | PASS    |
| templates/user_agreement.html                                           | PASS   | PASS   | PASS    |

<br>


## Accessibility 

Key to any successful website is ensuring its accessibility. As well as using Chrome's Developer Tools to test each html page, I also used the [WAVE online assessment tool](https://wave.webaim.org/) as I feel this provides a deeper level of insight and is clearer in highlighting where improvements are required.
To achieve a pass, each page had to have 0 Errors and 0 Contrast Errors from WAVE, or +90% from Chrome's Developer Tools.

Summary of the results;
* When using WAVE, it was not possible to run a test on the pages where authentication was required; add_post.html, delete_post.html, edit_profile.html and update_post.html. In this scenario Chrome's Developer Tools helped in providing the assessment.
* The test highlight multiple links to the same page. This was prevalent on the homepage where there was a link to categories in the navbar drop-down menu, and another within the post details in the homepage page list view. To improve the experience for users with screen readers I opted to remove the category name and link from each post, and instead allow users to navigate using the navbar menu only.

<br>

| File path                                                               | Result |
| ----------------------------------------------------------------------- | --------- |
| templates/account/login.html                                            | PASS      |
| templates/account/logout.html                                           | PASS      |
| templates/404.html                                                      | PASS      |
| templates/500.html                                                      | PASS      |
| templates/about.html                                                    | PASS      |
| templates/accessibility\_statement.html                                 | PASS      |
| templates/add\_post.html                                                | NP        |
| templates/categories.html                                               | PASS      |
| templates/change-password.html                                          | PASS      |
| templates/contact.html                                                  | PASS      |
| templates/copyright\_statement.html                                     | PASS      |
| templates/delete\_post.html                                             | NP        |
| templates/edit\_profile.html                                            | NP        |
| [https://fresh-casts.herokuapp.com](https://fresh-casts.herokuapp.com/) | PASS      |
| templates/post\_detail.html                                             | PASS      |
| templates/sign\_up.html                                                 | PASS      |
| templates/update\_post.html                                             | NP        |
| templates/user\_agreement.html                                          | PASS      |

<br>

 
## Performance

All pages were tested using Chrome's developer tool 'Lighthouse Testing'. At a high-level the tool tests performance in terms of loading speed, best-practice in regards to layout, SEO for how searchable the website and how accessible it is for visually impaired users who may also require a screen reader. Despite trying I could not test the 404 and 500 error pages and so they have been discounted from the results below.

To try and achieve clear and consistent results I used an incognito version of Chrome. 

The website scored well across all criteria, however further work was required to;
- improve the contrast of the background to foreground for Accessibility,
- ensure there was sufficient spacing between Footer links for mobile users,
- transform all future images uploaded to webP format and 300x300px in size to improve page loading times.

Research is required to improve an average Best Practices score of 83. The issue raised relates to the use of front-end JavaScript libraries with known security vulnerabilities. Three medium severity counts have been identified against the use of JQuery version 3.3.1 from Jan 2018. A fix is likely to be upgrading to a newer version of the library where a fix has been applied. However I need to ensure a newer version will be compatible with the version of Bootstrap I've implemented.

																	
The results below show mobile in the first 4 columns and desktop in the second 4 columns.

<br>

| File path                                                               | Performance | Accessibility | Best Practice | SEO | Performance | Accessibility | Best Practice | SEO |
| ----------------------------------------------------------------------- | ----------- | ------------- | ------------- | --- | ----------- | ------------- | ------------- | --- |
| templates/account/login.html                                            | 96          | 100           | 83            | 92  | 100         | 100           | 83            | 90  |
| templates/account/logout.html                                           | 91          | 100           | 83            | 92  | 100         | 100           | 83            | 90  |
| templates/about.html                                                    | 93          | 100           | 83            | 92  | 98          | 100           | 83            | 90  |
| templates/accessibility\_statement.html                                 | 96          | 100           | 83            | 92  | 99          | 100           | 83            | 90  |
| templates/add\_post.html                                                | 53          | 100           | 83            | 92  | 98          | 100           | 83            | 90  |
| templates/categories.html                                               | 77          | 100           | 83            | 92  | 98          | 100           | 83            | 90  |
| templates/change-password.html                                          | 92          | 100           | 83            | 92  | 99          | 100           | 83            | 90  |
| templates/contact.html                                                  | 85          | 100           | 83            | 92  | 99          | 100           | 83            | 90  |
| templates/copyright\_statement.html                                     | 96          | 100           | 83            | 92  | 98          | 100           | 83            | 90  |
| templates/delete\_post.html                                             | 83          | 100           | 83            | 92  | 100         | 100           | 83            | 90  |
| templates/edit\_profile.html                                            | 94          | 97            | 83            | 92  | 99          | 97            | 83            | 90  |
| [https://fresh-casts.herokuapp.com](https://fresh-casts.herokuapp.com/) | 72          | 100           | 83            | 92  | 96          | 100           | 83            | 90  |
| templates/post\_detail.html                                             | 75          | 100           | 83            | 92  | 99          | 93            | 83            | 90  |
| templates/sign\_up.html                                                 | 89          | 100           | 83            | 92  | 98          | 100           | 83            | 90  |
| templates/update\_post.html                                             | 92          | 97            | 83            | 92  | 91          | 97            | 83            | 90  |
| templates/user\_agreement.html                                          | 96          | 100           | 83            | 92  | 98          | 100           | 83            | 90  |

<br>


## Browser

Performing cross browser testing is key to ensuring a positive user experience no matter which browser users prefer to use. To perform a thorough test, I used Firefox, Chrome and Edge on my local machine, which uses Windows 10 as the operating system. To gain further coverage I used Lambda Testing, a browser test tool that virtualises browsers, devices and screen sizes. Here I could test the site on Safari and Opera. IE11 or previous versions were not tested at this time as Microsoft has ceased supporting this browser as they look to embed Edge.

Reassuringly the tests proved the website loads on all 5 browser types. All elements such as buttons, forms, menus and images loaded and were functional where required. Despite getting some poor lighthouse performance results for the website loading on mobile devices, I didn't experience this in reality from either browser or device testing.

<br>

| File path                                                               | Chrome (v107) | Firefox (v107 win 10) | Edge (v104 Win 10) | Safari (v15 macOS Monterey) | Opera (v89 macOS Monterey) |
| ----------------------------------------------------------------------- | ------------- | --------------------- | ------------------ | --------------------------- | -------------------------- |
| templates/account/login.html                                            | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/account/logout.html                                           | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/about.html                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/accessibility\_statement.html                                 | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/add\_post.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/categories.html                                               | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/change-password.html                                          | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/contact.html                                                  | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/copyright\_statement.html                                     | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/delete\_post.html                                             | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/edit\_profile.html                                            | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| [https://fresh-casts.herokuapp.com](https://fresh-casts.herokuapp.com/) | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/post\_detail.html                                             | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/sign\_up.html                                                 | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/update\_post.html                                             | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/user\_agreement.html                                          | PASS          | PASS                  | PASS               | PASS                        | PASS                       |

<br>


## Device

Similar to the aims of browser testing, I wanted to tests users experience of the website across conventional devices. For this I used an iPhone SE, iPad, Laptop, 27" Monitor and lastly a virtual environment for a mobile phone using an Android operating system.

The only major issue identified was on mobile and tablet devices where as a user I assumed I could click on any part of a posts summary card to reveal further information. However on the homepage and categories view I could only click on the image or post title. To improve the user experience by aligning with convention on blog/news feed sites, I updated the code to ensure all the card was clickable and also changed the user feedback from a coloured hyperlink style flash under text, to a flash of colour from the whole card. As a result of this issue, a Fail was recorded against the relating pages, however this has been fixed.

<br>

| File path                                                               | Mobile (iOS) | Mobile (Android) | Tablet | Desktop |
| ----------------------------------------------------------------------- | ------------ | ---------------- | ------ | ------- |
| templates/account/login.html                                            | PASS         | PASS             | PASS   | PASS    |
| templates/account/logout.html                                           | PASS         | PASS             | PASS   | PASS    |
| templates/404.html                                                      | PASS         | PASS             | PASS   | PASS    |
| templates/500.html                                                      | PASS         | PASS             | PASS   | PASS    |
| templates/about.html                                                    | PASS         | PASS             | PASS   | PASS    |
| templates/accessibility\_statement.html                                 | PASS         | PASS             | PASS   | PASS    |
| templates/add\_post.html                                                | PASS         | PASS             | PASS   | PASS    |
| templates/categories.html                                               | FAIL         | FAIL             | FAIL   | PASS    |
| templates/change-password.html                                          | PASS         | PASS             | PASS   | PASS    |
| templates/contact.html                                                  | PASS         | PASS             | PASS   | PASS    |
| templates/copyright\_statement.html                                     | PASS         | PASS             | PASS   | PASS    |
| templates/delete\_post.html                                             | PASS         | PASS             | PASS   | PASS    |
| templates/edit\_profile.html                                            | PASS         | PASS             | PASS   | PASS    |
| [https://fresh-casts.herokuapp.com](https://fresh-casts.herokuapp.com/) | FAIL         | FAIL             | FAIL   | PASS    |
| templates/post\_detail.html                                             | PASS         | PASS             | PASS   | PASS    |
| templates/sign\_up.html                                                 | PASS         | PASS             | PASS   | PASS    |
| templates/update\_post.html                                             | PASS         | PASS             | PASS   | PASS    |
| templates/user\_agreement.html                                          | PASS         | PASS             | PASS   | PASS    |

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

Whilst further testing is required to achieve 100% coverage, the results so far are highlighted in the summary report below:

<p align="center">
    <img src="readme-images/fresh-casts-blog-app-automated-testing.png" alt="Django automatic testing results"/>
    </p>

<br>


## Bugs

