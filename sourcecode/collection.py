from flask import Flask, request, json, render_template,url_for

app = Flask(__name__)
#load collection from json
with app.open_resource('data/books.json') as book_file:
  data = json.load(book_file)
  global book_list
  book_list = data['books']
#method to get list of subcatagories, eg all the genres
def getlist(sort):
  list=[]
  for elem in book_list:
    for k,v in elem.iteritems():
      if k == sort:
        if v not in list:
          list.append(v)
          list.sort()
  return list
#method to get list of all books belonging to a subcatagory
def getsplist(sort):
  list=[]
  for elem in book_list:
    for k,v in elem.iteritems():
      if v == sort:
        list.append(elem['title'])
        list.sort()
  return list
@app.route('/',methods=['GET','POST'])
def index():
#get info from main page add book form and add to list--TBC
  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    publisher = request.form['publisher']
    year = request.form['published']
    book ={'title:'+title}
   # book_list.insert(len(book_list),'title:'+title)
  return render_template("main.html")

#page that shows a list of all items in the collection
@app.route('/title')
def titles():
  sort='title'
  list=getlist(sort)
  return render_template("titles.html",list=list,books=book_list,title="Title")
#page that shows info about specific item
@app.route('/title/<title>')
def title(title):
   return render_template("book.html",list=book_list,title=title)
#routes for navigation, page that displays list of sub catagories and then a
#page that shows all item in sub catagory
@app.route('/author')
def author():
  sort= 'author'
  list=getlist(sort)
  return render_template("author.html",list=list)

@app.route('/author/<spauthor>')
def spauthor(spauthor):
  sort = spauthor
  list=getsplist(sort)
  return render_template("titles.html",title=spauthor,list=list,books=book_list)
@app.route('/publisher')
def publisher():
  sort = 'publisher'
  list = getlist(sort)
  return render_template("publishers.html",list=list)


@app.route('/publisher/<sppub>')
def sppub(sppub):
  sort = sppub
  list = getsplist(sort)
  return render_template("titles.html",title=sppub,list=list,books=book_list)

@app.route('/genre')
def genre():
  sort = 'genre'
  list = getlist(sort)
  return render_template("genres.html", list=list)

@app.route('/genre/<spgenre>')
def spgenre(spgenre):
  sort=spgenre
  list=getsplist(sort)
  return render_template("titles.html",title=spgenre,list=list,books=book_list)

@app.route('/year')
def year():
  sort='published'
  list=getlist(sort)
  return render_template("year.html",list=list)

@app.route('/year/<spyear>')
def spyear(spyear):
  sort=spyear
  list=getsplist(sort)
  return render_template("titles.html",title=spyear,list=list,books=book_list)




if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)
