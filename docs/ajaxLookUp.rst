Continue with React
===================

05:26:27 54. Ajax lookup via XHR in React.js
--------------------------------------------

https://github.com/Otinanai1309/tweetmetoo/commit/3674ee794d22a9ca20a3167513ef40ddaa20daa3


05:32:18 55. Handling CORS and Invalid HOST_HEADER in Django
------------------------------------------------------------

In order to make React render correctly our posts i have to do some changes.

.. code-block:: console
    :emphasize-lines: 1

    $ pip install django-cors-header
    Collecting django-cors-headers
    Downloading django_cors_headers-3.13.0-py3-none-any.whl (13 kB)
    c:\mydjangorestfullreactapps\twitterlikeapp2\venv\lib\site-packages (from Django>=3.2->django-cors-headers) (0.4.2)
    Installing collected packages: django-cors-headers
    Successfully installed django-cors-headers-3.13.0

I follow instuctions from https://pypi.org/project/django-cors-headers/
and i make a few changes mainly to the settings.py

https://github.com/Otinanai1309/tweetmetoo/commit/b87698facaadaed63520e33b62af7d357ad347ae


05:35:35 56. Functional Components in React
-------------------------------------------

https://github.com/Otinanai1309/tweetmetoo/commit/5a14e97d360e3c87ea7f3f796e8fcca7517b6fdb



05:42:52 57. React.js Action Btn
--------------------------------

https://github.com/Otinanai1309/tweetmetoo/commit/5ad22bc507457f9ef57aa71373c2f4cd1923885f


05:47:07 58. Using JavaScript Modules
-------------------------------------


https://github.com/Otinanai1309/tweetmetoo/commit/5acde55d31379e42599598668aacf09657f83229


05:53:00 59. Improved Action Btn
--------------------------------

https://github.com/Otinanai1309/tweetmetoo/commit/a80cdc64640ece6832c2a8c344a70fb205de5318


05:57:31 60. Understanding setState Hook
----------------------------------------

https://github.com/Otinanai1309/tweetmetoo/commit/304c9008b3b06f8054123b81feca3460fccefc05


06:03:02 61. Handling a Form in React
-------------------------------------

https://github.com/Otinanai1309/tweetmetoo/commit/43a2c140336967dc2480b335796dc94c161d6e7f


6:08:55 62. Pass from Parent Component to Child with useEffect
--------------------------------------------------------------

There is an error the React part doesn't work but i will continue anyway.

https://github.com/Otinanai1309/tweetmetoo/commit/52aa01dd17a5ed5cc759fb0d9fd64e5d1daded37


06:19:10 63. Adjust the React Render Process
--------------------------------------------

create a React production build by running 

.. code-block:: console
    :emphasize-lines: 1

    $ npm run build
    > tweetme2-web@0.1.0 build
    > react-scripts build

    Creating an optimized production build...
    Compiled successfully.

    File sizes after gzip:

    46.76 kB  build\static\js\main.587b742f.js
    541 B     build\static\css\main.073c9b0a.css
    You can control this with the homepage field in your package.json.

    The build folder is ready to be deployed.
    You may serve it with a static server:

    npm install -g serve
    serve -s build


https://github.com/Otinanai1309/tweetmetoo/commit/1f531ce366ee6103dc44502b708d3a8a74aed04b


06:23:07 64. React Rendered by Django
-------------------------------------

I add few lines in settings.py about statifiles_dir and static_root
and then i create the folders under twitterlikeapp2 (main app folder)

Right after i copy all the contents from the Reacts folder
build/static within the newly created static folder.

Then in my projects folder i run 

.. code-block:: console
    :emphasize-lines: 1

    $ .\manage.py collectstatic
    167 static files copied to 'C:\MyDjangoRestfullReactApps\TwitterLikeApp2\static-root'.

https://github.com/Otinanai1309/tweetmetoo/commit/5665549b7c9034428d0e0ccffc93e41e358af893


06:30:22 65. Render React App via Any Django Template
-----------------------------------------------------

https://github.com/Otinanai1309/tweetmetoo/commit/3bade35b4f3bfe1515692807b48f87e140d2da5d



06:38:36 66. A Better XHR Lookup
--------------------------------


