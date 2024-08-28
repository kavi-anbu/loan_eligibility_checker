from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        loan_type = request.form['loan_type']
        if loan_type == 'home':
            return redirect(url_for('home_loan'))
        elif loan_type == 'personal':
            return redirect(url_for('personal_loan'))
        elif loan_type == 'vehicle':
            return redirect(url_for('vehicle_loan'))
        elif loan_type == 'educational':
            return redirect(url_for('educational_loan'))
        elif loan_type == 'business':
            return redirect(url_for('business_loan'))
    return render_template('index.html')

# Route for the home loan page
@app.route('/home-loan', methods=['GET', 'POST'])
def home_loan():
    if request.method == 'POST':
        # Process home loan form data here
        pass
    return render_template('home_loan.html')

# Route for the personal loan page
@app.route('/personal-loan', methods=['GET', 'POST'])
def personal_loan():
    if request.method == 'POST':
        # Process personal loan form data here
        pass
    return render_template('personal_loan.html')

# Route for the vehicle loan page
@app.route('/vehicle-loan', methods=['GET', 'POST'])
def vehicle_loan():
    if request.method == 'POST':
        # Process vehicle loan form data here
        pass
    return render_template('vehicle_loan.html')

# Route for the educational loan page
@app.route('/educational-loan', methods=['GET', 'POST'])
def educational_loan():
    if request.method == 'POST':
        # Process educational loan form data here
        pass
    return render_template('educational_loan.html')

# Route for the business loan page
@app.route('/business-loan', methods=['GET', 'POST'])
def business_loan():
    if request.method == 'POST':
        # Process business loan form data here
        pass
    return render_template('business_loan.html')

if __name__ == '__main__':
    app.run(debug=True)
