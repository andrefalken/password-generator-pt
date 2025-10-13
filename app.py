# Import modules
from flask import Flask, render_template, request, jsonify
from password_generator import password_generator
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Creating the application
# app is the main site
# __name__ is the variable who identifies this current file

app = Flask(__name__)

# Main website address
@app.route('/')
# Function that will run
def index():
    """Render the main page"""
    # It will show the main HTML page
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    """Generate password based on user input"""
    try:
        # Get quantity from form
        quantity = int(request.form.get('quantity', 16))

        # Validate input
        if quantity < 8:
            return jsonify({'error': 'Password must be at least 8 characters'}), 400
        if quantity > 50:
            return jsonify({'error': 'Password must be less than 50 characters'}), 400

        # Generate password
        # Function who will generate the password
        password = password_generator(quantity)

        logger.info(f"Generated password with {quantity} characters.")

        return jsonify({ # Return the password in JSON format (as a data package)
            'password': password,
            'length': len(password)
        })
    # If the user type a letter instead a number
    except ValueError:
        return jsonify({'error': 'Please enter a valid number'}), 400
    # Any other unexpected kind of error
    except Exception as e:
        logger.error(f"Error generating password: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

# For others software to use
@app.route('/api/generate/<int:quantity>')
# Get the number directly from the URL
def api_generate(quantity):
    """API endpoint for password generation"""
    try:
        if quantity < 8 or quantity > 50:
            return jsonify({'error': 'Quantity must be between 8 and 50'}), 400
        password = password_generator(quantity)
        return jsonify({'password': password, 'length': len(password)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Just run if it's the main file
if __name__ == '__main__':
    app.run(debug=False)