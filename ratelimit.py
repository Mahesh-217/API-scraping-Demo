from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(app)
limiter.key_func = get_remote_address

# Example API endpoint
@app.route('/api/profile', methods=['GET'])
@limiter.limit('10/minute')  # Limit to 10 requests per minute
def get_profile():
    # Check for headers commonly used by scraping tools
    user_agent = request.headers.get('User-Agent', '')
    if 'scrapy' in user_agent.lower() or 'beautifulsoup' in user_agent.lower():
        return jsonify({'error': 'Unauthorized access'}), 403

    # Implement other checks to validate the request
    # For example, you can verify API keys, IP addresses, or session tokens

    # Process the request and return the profile data
    profile_data = {
        'name': 'John Doe',
        'linkedin_url': 'https://www.linkedin.com/in/johndoe',
        'username': 'johndoe',
        'title': 'Software Engineer',
        'company': 'Acme Inc.',
        'location': 'San Francisco Bay Area',
        'summary': 'Experienced software engineer with expertise in web development...',
        'experience': [
            {
                'title': 'Senior Software Engineer',
                'company': 'XYZ Corp',
                'duration': '2018 - Present',
                'description': 'Responsible for developing and maintaining...',
            },
            {
                'title': 'Software Engineer',
                'company': 'ABC Inc.',
                'duration': '2015 - 2018',
                'description': 'Contributed to the development of...',
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Science in Computer Science',
                'school': 'University of ABC',
                'duration': '2011 - 2015',
            }
        ],
        'skills': ['Python', 'JavaScript', 'HTML', 'CSS', 'Node.js'],
        'languages': ['English', 'Spanish'],
        'certifications': ['AWS Certified Developer', 'Google Certified Professional Cloud Architect'],
        'interests': ['Machine Learning', 'Blockchain', 'Photography'],
    }

    return jsonify(profile_data)

if __name__ == '__main__':
    app.run()
