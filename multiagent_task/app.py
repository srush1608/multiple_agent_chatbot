from flask import Flask, render_template, request, jsonify
from multiagent import generate_outline, fill_content, format_content

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get('topic', '')

    if not topic:
        return jsonify({"error": "Please provide a valid topic."}), 400

    try:
        # Generate outline
        outline = generate_outline(topic)
        print(f"Generated outline: {outline}")

        # Fill content
        content = fill_content(outline)
        print(f"Filled content: {content}")

        # Format content
        formatted_content = format_content(content)
        print(f"Formatted content: {formatted_content}")

        # Return formatted content as response
        return jsonify({
            "outline": outline,
            "content": content,
            "formatted_content": formatted_content
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
