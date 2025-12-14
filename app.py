from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi App CI/CD</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }
            .container {
                background: white;
                border-radius: 15px;
                padding: 40px;
                max-width: 500px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                text-align: center;
            }
            h1 { color: #667eea; margin-bottom: 20px; }
            p { color: #666; margin-bottom: 30px; }
            button {
                background: #667eea;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover { background: #764ba2; }
            #status { margin: 20px 0; font-size: 1.2em; font-weight: bold; }
            .ok { color: #28a745; }
            .error { color: #dc3545; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Mi Aplicación</h1>
            <p>Desplegada automáticamente con GitHub Actions</p>
            <div id="status">Verificando...</div>
            <button onclick="checkStatus()">Actualizar Estado</button>
        </div>
        <script>
            async function checkStatus() {
                try {
                    const res = await fetch('/api/health');
                    const data = await res.json();
                    document.getElementById('status').innerHTML = 
                        '<span class="ok">✅ Sistema: ' + data.status.toUpperCase() + '</span>';
                } catch (error) {
                    document.getElementById('status').innerHTML = 
                        '<span class="error">❌ Error al conectar</span>';
                }
            }
            checkStatus();
        </script>
    </body>
    </html>
    '''

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)