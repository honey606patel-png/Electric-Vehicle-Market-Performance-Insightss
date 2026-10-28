from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Replace the base URL with your actual Tableau Public view URL
    base_url = "https://public.tableau.com/views/EV_Market_Performance_Dashboard_17932088931070/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
    
    # Ensure embed parameters are appended
    if "?:showVizHome=no" not in base_url:
        tableau_url = base_url + "?:showVizHome=no&:embed=true"
    else:
        tableau_url = base_url

    return render_template('index.html', dashboard_url=tableau_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)