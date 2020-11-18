from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/facelook'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    ppic = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(80), unique=True, nullable=False)
    pimg = db.Column(db.String(120), unique=True, nullable=False)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    msg = db.Column(db.String(80), unique=True, nullable=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    ppic = db.Column(db.String(80), unique=True, nullable=False)
    about = db.Column(db.String(80), unique=True, nullable=False)

class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)


@app.route('/',methods=['POST','GET'])
def home():
    if(request.method=='POST'):
        name = request.form.get('name')
        msg = request.form.get('msg')
        mesg = Messages(name=name,msg=msg)
        db.session.add(mesg)
        db.session.commit()
    msgs = Messages.query.all()    
    posts = Post.query.filter_by().all()
    return render_template('home.html',posts=posts,msgs=msgs)

@app.route('/clear')
def clear():
    db.session.query(Messages).delete()
    db.session.commit()
    return redirect('/')

@app.route('/about',methods=['POST','GET'])
def about():
    if(request.method=='POST'):
        name = request.form.get('name')
        ppic = request.form.get('ppic')
        about = request.form.get('about')
        about = Profile(name=name,ppic=ppic,about=about)
        db.session.add(about)
        db.session.commit()
        redirect('/')
    return render_template('add-about.html')

@app.route('/profiles')
def profiles():
    profiles = Profile.query.filter_by().all()
    return render_template('profile.html',profiles=profiles)

@app.route('/Your-personality-according-to-your-name')
def gameone():
    return render_template('per.html')


@app.route('/Your-future-personality-in-present')
def gametwo():
    return render_template('gtwo.html')

@app.route('/videos',methods=['POST','GET'])
def videos():
    if(request.method=='POST'):
        name = request.form.get('name')
        video = request.form.get('video')
        vid = Videos(video=video,name=name)
        db.session.add(vid)
        db.session.commit()
    videos = Videos.query.filter_by().all()
    return render_template('video.html',videos=videos)


@app.route('/add',methods=['POST','GET'])
def add():
    if(request.method=='POST'):
        name = request.form.get('name')
        ppic = request.form.get('ppic')
        title = request.form.get('title')
        content = request.form.get('content')
        pimg = request.form.get('pimg')
        post = Post(name=name,ppic=ppic,title=title,content=content,pimg=pimg)
        db.session.add(post)
        db.session.commit()
        redirect('/')
    return render_template('index.html')

@app.route('/delete/<int:Post_id>')
def delete(Post_id):
    post = Post.query.filter_by(id=Post_id).one()
    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route('/profile-delete/<int:Profile_id>')
def profile_delete(Profile_id):
    profile = Profile.query.filter_by(id=Profile_id).one()
    db.session.delete(profile)
    db.session.commit()
    return redirect('/profiles')


@app.route('/video-delete/<int:Videos_id>')
def video_delete(Videos_id):
    video = Videos.query.filter_by(id=Videos_id).one()
    db.session.delete(video)
    db.session.commit()
    return redirect('/videos')


app.run(debug=True)