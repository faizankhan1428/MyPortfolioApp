from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# ── base HTML template ────────────────────────────────────────────────────────
BASE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">
<meta name="description" content="Muhammad Faizan's portfolio showcasing AI, data science, and ML projects.">
<meta name="keywords" content="AI Engineer, Data Scientist, ML Developer, Muhammad Faizan, Portfolio">
<meta name="author" content="Muhammad Faizan">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#1B263B">
<title>{{ title }}</title>

<link rel="icon" type="image/png" href="/profile/myphoto.jpg">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<style>
:root{
  --dark-blue:#0D1B2A;
  --light-blue:#1B263B;
  --accent:#415A77;
  --white:#FFFFFF;
}
*{box-sizing:border-box;margin:0;padding:0;font-family:'Poppins',sans-serif;}
body{background:var(--light-blue);color:var(--white);}
nav{background:var(--dark-blue);padding:15px 30px;display:flex;gap:20px;flex-wrap:wrap;}
nav a{color:var(--white);text-decoration:none;font-weight:400;}
nav a.active,nav a:hover{color:var(--accent);font-weight:600;}
.container{max-width:1000px;margin:40px auto;padding:20px;}
h1{font-size:42px;margin-bottom:15px;}
h2{margin-bottom:15px;}
.progress{background:#888;border-radius:25px;overflow:hidden;height:16px;margin:10px 0;}
.progress-bar{height:100%;background:var(--accent);text-align:right;padding-right:8px;
             line-height:16px;color:var(--white);font-size:12px;}
.card{background:var(--dark-blue);padding:15px;border-radius:10px;margin-bottom:25px;
      box-shadow:0 0 10px rgba(0,0,0,0.3);}
.cert-container{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;}
.cert{width:30%;background:var(--dark-blue);padding:15px;border-radius:10px;
      box-shadow:0 0 8px rgba(0,0,0,0.3);}
.cert img{width:100%;border:2px solid var(--accent);border-radius:8px;}
.cert p{margin-top:8px;font-size:14px;}
.entry-box{background:var(--dark-blue);padding:15px 20px;border-radius:15px;
           margin-bottom:20px;box-shadow:0 0 10px rgba(0,0,0,0.3);}
.contact-box{background:var(--dark-blue);padding:10px 15px;margin-bottom:10px;
             border-radius:12px;box-shadow:0 0 5px rgba(0,0,0,0.2);}
.contact-box a{color:var(--white);text-decoration:none;}
img.profile{width:160px;height:220px;object-fit:cover;border-radius:10px;
            box-shadow:0 0 10px rgba(0,0,0,0.5);margin-bottom:10px;}
.center{text-align:center;}
.project-grid{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;}
.project-card{width:30%;background:var(--dark-blue);padding:15px;border-radius:10px;
              box-shadow:0 0 8px rgba(0,0,0,0.3);}
.project-card img{width:100%;border-radius:8px;border:2px solid var(--accent);}
.project-card p{margin:10px 0;font-size:14px;}
.project-card a{color:var(--accent);font-size:14px;text-decoration:none;}
.home-description{background:var(--dark-blue);padding:15px;border-radius:12px;
                  box-shadow:0 0 8px rgba(0,0,0,0.3);margin-top:20px;}
@media (max-width:900px){
  .project-card, .cert{width:47%;}
}
@media (max-width:600px){
  nav{flex-direction:column;gap:10px;padding:10px;}
  .container{padding:15px;margin:20px;}
  h1{font-size:32px;}
  img.profile{width:120px;height:160px;}
  .project-card, .cert{width:100%;}
  .cert-container{flex-direction:column;}
}
</style>
</head>
<body>
<nav>
  <a href="/"           class="{{ 'active' if active=='home'        else '' }}">Home</a>
  <a href="/skills"     class="{{ 'active' if active=='skills'      else '' }}">Skills</a>
  <a href="/projects"   class="{{ 'active' if active=='projects'    else '' }}">Projects</a>
  <a href="/certificates" class="{{ 'active' if active=='certificates' else '' }}">Certificates</a>
  <a href="/experience" class="{{ 'active' if active=='experience'  else '' }}">Experience</a>
  <a href="/contact"    class="{{ 'active' if active=='contact'     else '' }}">Contact</a>
</nav>
<div class="container">
{{ body|safe }}
</div>
</body>
</html>
'''

def render_page(title, active, body_html):
    return render_template_string(BASE_TEMPLATE, title=title, active=active, body=body_html)

@app.route('/profile/<path:filename>')
def profile_file(filename):
    return send_from_directory('profile', filename)

@app.route('/projects/<path:filename>')
def project_files(filename):
    return send_from_directory('projects', filename)

@app.route('/certificates/<path:filename>')
def certificate_files(filename):
    return send_from_directory('certificates', filename)

@app.route('/')
def home():
    body = '''
    <div class="center">
        <img src="/profile/myphoto.jpg" alt="Muhammad Faizan" class="profile">
        <h1 style="font-size:50px;">MUHAMMAD FAIZAN</h1>
        <div class="home-description">
            <h2>AI Engineer | Data Scientist | ML Developer</h2>
            <p>Aspiring AI Engineer, passionate about data, intelligent models, and autonomous AI agents.<br>
               Skilled in Python, exploring the future of AI through real-world projects and experiments.</p>
        </div>
    </div>
    '''
    return render_page('Muhammad Faizan | Home', 'home', body)

@app.route('/skills')
def skills():
    skills_data = [
        ('Python', 95),
        ('Pandas / NumPy / Matplotlib', 90),
        ('Scikit-learn / TensorFlow / Keras', 85),
        ('Flask / Streamlit', 80),
        ('Git / GitHub', 85),
        ('Jupyter / VS Code / Google Colab', 90),
        ('SQL / Excel / Power BI', 75),
        ('Linux / Bash / CLI Tools', 70),
        ('Machine Learning / Deep Learning', 90),
        ('Data Wrangling / Cleaning', 88)
    ]
    bars = ''.join(
        f'<p>{name}</p><div class="progress">'
        f'<div class="progress-bar" style="width:{pct}%">{pct}%</div></div>'
        for name, pct in skills_data
    )
    body = f'<h2>Skills</h2><div class="card">{bars}</div>'
    return render_page('Skills | Muhammad Faizan', 'skills', body)

@app.route('/projects')
def projects():
    projects = [
        ("project1.jpg", "Ai Travel Planner",
         "A Flask-based web application that helps users plan personalized trips across Pakistan based on their budget, preferences, and travel goals.",
         "https://my-ai-travel-guide.vercel.app/"),

        ("project2.jpg", "CNN Cat vs Dog Classifier",
         "A complete CNN-based image classification project to identify cats and dogs using TensorFlow/Keras, including EDA, training, evaluation, and predictions.",
         "https://github.com/faizankhan1428/cats-vs-dogs-cnn"),

        ("project3.jpg", "Titanic Survival Prediction",
         "Beginner-friendly Titanic survival prediction using EDA, feature engineering, and Random Forest model. Built for Kaggle competition.",
         "https://github.com/faizankhan1428/titanic-survival-prediction"),

        ("project4.jpg", "Data Profiler",
         "A simple Flask-based web application that allows users to upload CSV files, view data profiling reports, generate visualizations, apply cleaning options, and download the cleaned data.",
         "https://data.profiler.vercel.app/"),

        ("project5.jpg", "PSL Cricket Analysis",
         "A machine learning model that predicts match winners based on team combinations.",
         "https://github.com/faizankhan1428/PSL")
    ]
    cards = ''.join(f'''
    <div class="project-card">
        <img src="/projects/{img}" alt="{title}">
        <h3>{title}</h3>
        <p>{desc}</p>
        <p><a href="{link}" target="_blank">View Project</a></p>
    </div>
    ''' for img, title, desc, link in projects)
    body = f'<h2>Projects</h2><div class="project-grid">{cards}</div>'
    return render_page('Projects | Muhammad Faizan', 'projects', body)

@app.route('/certificates')
def certificates():
    certs = [
        ('certificate1.png', 'Attended a virtual session on pursuing a career in UI/UX Design (Xounity)'),
        ('certificate2.png', 'Basics of Data Science (UniAthena)'),
        ('certificate3.png', 'Introduction to Artificial Intelligence (SkillUp by Simplilearn)'),
        ('certificate4.png', 'NLP and Text Mining (SkillUp by Simplilearn)'),
        ('certificate5.png', 'Virtual session: Unlocking Data Science (Xounity)'),
        ('certificate6.png', 'Basics of Machine-Learning Algorithms (UniAthena)'),
        ('certificate7.png', 'Deep Learning (SkillUp by Simplilearn)'),
        ('certificate8.png', 'Python Programming: Complete Course for Success (Udemy)'),
        ('certificate9.png', 'Python Course (Kaggle)')
    ]
    cert_html = ''.join(
        f'<div class="cert"><img src="/certificates/{file}" alt="{desc}"><p>{desc}</p></div>'
        for file, desc in certs
    )
    body = f'<h2>Certificates</h2><div class="cert-container">{cert_html}</div>'
    return render_page('Certificates | Muhammad Faizan', 'certificates', body)

@app.route('/experience')
def experience():
    experiences = [
        ("Sales Support Executive", "Tricore Marketing Solution, Karachi (1 Year)",
         "Called physicians to obtain fax numbers, processed prescriptions, and maintained accurate records in Excel."),

        ("Data Management Assistant", "Auto Tech, Karachi (1 Year)",
         "Supported internal operations by handling routine data tasks and report workflows."),

        ("AI Project Developer", "Innovative Tech, Karachi (6 Months)",
         "Led the development of AI-based projects tailored to client requirements received by the sales team.")
    ]
    boxes = ''.join(
        f'<div class="entry-box"><h3>{title}</h3><p><strong>{org}</strong><br>{desc}</p></div>'
        for title, org, desc in experiences
    )
    body = f'<h2>Work Experience</h2>{boxes}'
    return render_page('Experience | Muhammad Faizan', 'experience', body)

@app.route('/contact')
def contact():
    body = '''
    <h2>Contact</h2>
    <div class="card contact">
      <div class="contact-box">Email: <a href="mailto:faizankhandeshmukh28@gmail.com">faizankhandeshmukh28@gmail.com</a>,
                               <a href="mailto:faixankhandeshmukh@gmail.com">faixankhandeshmukh@gmail.com</a></div>
      <div class="contact-box">Phone: <a href="tel:+923358102371">0335 8102371</a>,
                                <a href="tel:+923323238391">0332 3238391</a></div>
      <div class="contact-box">Instagram: <a href="https://www.instagram.com/faixan__xx/" target="_blank">@faixan__xx</a></div>
      <div class="contact-box">GitHub: <a href="https://github.com/faizankhan1428" target="_blank">github.com/faizankhan1428</a></div>
      <div class="contact-box">LinkedIn: <a href="https://www.linkedin.com/in/muhammad-faizan-1335b0288/" target="_blank">
                                muhammad-faizan-1335b0288</a></div>
    </div>
    '''
    return render_page('Contact | Muhammad Faizan', 'contact', body)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
