
---

# 🌐 Web 학습 1일차

## 1️⃣ 알고리즘 vs 웹 개발

* **알고리즘**: 명확한 **정답**을 찾는 과정
* **웹 개발**: 여러 기술을 조합하여 **최적의 경험**을 만드는 과정

📌 **중요 포인트**

* **정답이 아닌 표준**을 찾기 → MDN & 공식 문서 참고 (처음부터 끝까지 다 읽지 말기!)
* 에러 메시지 → 그대로 구글링 (단순 How-to X, Why 중심 검색)
* **AI 협업** → 명확한 요구사항 제시, 디버깅·아이디어 함께 활용

---

## 2️⃣ WWW와 Web

💡 **WWW (World Wide Web)**
→ 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

💡 **Web**
→ Website, Web application 등을 통해 **정보 검색 & 상호작용** 가능

💡 **Web Page**
→ HTML, CSS, JS로 만들어진 Website의 한 요소

* **HTML**: Structure (구조)
* **CSS**: Styling (디자인)
* **JS**: Behavior (동작)

---

## 3️⃣ HTML 기초

### 📌 HTML이란?

* **HyperText Markup Language**
* 웹 페이지의 **의미와 구조**를 정의
* **HyperText**: 다른 페이지로 연결되는 **링크**

### 📌 HTML 기본 구조

```html
<!DOCTYPE html>   <!-- 문서가 HTML임을 선언 -->
<html>
  <head>
    <title>브라우저 탭 제목</title>
  </head>
  <body>
    <h1>제목</h1>
    <p>문단</p>
    <a href="#">링크</a>
    <img src="img.png" alt="대체 텍스트">
  </body>
</html>
```

| 태그                 | 의미    |
| ------------------ | ----- |
| `<p>`              | 문단    |
| `<a>`              | 하이퍼링크 |
| `<img>`            | 이미지   |
| `<h1>~<h6>`        | 제목    |
| `<ol>, <ul>, <li>` | 리스트   |
| `<em>`             | 기울임   |
| `<strong>`         | 굵게    |

---

## 4️⃣ HTML 요소 & 속성

* **요소(Element)** = `<여는 태그>내용</닫는 태그>`
* **속성(Attribute)** = 태그에 **추가 기능**을 부여

  * 작성 규칙: 공백, 따옴표 필수
  * 예: `<img src="dog.png" alt="강아지">`

---

## 5️⃣ CSS 기초

### 📌 CSS란?

* **Cascading Style Sheets**
* 웹 페이지의 **디자인 & 레이아웃** 담당

### 📌 적용 방법

1. Inline Style → ❌ 거의 사용 안 함
2. Internal Style → `<head>`에 `<style>`
3. External Style → 별도 CSS 파일 관리

### 📌 선택자 (Selector)

| 선택자            | 설명                |
| -------------- | ----------------- |
| `*`            | 전체 선택자            |
| `태그`           | 태그 요소 선택          |
| `.class`       | 클래스 선택자           |
| `#id`          | 아이디 선택자 (문서 내 유일) |
| `[attr=value]` | 속성 선택자            |
| `부모 자식`        | 자손 결합자            |
| `부모 > 자식`      | 직계 자식 선택자         |

---

## 6️⃣ CSS 명시도 (Specificity)

* **우선순위**:

  1. `!important`
  2. Inline Style
  3. 선택자: `id > class > tag`
  4. 코드 선언 순서

* **상속되는 속성**: `font`, `color`, `text-align` 등

* **상속되지 않는 속성**: `box-model`, `position` 등

---

## 7️⃣ 값과 단위

* **절대 단위**: `px`, `pt`, `cm`
* **상대 단위**: `%`, `em`, `rem`, `vw`, `vh`

📌 `em` = 부모의 font-size 기준
📌 `rem` = 최상위 `<html>`의 font-size 기준

---

## 8️⃣ CSS Box Model

HTML 요소는 모두 **사각형 상자(Box Model)** 로 구성됨

| 구성 요소   | 설명    |
| ------- | ----- |
| Content | 내용    |
| Padding | 안쪽 여백 |
| Border  | 테두리   |
| Margin  | 바깥 여백 |

👉 `box-sizing: border-box;` 설정 권장

---

## 9️⃣ 기타 태그

* `<dl>`: 정의 목록
* `<dt>`: 정의할 용어
* `<dd>`: 용어 설명

---

## 🎮 연습 추천

* 🥢 [Dinner CSS](https://flukeout.github.io/)
* 🐸 [Flex Froggy](https://flexboxfroggy.com/)

👉 재미있게 게임으로 CSS Flexbox & Selector 학습 가능!

---

✅ 오늘 배운 핵심:

* HTML = 구조, CSS = 디자인, JS = 동작
* CSS 선택자 & 명시도 이해
* `em` vs `rem`, Box Model

---
