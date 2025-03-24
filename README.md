# 1. 프로젝트와 앱 만들기
```shell
django-admin startproject board .
django-admin startapp articles
```
# 2. 프로젝트 등록하기
- board => settings => installed_apps => 'articles' 등록

# 3. 최상단에 templates 폴더 생성
- templates => 폴더 하위에 base.html 파일 생성 
- board => settings => templates => 'DIRS': [BASE_DIR / 'templates'] 추가하기

# 4. migrations models.py에 모델 생성

# 5. migration 작업(번역본 생성해주기)
```shell
python manage.py makemigrations
python manage.py migrate
```