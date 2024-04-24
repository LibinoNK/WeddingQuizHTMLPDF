import db
import pdfkit

result_tuple = {
    'season': {'summer': 'Летом', 'autumn': 'Осенью', 'winter': 'Зимой', 'spring': 'Весной'}.get(db.data['season'],
                                                                                                 None),
    'amount': {'together': 'Только вдвоем', 'folks': 'Только близкие', 'upto100': 'До 100', 'more100': 'Более 100'}.get(
        db.data['amount'], None),
    'place': {'restaurant': 'Банкетный зал', 'unique': 'Уникальная локация', 'garden': 'Вечеринка в саду',
              'sea': 'Море'}.get(db.data['place'], None),
    'style': {'romantic': 'Романтическая свадьба', 'vintage': 'Винтажная свадьба', 'eccentric': 'Эксцентричная свадьба',
              'modern': 'Современная свадьба', 'classic': 'Классическая свадьба',
              'travel': 'Свадьба в стиле travel'}.get(db.data['style'], None),
    'colors': {'emerald_green': 'Изумрудно-зеленая', 'vanilla_cream': 'Ванильная', 'macchiato': 'Капучино',
               'dusty_rose': 'Пыльная роза', 'wine': 'Винная', 'quartz_pink': 'Розовый кварц'}.get(db.data['colors'],
                                                                                                   None),
    'fashion': {'trapezoidal': 'Трапециевидный силуэт', 'naiad': 'Русалка', 'sheath': 'Футляр',
                'ball_gown': 'Бальное платье', 'overalls': 'Комбинезон', 'retro': 'Ретро'}.get(db.data['fashion'],
                                                                                               None),
    'costume': {'classic_costume': 'Классика', 'tuxedo': 'Смокинг', 'casual': 'Кэжуал',
                'modern_costume': 'Современный костюм'}.get(db.data['costume'], None)
}

photo_season_path = {
    'summer': 'summer',
    'spring': 'spring',
    'autumn': 'autumn',
    'winter': 'winter'
}.get(db.data['season'],
      'winter')  # Если сезон отсутствует в данных или не соответствует ни одному времени года, используем 'winter' по умолчанию

# Определяем переменную photo_amount_path на основе значения db.data['amount']
photo_amount_path = {
    'together': 'together',
    'folks': 'folks',
    'upto100': 'upto100',
    'more100': 'more100'
}.get(db.data['amount'], None)

# Определяем переменную photo_place_path на основе значения db.data['place']
photo_place_path = {
    'restaurant': 'restaurant',
    'unique': 'unique',
    'garden': 'garden',
    'sea': 'sea'
}.get(db.data['place'], None)

# Определяем переменную photo_style_path на основе значения db.data['style']
photo_style_path = {
    'romantic': 'romantic',
    'vintage': 'vintage',
    'eccentric': 'eccentric',
    'modern': 'modern',
    'classic': 'classic',
    'travel': 'travel'
}.get(db.data['style'], None)

# Определяем переменную photo_colors_path на основе значения db.data['colors']
photo_colors_path = {
    'emerald_green': 'emerald_green',
    'vanilla_cream': 'vanilla_cream',
    'macchiato': 'macchiato',
    'dusty_rose': 'dusty_rose',
    'wine': 'wine',
    'quartz_pink': 'quartz_pink'
}.get(db.data['colors'], None)

# Определяем переменную photo_fashion_path на основе значения db.data['fashion']
photo_fashion_path = {
    'trapezoidal': 'trapezoidal',
    'naiad': 'naiad',
    'sheath': 'sheath',
    'ball_gown': 'ball_gown',
    'overalls': 'overalls',
    'retro': 'retro'
}.get(db.data['fashion'], None)

# Определяем переменную photo_costume_path на основе значения db.data['costume']
photo_costume_path = {
    'classic_costume': 'classic_costume',
    'tuxedo': 'tuxedo',
    'casual': 'casual',
    'modern_costume': 'modern_costume'
}.get(db.data['costume'], None)

# Читаем содержимое index.html
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Заменяем каждое вхождение {} в HTML на соответствующее значение из словаря result_tuple
formatted_html = html_content.format(
    result_tuple['season'],
    photo_season_path,
    photo_season_path,
    photo_season_path,
    result_tuple['amount'],
    photo_amount_path,
    photo_amount_path,
    result_tuple['place'],
    photo_place_path,
    photo_place_path,
    photo_place_path,
    photo_place_path,
    result_tuple['style'],
    photo_style_path,
    photo_style_path,
    result_tuple['colors'],
    photo_colors_path,
    result_tuple['fashion'],
    photo_fashion_path,
    photo_fashion_path,
    photo_fashion_path,
    result_tuple['costume'],
    photo_costume_path,
    photo_costume_path,
    photo_costume_path
)

# Записываем отформатированную HTML-страницу в новый файл
# with open(f'{db.data["user_id"]}_output.html', 'w',
with open('output.html', 'w', encoding='utf-8') as file:  # поменять название на уникальное каждый раз
    file.write(formatted_html)

# Настройки pdfkit (путь к исполняемому файлу wkhtmltopdf)
# config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

# Преобразование HTML в PDF
pdfkit.from_file("output.html", "output.pdf", verbose=True, options={"enable-local-file-access": True})
f = pdfkit.PDFKit
# command(f)
print("=" * 50)
