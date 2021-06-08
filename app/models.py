class Source : 
    def __init__(self,id,name,description,language, urlToImage):
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.urlToImage = urlToImage
    
class Article :
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        