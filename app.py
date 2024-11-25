from flask import Flask, render_template, request, jsonify
from multiagent import generate_outline, fill_content, format_content

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form.get('topic', '')

    if not topic:
        return jsonify({"error": "Please provide a valid topic."}), 400

    try:
        # Generate outline
        outline = generate_outline(topic)

        # Fill content
        content = fill_content(outline)

        # Format content
        formatted_content = format_content(content)

        # Return response
        return jsonify({
            "outline": outline,
            "content": content,
            "formatted_content": formatted_content
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
