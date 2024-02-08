from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Startup Landing Page</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#team">Team</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="hero">
        <div class="hero-content">
            <h1>Welcome to our AI Startup</h1>
            <p>Revolutionizing the future with artificial intelligence</p>
            <a href="#contact" class="btn">Get Started</a>
        </div>
    </section>

    <section id="about">
        <div class="container">
            <h2>About Us</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut convallis est. Proin auctor ante a semper placerat. Nullam vulputate, nisi et rutrum ultrices, sem augue fringilla ante, non aliquam metus orci quis tellus. Integer id semper felis. Nunc ut orci quis est iaculis finibus. Nullam nec erat id elit sodales semper. Nullam dignissim, sem ac facilisis cursus, tellus orci gravida risus, id dictum risus odio eget velit.</p>
        </div>
    </section>

    <section id="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service">
                <h3>Machine Learning</h3>
                <p>Utilizing machine learning algorithms to analyze and predict patterns in data.</p>
            </div>
            <div class="service">
                <h3>Natural Language Processing</h3>
                <p>Developing AI systems that can understand and interpret human language.</p>
            </div>
            <div class="service">
                <h3>Computer Vision</h3>
                <p>Creating AI models that can analyze and interpret visual data.</p>
            </div>
        </div>
    </section>

    <section id="team">
        <div class="container">
            <h2>Our Team</h2>
            <div class="member">
                <img src="team_member1.jpg" alt="Team Member 1">
                <h3>John Doe</h3>
                <p>Machine Learning Expert</p>
            </div>
            <div class="member">
                <img src="team_member2.jpg" alt="Team Member 2">
                <h3>Jane Smith</h3>
                <p>Natural Language Processing Specialist</p>
            </div>
            <div class="member">
                <img src="team_member3.jpg" alt="Team Member 3">
                <h3>David Johnson</h3>
                <p>Computer Vision Engineer</p>
            </div>
        </div>
    </section>

    <section id="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <form>
                <label for="name">Name</label>
                <input type="text" id="name" name="name" placeholder="Your name..">

                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Your email..">

                <label for="message">Message</label>
                <textarea id="message" name="message" placeholder="Write something.." style="height:200px"></textarea>

                <input type="submit" value="Submit">
            </form>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 AI Startup. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.get("/items/")
async def get_items():
  return {"greeting": "Hello"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    message = await websocket.receive_text()
    await websocket.send_text(f"Message text was: {message}")