from flask import Flask, request, json, render_template,url_for

app = Flask(__name__)
with app.open_resource('data/books.json') as book_file:
  data = json.load(book_file)
  global book_list
  book_list = data['books']

def getlist(sort):
  list=[]
  for elem in book_list:
    for k,v in elem.iteritems():
      if k == sort:
        if v not in list:
          list.append(v)
          list.sort()
  return list

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
 # global d
  return render_template("main.html")

@app.route('/title')
def titles():
  sort='title'
  list=getlist(sort)
  return render_template("titles.html",list=list)

@app.route('/title/<title>')
def title(title):
   return render_template("book.html",list=book_list,title=title)

@app.route('/author')
def author():
  sort= 'author'
  list=getlist(sort)
  return render_template("author.html",list=list)

@app.route('/author/<spauthor>')
def spauthor(spauthor):
  sort = spauthor
  list=getsplist(sort)
  return render_template("spauthor.html",author=spauthor,list=list)
@app.route('/publisher')
def publisher():
  sort = 'publisher'
  list = getlist(sort)
  return render_template("publishers.html",list=list)


@app.route('/publisher/<sppub>')
def sppub(sppub):
  sort = sppub
  list = getsplist(sort)
  return render_template("sppub.html",sppub=sppub,list=list)

@app.route('/genre')
def genre():
  sort = 'genre'
  list = getlist(sort)
  return render_template("genres.html", list=list)

@app.route('/genre/<spgenre>')
def spgenre(spgenre):
  sort=spgenre
  list=getsplist(sort)
  return render_template("spgenre.html",spgenre=spgenre,list=list)

@app.route('/year')
def year():
  sort='published'
  list=getlist(sort)
  return render_template("year.html",list=list)

@app.route('/year/<spyear>')
def spyear(spyear):
  sort=spyear
  list=getsplist(sort)
  return render_template("spyear.html",spyear=spyear,list=list)




if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)
