from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters from the URL
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate that both query parameters are provided
    if not slack_name or not track:
        return jsonify({"error": "Both slack_name and track are required."}), 400

    # Get the current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get the current UTC time with a +/- 2 minute window
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs based on your repository and file names
    github_repo_url = "https://github.com/yuenfu001/endp"
    github_file_url = f"{github_repo_url}/blob/main/endpoint.py"

    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
