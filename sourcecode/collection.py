from flask import Flask, request, json, render_template,url_for

app = Flask(__name__)
with app.open_resource('data/books.json') as book_file:
  data = json.load(book_file)
  global book_list
  book_list = data['books']
@app.route('/',methods=['GET','POST'])
def index():
 # global d
  return render_template("main.html")

@app.route('/title')
def titles():
  tlist=[]
  for elem in book_list:
    for k,v in elem.iteritems():
      if k == 'title':
        tlist.append(v)
        tlist.sort()
  return render_template("titles.html",list=tlist)

@app.route('/title/<title>')
def title(title):
   return render_template("book.html",list=book_list,title=title)

@app.route('/author')
def author():
  global alist 
  alist =[]
  for elem in book_list:
    for k,v in elem.iteritems():
      if k == 'author':
        if v not in alist:
          alist.append(v)
          alist.sort()
  return render_template("author.html",list=alist)

@app.route('/author/<spauthor>')
def spauthor(spauthor):
  return render_template("spauthor.html",author=spauthor,list=book_list,alist=alist)

@app.route('/publisher')
def publisher():
  global plist
  plist = []
  for elem in book_list:
    for k,v in elem.iteritems():
      if k == 'publisher':
        if v not in plist:
          plist.append(v)
          plist.sort()
  return render_template("publishers.html",list=plist)


@app.route('/publisher/<sppub>')
def sppub(sppub):
  return render_template("sppub.html",sppub=sppub,list=book_list,plist=plist)

@app.route('/genre')
def genre():
  glist = []
  for elem in book_list:
    for k,v in elem.iteritems():
      if k =='genre':
        if v not in glist:
          glist.append(v)
          glist.sort()
  return render_template("genres.html", list=glist)

@app.route('/genre/<spgenre>')
def spgenre(spgenre):
  return render_template("spgenre.html",spgenre=spgenre,list=book_list)

@app.route('/year')
def year():
  ylist=[]
  for elem in book_list:
    for k,v in elem.iteritems():
      if k =='published':
        if v not in ylist:
          ylist.append(v)
          ylist.sort()
  return render_template("year.html",list=ylist)

@app.route('/year/<spyear>')
def spyear(spyear):
  return render_template("spyear.html",spyear=spyear,list=book_list)




if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)
