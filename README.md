# News_API

## Author

ANGELA MUTYOTA

# Description
News pount is an app that ensures people are able to get real time news everyday. The website will show news articles from several sources and news sources that a user can click to see more news. 


## User Story

1. A user should see various news sources on the homepage of the application.
2. A user can select a news source and see all news articles from the selected news source in the application.
3. A user will be able to see the image, description and the time a news article was created from the News-Articles tab.
4. A user can click on an article and read the full article on the source website.


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/Angelamutyota/news-API.git

2. Move to the folder and install requirements
  ```bash
  cd News_API
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export API_KEY='{Enter your News Api Key}'
  ```
4. Running the application
  ```bash
  python3.6 manage.py server
  ```
5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* Python3.6
* Flask
* Heroku


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug


## License
* *MIT License:*
* Copyright (c) 2021 **Angela Mbithe**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.