from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/education")
def education():
    return render_template(
        "education.html",
        show_result=False
    )

@app.route("/action")
def action():
    return render_template("action.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/calculate", methods=["POST"])
def calculate():

    score = 0

    buying = request.form["buying"]
    old = request.form["old"]
    material = request.form["material"]
    shop = request.form["shop"]
    life = request.form["life"]


    # scoring
    if buying == "more_week":
        score += 50
    elif buying == "two_week":
        score += 40
    elif buying == "month":
        score += 25
    elif buying == "year":
        score += 10
    else:
        score += 5


    if old == "throw":
        score += 50
    elif old == "donate":
        score += 30
    elif old == "sell":
        score += 20
    else:
        score += 5


    if material == "polyester":
        score += 50
    elif material == "nylon":
        score += 45
    elif material == "denim":
        score += 25
    elif material == "cotton":
        score += 20
    else:
        score += 10


    if shop == "shein":
        score += 60
    elif shop == "fast":
        score += 45
    elif shop == "dept":
        score += 30
    else:
        score += 10


    if life == "short":
        score += 50
    elif life == "mid":
        score += 40
    elif life == "long":
        score += 25
    elif life == "longer":
        score += 15
    else:
        score += 5

 # RESULT CATEGORY
    if score <= 80:
        result = "Excellent: Very low impact"
        description = "Great job! Your clothing choices show many sustainable habits. You are already making choices that help reduce textile waste and environmental impact. Keep up these positive habits!"

    elif score <= 140:
        result = "Good: Low impact"
        description = "Nice work! Your clothing habits are already helping reduce your textile footprint. There are always small ways to improve, such as repairing clothes, shopping secondhand, or choosing pieces that last longer."

    elif score <= 200:
        result = "Average: Moderate impact"
        description = "Your textile footprint is around the average range. Small changes over time can make a meaningful difference, such as buying fewer unnecessary items, reusing clothing, or exploring more sustainable options."

    elif score <= 260:
        result = "High: Room for improvement"
        description = "Your results show there are opportunities to make your clothing habits more sustainable. Even small steps, like wearing clothes longer, donating responsibly, or choosing secondhand items, can help lower your impact."

    else:
        result = "Very High: Starting point for change"
        description = "Your results show there are many opportunities to reduce your textile footprint. Don't worry — sustainability is a journey, and even small changes can create a positive impact over time."


    return render_template(
        "education.html",
        score=score,
        result=result,
        description=description,
        show_result=True
    )

if __name__ == "__main__":
    app.run()