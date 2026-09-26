from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        category = data.get('category', 'General')
        if title:
            task = {'id': len(tasks) + 1, 'title': title, 'category': category}
            tasks.append(task)
            return jsonify({'success': True, 'task': task}), 201
        return jsonify({'error': 'Title is required'}), 400
    
    return jsonify({'tasks': tasks})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
