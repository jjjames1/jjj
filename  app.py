from flask import Flask, render_template_string

# Flask App Initialization
app = Flask(__name__)

# HTML Template for the Web Interface
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Match Predictions</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .match { margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        .match h3 { margin: 0; }
        .match p { margin: 5px 0; }
        .best-play { font-weight: bold; color: green; }
    </style>
</head>
<body>
    <h1>Upcoming Match Predictions</h1>
    {% for match in matches %}
    <div class="match">
        <h3>{{ match.home_team }} vs {{ match.away_team }}</h3>
        <p><strong>Predicted Winner:</strong> {{ match.predictions.Predicted_Winner }}</p>
        <p><strong>Outcome Probabilities:</strong>
            Home Win: {{ match.predictions.Outcome_Probabilities['Home Win'] }}%,
            Draw: {{ match.predictions.Outcome_Probabilities['Draw'] }}%,
            Away Win: {{ match.predictions.Outcome_Probabilities['Away Win'] }}%
        </p>
        <p><strong>Best Play Option:</strong> <span class="best-play">{{ match.predictions.Best_Play_Option }}</span></p>
        <p><strong>Total Goals:</strong> {{ match.predictions.Total_Goals }}</p>
        <p><strong>Total Cards:</strong> {{ match.predictions.Total_Cards }}</p>
        <p><strong>Total Corners:</strong> {{ match.predictions.Total_Corners }}</p>
        <p><strong>Both Teams to Score:</strong> {{ match.predictions.Both_Teams_To_Score }}</p>
        <p><strong>Likely Score:</strong> {{ match.predictions.Likely_Score }}</p>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def home():
    # Example match data (replace this with your actual data)
    matches_with_predictions = [
        {
            'home_team': 'NAC Breda',
            'away_team': 'Heracles Almelo',
            'match_date': '2023-10-15',
            'match_status': 'Scheduled',
            'predictions': {
                'Predicted_Winner': 'Away Win',
                'Outcome_Probabilities': {'Home Win': 10.0, 'Draw': 29.88, 'Away Win': 60.12},
                'Best_Play_Option': 'Away Win',
                'Total_Goals': 3,
                'Total_Cards': 8,
                'Total_Corners': 6,
                'Both_Teams_To_Score': 'Yes',
                'Likely_Score': '1-2'
            }
        },
        {
            'home_team': 'SV Werder Bremen',
            'away_team': '1. FSV Mainz 05',
            'match_date': '2023-10-15',
            'match_status': 'Scheduled',
            'predictions': {
                'Predicted_Winner': 'Home Win',
                'Outcome_Probabilities': {'Home Win': 60.0, 'Draw': 30.0, 'Away Win': 10.0},
                'Best_Play_Option': 'Home Win',
                'Total_Goals': 3,
                'Total_Cards': 7,
                'Total_Corners': 4,
                'Both_Teams_To_Score': 'Yes',
                'Likely_Score': '3-0'
            }
        }
    ]
    
    # Render the HTML template with match data
    return render_template_string(html_template, matches=matches_with_predictions)

if __name__ == '__main__':
    app.run(debug=True)