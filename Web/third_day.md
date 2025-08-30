
---

# 🌐 Web 학습 3일차

## 1️⃣ Bootstrap이란?

* **CSS 프론트엔드 프레임워크 (Toolkit)**
* 미리 만들어진 다양한 **디자인 요소** 제공
* 빠르고 쉽게 웹사이트를 개발할 수 있도록 도움

📌 **Bootstrap CSS 파일 다운로드 → or CDN 사용 가능**

---

## 2️⃣ CDN (Content Delivery Network)

* 서버와 사용자 사이의 물리적 거리를 줄여 **로딩 속도 개선**
* 사용자와 가까운 **CDN 서버에 콘텐츠 저장 → 빠른 전달**

```html
<!-- Bootstrap CSS CDN 예시 -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```

---

## 3️⃣ Bootstrap 기본 사용법

Bootstrap은 **클래스 이름 규칙**을 통해 스타일 및 레이아웃 제공

### ✔ 클래스 규칙

* **Property**

  * `m`: margin
  * `p`: padding
* **Sides**

  * `t`: top
  * `b`: bottom
  * `s`: left (start)
  * `e`: right (end)
  * `y`: top, bottom
  * `x`: left, right
  * `blank`: 4 sides (전체)
* **Size**

  * `0` → `0px`
  * `1` → `0.25rem` (4px)
  * `2` → `0.5rem` (8px)
  * `3` → `1rem` (16px)
  * `auto` → 자동

📌 예시

```html
<div class="mt-3 p-2">
  여백이 적용된 박스
</div>
```

---

## 4️⃣ Reset CSS

* **User-agent stylesheet**
  → 브라우저마다 기본 제공하는 스타일 (브라우저마다 다름)
* 문제: 모든 브라우저에서 동일하게 보이기 어려움

✅ 해결 → **Reset CSS** (초기화 후 스타일링 시작)

* 대표적인 방식: **Normalize.css**

---

## 5️⃣ Bootstrap 기본 기능

* **Typography**: 글꼴, 제목 스타일 제공
* **Color System**: 의미 기반 색상 네이밍

  * `primary` (blue), `danger` (red) 등
* **Component**: UI 요소 모음

  * 버튼, 네비게이션 바(navbar), 카드(card), 폼(form), 드롭다운(dropdown)

---

## 6️⃣ Semantic Web

* **의미론적 구조**로 웹 데이터를 표현

### ✔ Semantic in HTML

요소 자체의 의미에 집중 → 가독성과 구조 강화

| 태그          | 의미                         |
| ----------- | -------------------------- |
| `<header>`  | 소개/탐색 콘텐츠                  |
| `<nav>`     | 네비게이션 영역                   |
| `<main>`    | 주요 콘텐츠                     |
| `<article>` | 독립적으로 배포 가능한 구획            |
| `<section>` | 문서의 독립 구획 (적합한 요소 없을 때 사용) |

### ✔ Semantic in CSS

CSS 유지보수를 쉽게 하는 **방법론**

* **OOCSS (Object Oriented CSS)**

  1. 구조(Structure)와 스킨(Skin) 분리
  2. 컨테이너(Container)와 콘텐츠(Content) 분리

---

## ✅ 핵심 정리

* **Bootstrap**: 미리 만들어진 CSS 프레임워크 (CDN으로 간편 사용)
* **Reset CSS**: 브라우저 간 차이를 없애고 동일한 출발선 만들기
* **Semantic Web**: 의미 중심의 HTML + 관리하기 쉬운 CSS

---
