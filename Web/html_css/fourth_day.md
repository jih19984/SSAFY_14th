
---

# 🌐 Web 학습 4일차

## 1️⃣ 디바이스별 화면 차이

🍎 **모든 기기에서 화면이 똑같이 보장되지 않는다**

* PC, 태블릿, 스마트폰 → 화면 크기와 비율이 다름
* HTML, CSS 렌더링 환경도 기기마다 차이가 있음

👉 따라서 **반응형 웹 디자인** 필요!

---

## 2️⃣ Bootstrap Grid System

💡 **12개의 컬럼**으로 구성된 시스템

* 웹 페이지의 레이아웃을 효율적으로 구성할 수 있도록 설계됨
* 컬럼 수를 조합하여 원하는 크기의 레이아웃 생성

📌 **구조**

* **Container**: 컬럼들을 담는 공간
* **Row**: 열(Column)들을 수평으로 묶는 단위
* **Column**: 실제 콘텐츠가 들어가는 영역
* **Gutter**: 컬럼과 컬럼 사이의 여백

  * X축 → **padding** 사용
  * Y축 → **margin** 사용

---

## 3️⃣ 반응형 웹 디자인

💡 디바이스 종류·화면 크기에 상관없이 **일관된 레이아웃과 사용자 경험** 제공

Bootstrap Grid System → **6개의 Breakpoint** 제공

| Breakpoint | 크기 기준     | 클래스 접두사     |
| ---------- | --------- | ----------- |
| xs         | `<576px`  | `.col-`     |
| sm         | `≥576px`  | `.col-sm-`  |
| md         | `≥768px`  | `.col-md-`  |
| lg         | `≥992px`  | `.col-lg-`  |
| xl         | `≥1200px` | `.col-xl-`  |
| xxl        | `≥1400px` | `.col-xxl-` |

📌 각 Breakpoint마다 다른 레이아웃을 지정 가능

---

## 4️⃣ Grid System 예시

```html
<div class="container">
  <div class="row">
    <div class="col-sm-6 col-md-4 col-lg-3 bg-primary text-white">
      Column 1
    </div>
    <div class="col-sm-6 col-md-4 col-lg-3 bg-success text-white">
      Column 2
    </div>
    <div class="col-sm-6 col-md-4 col-lg-3 bg-danger text-white">
      Column 3
    </div>
    <div class="col-sm-6 col-md-4 col-lg-3 bg-warning">
      Column 4
    </div>
  </div>
</div>
```

📌 위 예시에서는 화면 크기에 따라 **컬럼 크기 자동 조정**

* 작은 화면(xs/sm) → 2개씩 표시
* 중간 화면(md) → 3개씩 표시
* 큰 화면(lg 이상) → 4개씩 표시

---

## 5️⃣ 관련 개념

* **UX (User Experience)**: 사용자가 느끼는 경험, 편리성과 직관성 중시
* **UI (User Interface)**: 사용자와 상호작용하는 화면 요소 (버튼, 메뉴 등)
* **Grid System**: 웹 페이지의 **레이아웃 뼈대**
* **Grid Cards**: Bootstrap 카드 컴포넌트를 Grid 시스템과 결합하여 레이아웃 구성

---

## ✅ 핵심 정리

* 기기별 화면 차이를 고려해 **반응형 웹** 필수
* Bootstrap Grid System → **12 컬럼 + 6 Breakpoints**
* **Container → Row → Column 구조** 이해
* UX/UI 개선을 위해 Grid를 활용해 **일관된 사용자 경험 제공**

---
