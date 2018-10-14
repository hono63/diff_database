# diff_database

ただのデータベース

### Django install
pip install Django

### Apache & mod_wsgi環境

sudo yum install -y httpd php mariadb-server php-mysqlnd  
sudo yum install httpd-devel  
pip install mod-wsgi  

### お試し
https://qiita.com/gragragrao/items/373057783ba8856124f3

外部公開向けには、0:[port番号]で。
ALLOWED_HOSTにドメイン名を追加せなあかんかった。

### crud参考
https://qiita.com/kaki_k/items/6e17597804437ef170ae

### command
起動
~~~
python manage.py runserver [8000]
~~~