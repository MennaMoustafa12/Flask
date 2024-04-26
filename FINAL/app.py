from flask import Flask, request, Response
from Project import split_arabic_text, get_gif_file, display_gif_sequence
import os

gif_folder = '/Users/Computer Science/Desktop/Gifs'
app = Flask(__name__)

@app.route('/Take_text', methods=['POST'])
def text_process():
    data = request.json  # Get input data from the request
    text = data.get('text')  # Extract text input from JSON data
    if text:
        # Process text input using your AI model to generate a GIF
        gif_data = split_arabic_text(text)

        arabic_text = display_gif_sequence(gif_data, gif_folder)

        if arabic_text:
            # Get the path of the generated GIF file
            gif_file_path = get_gif_file(arabic_text)
            if gif_file_path:
                # Open the GIF file and return it as binary data
                try:
                    with open(gif_file_path, 'rb') as f:
                        gif_binary = f.read()
                    # Return the GIF binary data with the appropriate content type
                    return Response(gif_binary, mimetype='image/gif')
                except FileNotFoundError:
                    return jsonify({'error': 'GIF file not found'}), 404
            else:
                return jsonify({'error': 'Failed to get GIF file path'}), 500
        else:
            return jsonify({'error': 'Failed to generate GIF from text'}), 500
    else:
        return jsonify({'error': 'Text input is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
