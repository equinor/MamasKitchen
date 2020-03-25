import random

html_template = '''
<html>
<head>
<title>Mama's Kitchen - shut up and eat</title>
</head>
<body>
<h2>Mama's Kitchen - shut up and eat</h2>

Welcome to Mama's Kitchen, a diner where you shut up and eat whatever
you get served.
<p>
Menu this week:
<ul>
  <li>Monday: {}
  <li>Tuesday: {}
  <li>Wednesday: {}
  <li>Thursday: {}
  <li>Friday: {}
</ul>

<i>Notes: 
Dinner is served 5.15pm o'clock. Arrive on time! 
Kitchen only open to paying members. Monthly membership is $350.
</i>

</body>
</html>
'''


def read_dishes_from_file(filename):
    dishes = []
    with open(filename, 'rt') as f:
        for line in f:
            dishes.append(line.strip())
    return dishes


def select_random_week_menu(dishes):
    assert len(dishes) >= 5
    return random.sample(dishes, 5)


def create_webpage(template, menu):
    assert len(menu) == 5
    return template.format(*menu)


def write_webpage_to_file(filename, html):
    with open(filename, 'wt') as f:
        print(html, file=f)


if __name__ == '__main__':
    dishes = read_dishes_from_file("dishes.txt")
    menu = select_random_week_menu(dishes)
    webpage = create_webpage(html_template, menu)
    write_webpage_to_file("menu.html", webpage)
    print("Weekly menu updated!")
