# Импортируем необходимые модули для создания веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer


# Определяем класс обработчика запросов
class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Этот метод вызывается каждый раз, когда приходит GET-запрос
        Например, когда ты открываешь страницу в браузере
        """

        # Открываем HTML-файл и читаем его содержимое
        try:
            # 'r' означает режим чтения (read)
            # encoding='utf-8' нужен для корректного отображения русских букв
            with open('contacts.html', 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Отправляем код ответа 200 (всё хорошо)
            self.send_response(200)

            # ВАЖНО: Указываем, что отправляем HTML, а не JSON
            self.send_header('Content-type', 'text/html; charset=utf-8')

            # Завершаем заголовки
            self.end_headers()

            # Отправляем содержимое HTML-файла
            # encode('utf-8') преобразует текст в байты для передачи
            self.wfile.write(html_content.encode('utf-8'))

            print(f"✅ Запрос обработан: {self.path}")

        except FileNotFoundError:
            # Если файл не найден, отправляем ошибку 404
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            error_message = """
            <html>
                <body>
                    <h1>Ошибка 404</h1>
                    <p>Файл contacts.html не найден!</p>
                    <p>Убедитесь, что файл находится в той же папке, что и сервер.</p>
                </body>
            </html>
            """
            self.wfile.write(error_message.encode('utf-8'))
            print("❌ Ошибка: файл contacts.html не найден!")


# Функция для запуска сервера
def run_server():
    # Настройки сервера
    server_address = ('', 8000)  # Пустая строка означает localhost, 8000 - порт

    # Создаём сервер
    httpd = HTTPServer(server_address, MyHandler)

    print("=" * 50)
    print("🚀 Сервер запущен!")
    print("📍 Адрес: http://localhost:8000")
    print("💡 Открой эту ссылку в браузере")
    print("⏹️  Для остановки нажми Ctrl+C")
    print("=" * 50)

    try:
        # Запускаем сервер (он будет работать бесконечно)
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Обрабатываем нажатие Ctrl+C
        print("\n\n⏹️  Сервер остановлен")
        httpd.server_close()


# Точка входа программы
if __name__ == '__main__':
    run_server()
