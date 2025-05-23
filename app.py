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

<!-- Open Graph / Facebook -->
<meta property="og:title" content="{{ title }}">
<meta property="og:description" content="Explore Muhammad Faizan's skills and projects in AI, data science, and machine learning.">
<meta property="og:type" content="website">
<meta property="og:image" content="/profile/myphoto.jpg">
<meta property="og:url" content="https://yourdomain.com/">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ title }}">
<meta name="twitter:description" content="Explore Muhammad Faizan's skills and projects in AI, data science, and machine learning.">
<meta name="twitter:image" content="/profile/myphoto.jpg">

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
.container{max-width:900px;margin:40px auto;padding:20px;}
h1{font-size:42px;color:var(--white);margin-bottom:15px;}
h2{color:var(--white);margin-bottom:15px;}
.progress{background:#888;border-radius:25px;overflow:hidden;height:20px;margin:10px 0;}
.progress-bar{height:100%;background:var(--accent);text-align:right;padding-right:8px;
             line-height:20px;color:var(--white);font-size:12px;}
.card{background:var(--dark-blue);padding:20px;border-radius:10px;margin-bottom:25px;
      box-shadow:0 0 10px rgba(0,0,0,0.3);}
.card img{max-width:100%;border-radius:8px;margin-bottom:15px;}
.cert-container{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;}
.cert{width:47%;background:var(--dark-blue);padding:15px;border-radius:10px;
      box-shadow:0 0 8px rgba(0,0,0,0.3);}
.cert img{width:100%;border:2px solid var(--accent);border-radius:8px;}
.cert p{margin-top:8px;font-size:14px;}
.timeline{position:relative;}
.entry-box{background:var(--dark-blue);padding:15px 20px;border-radius:15px;
           margin-bottom:20px;box-shadow:0 0 10px rgba(0,0,0,0.3);}
.entry-box h3{margin-bottom:8px;}
.contact-box{background:var(--dark-blue);padding:10px 15px;margin-bottom:10px;
             border-radius:12px;box-shadow:0 0 5px rgba(0,0,0,0.2);}
.contact-box a{color:var(--white);text-decoration:none;}
img.profile{width:160px;height:220px;object-fit:cover;border-radius:10px;
            box-shadow:0 0 10px rgba(0,0,0,0.5);margin-bottom:10px;}
.center{text-align:center;}
.project-thumbs{display:flex;gap:20px;flex-wrap:wrap;margin-bottom:10px;}
.project-thumbs img{width:50%;border-radius:8px;border:2px solid var(--accent);}
.home-description{background:var(--dark-blue);padding:15px;border-radius:12px;
                  box-shadow:0 0 8px rgba(0,0,0,0.3);margin-top:20px;}
@media (max-width:600px){
  nav{flex-direction:column;gap:10px;padding:10px;}
  .container{padding:15px;margin:20px;}
  h1{font-size:32px;}
  img.profile{width:120px;height:160px;}
  .project-thumbs img{width:100%;}
  .cert{width:100%;}
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

@app.route('/projects/<path:filepath>')
def project_files(filepath):
    return send_from_directory('projects', filepath)

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
    body = f'''
    <h2>Skills</h2>
    <div class="card">{bars}</div>
    '''
    return render_page('Skills | Muhammad Faizan', 'skills', body)

@app.route('/projects')
def projects():
    # Project 1 data
    folder_url1 = 'DataProfiler%20Project'
    images1 = ''.join(
        f'<img src="/projects/{folder_url1}/step{i}.jpg" alt="Step {i}">' 
        for i in range(1, 4)
    )
    project1 = f'''
    <div class="card">
        <h3>Project 1: DataProfiler Web App</h3>
        <div class="project-thumbs">{images1}</div>
        <p>A simple Flask-based web application that lets users upload CSV files, generate automated data-profiling
           reports, visualize insights, apply cleaning options, and download the refined dataset.</p>
        <p><a href="https://github.com/faizankhan1428/DataProfiler" target="_blank">View on GitHub</a></p>
    </div>
    '''

    # Project 2 data
    folder_url2 = 'Profile%20card%20generator%20project'
    images2 = ''.join(
        f'<img src="/projects/{folder_url2}/step{i}.jpg" alt="Profile Card Step {i}">' 
        for i in range(1, 3)
    )
    project2 = f'''
    <div class="card">
        <h3>Project 2: Profile Card Generator</h3>
        <div class="project-thumbs">{images2}</div>
        <p>A lightweight Flask tool that transforms basic user info and an uploaded photo into a polished profile card.
           It dynamically blends chosen colors, fonts, and layouts, then exports the finished card as a high-quality PNG
           ready for portfolios, resumes, or social media.</p>
        <p><a href="https://github.com/faizankhan1428/profile-card-generator" target="_blank">View on GitHub</a></p>
    </div>
    '''

    body = f'<h2>Projects</h2>{project1}{project2}'
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
        ('certificate7.png', 'Deep Learning (SkillUp by Simplilearn)')
    ]
    cert_html = ''.join(
        f'<div class="cert">'
        f'  <img src="/certificates/{file}" alt="{desc}">'
        f'  <p>{desc}</p>'
        f'</div>'
        for file, desc in certs
    )
    body = f'<h2>Certificates</h2><div class="cert-container">{cert_html}</div>'
    return render_page('Certificates | Muhammad Faizan', 'certificates', body)

@app.route('/experience')
def experience():
    experiences = [
        ("Auto Tech", "Team Lead / Data Entry / Report Maker", "2024 – Present, 1 yr",
         "Leading a team, managing data pipelines and compiling analytical reports."),
        ("American Web Express", "Sales Executive & Team Leader", "2023 – 2024, 1 yr",
         "Drove sales strategy and coached agents on customer-focused communication."),
        ("Innovative Tech", "Senior Supervisor / Data Entry", "2021 – 2023, 2.5 yrs",
         "Oversaw operations, ensured data integrity and mentored junior staff."),
        ("Tricore Marketing Solution (TMS Holdings)", "Call-Center Agent / Data Entry", "2019 – 2021, 1.5 yrs",
         "Handled outbound calls and maintained accurate records of customer interactions.")
    ]
    boxes = ''.join(
        f'<div class="entry-box">'
        f'  <h3>{org} — {role} <small>({duration})</small></h3>'
        f'  <p>{desc}</p>'
        f'</div>'
        for org, role, duration, desc in experiences
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
