
# 🐍 Django 정리 노트

## 🌐 Web

> 데이터를 전처리하고, 직접 다루며, 사용자에게 제공하기 위한 서비스를 어떻게 구성할지 **API를 설계**한다!

### 🛠️ Web Application 개발

인터넷을 통해 사용자에게 제공되는 **소프트웨어 프로그램을 구축**하는 과정.

---

### ⚙️ Web의 동작 방식

* **클라이언트 (Client)** 👉 서비스를 요청하는 주체
* **서버 (Server)** 👉 요청에 응답하는 주체

📌 **흐름**
➡️ 클라이언트 **Request** ↔ 서버 **Response**

---

### 👀 우리가 웹페이지를 보게 되는 과정

1️⃣ 브라우저에 `google.com` 입력
2️⃣ 브라우저 → 구글 서버에 `"Google 홈페이지.html"` 요청
3️⃣ 서버 → DB에서 파일을 찾아 응답
4️⃣ 브라우저 → 응답을 해석해 화면에 표시

---

### 🎨 Frontend & Backend

* 🎭 **Frontend**: 사용자 UI & 상호작용 담당
  → HTML, CSS, JavaScript, 프론트엔드 프레임워크

* ⚡ **Backend**: 데이터 처리 & DB 상호작용
  → Python, Java, 프레임워크, DB, API, 보안 등

---

### 🔑 웹 서비스 개발에 필요한 요소

* 🔐 로그인 / 로그아웃
* 👥 회원 관리
* 💾 데이터베이스 연결
* 🛡️ 보안 처리

👉 모든 것을 직접 구현할 필요 ❌
→ **Web Framework** 활용 = 빠르고 안정적인 개발 가능

---

## 🚀 Django

* ✅ 대규모 서비스에서도 안정적인 서비스 제공
* 🇰🇷 국내는 Spring이 주력 → **취업 시 Spring 필수**

---

### 📦 가상 환경 (Virtual Environment)

> 패키지를 **독립적으로 격리 관리**하기 위한 환경

#### 왜 필요할까? 🤔

1. **버전 충돌 방지**

   * A: requests v1 필요
   * B: requests v2 필요
   * 👉 가상환경 없이는 공존 불가

2. **패키지 충돌 방지**

   * A: water 패키지
   * B: fire 패키지
   * 👉 충돌 발생 → 독립된 환경 필요

---

### 📝 Django 프로젝트 생성 루틴

1. 가상환경 생성

   ```bash
   python3 -m venv venv
   ```
2. 가상환경 활성화

   ```bash
   source venv/bin/activate
   ```
3. Django 설치

   ```bash
   pip install django
   ```
4. 의존성 관리

   ```bash
   pip freeze > requirements.txt
   pip install -r requirements.txt
   ```
5. 서버 실행

   ```bash
   python3 manage.py runserver
   ```

---

### 📂 Django 프로젝트 구조

* ⚙️ **settings.py** → 프로젝트 설정
* 🌐 **urls.py** → URL 라우팅
* 📦 **\_\_init\_\_.py** → 패키지 인식
* ⚡ **asgi.py** → 비동기 서버 설정
* 🔗 **wsgi.py** → 웹 서버 설정
* 🔧 **manage.py** → 유틸리티 명령

---

### 🧩 Django 앱 구조

* 🛠️ **admin.py** → 관리자 페이지
* 🗂️ **models.py** → DB 모델 정의 (**M**)
* 👨‍💻 **views.py** → 요청/응답 처리 (**V**)
* 📋 **apps.py** → 앱 정보
* 🧪 **tests.py** → 테스트 코드

---

### 🔄 요청 & 응답

📌 클라이언트 요청 → 서버 처리 → 응답 반환

---

### 🎨 render 함수

```python
render(request, template_name, context)
```

* 📨 request: 요청 객체
* 📄 template\_name: 템플릿 경로
* 📦 context: 데이터 (dict)

✨ **렌더링** = 템플릿(HTML) + 데이터 → 완성된 HTML
✨ **HttpResponse 객체** = 최종 응답

---

## 🏗️ 디자인 패턴

### 🧩 MVC 패턴 (일반적)

* **M**: 데이터
* **V**: 화면
* **C**: 로직

### 🧩 MTV 패턴 (Django)

* **M (Model)**: 데이터 로직
* **T (Template)**: 화면
* **V (View)**: 로직 & 응답

📌 Django에서는 **Controller → View**, **View → Template**

---

### 📌 Django Project vs Application

* **Project** = 전체 앱 집합 (DB, URL, 전반 관리)
* **Application** = 독립 기능 모듈

#### 명령어

```bash
django-admin startproject 프로젝트명 .
python manage.py startapp 앱이름
```

📌 앱 등록 → `settings.py` → `INSTALLED_APPS`

---

### 🔗 Django `{% url %}` 태그

```python
# urls.py
path("create_todo/", views.create_todo, name="create_todo")

# template
<a href="{% url 'create_todo' %}">할 일 추가</a>
```

---

## 🌍 REST API

* **REST (Representational State Transfer)**
  → API 설계 방법론

* REST 원칙 준수 = **RESTful**

* 핵심:

  1. 자원 정의
  2. 자원 주소 지정

---

### 📌 REST 자원 사용 방법

1. 🆔 **URI (식별)**: `https://example.com`
2. ⚡ **HTTP Methods (행위)**: GET, POST, PUT, DELETE
3. 📦 **JSON (표현)**: 데이터 직렬화

---

### 🗂️ URI 구성 요소

* 🌐 **Schema/Protocol**: http, https, mailto, ftp
* 🏠 **Domain Name**: 서버 주소 (`google.com`)
* 🚪 **Port**: 접속 게이트 (http:80, https:443, django:8000)
* 📂 **Path**: 리소스 경로
* 🔑 **Parameters**: `?key=value&key2=value2`
* 📍 **Anchor**: `#section` (북마크, 서버 전송 ❌)

---