# PosTechTask
Тестовая работа для компании Positive Technologies. Для корректной работы необходим python 3.

Модуль в качестве аргумента ожидает строку "program" с именем программы, версию которой нужно посмотреть. Вывод сделан для libreoffice. Для других программ корректный вывод не гарантируется.

Работает в нескольких вариантах:

1) В составе playbook:
    - запускать как "ansible-playbook -i hosts test.yml"
2) Как отдельный модуль:
    - запускать как "ansible -i hosts -m get_version -a "program=libreoffice" all"
3) C помощью API:
    - запускать python play.py
