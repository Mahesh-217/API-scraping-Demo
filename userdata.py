from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/profile', methods=['GET'])
def get_profile():

    user_agent = request.headers.get('User-Agent', '')
    if 'scrapy' in user_agent.lower() or 'beautifulsoup' in user_agent.lower():
        return jsonify({'error': 'Unauthorized access'}), 403

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
