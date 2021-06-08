from flask import render_template
from app import app
from ..request import get_article, get_sources

#views
@app.route("/")
def index():
    """View root page function that returns the index page and its data"""


    news = get_sources()
    title = 'News - Get yourself newsed up'
    return render_template("index.html",title = title ,news=news)


@app.route("/news/<id>")
def article(id):
    """View article page that returns articles and their data"""
    article = get_article(id)
    #title = f"{article.title}"

    return render_template("articles.html",article=article, )

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourowfour.html'),404


