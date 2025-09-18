
---

# 🌐 Web 학습 2일차

## 1️⃣ CSS Box Model

### ✔ Block 요소

* 하나의 독립된 덩어리처럼 동작
* 항상 새로운 줄에서 시작 (한 줄 전체 차지, 너비 100%)
* `width`, `height`, `margin`, `padding` 모두 사용 가능
* 다른 요소를 밀어냄

📌 대표 태그 → **`<div>`**
→ 요소들을 그룹화하여 레이아웃 구성/스타일링 가능

---

### ✔ Inline 요소

* 문장 안 단어처럼 흐름에 따라 배치
* 줄바꿈 ❌ (콘텐츠 크기만큼만 영역 차지)
* `width`, `height` ❌ 사용 불가
* 상하 방향 margin/padding은 공간 차지 안 함
* 좌우 방향 margin/padding은 적용됨

📌 대표 태그 → **`<a>`, `<img>`, `<span>`, `<strong>`**

---

### ✔ 기타 Display 속성

* `inline-block` : inline처럼 흐름 유지 + `width`, `height` 사용 가능
* `none` : 요소 숨김 (공간도 차지 안 함)
* `flex` : Flexbox 컨테이너 지정

---

📌 **Normal flow**
→ 레이아웃 변경 없이 요소가 기본 흐름대로 배치되는 방식

---

## 2️⃣ CSS Position

### ✔ Layout vs Position

* **Layout**: 요소의 크기·위치 조정 → 전체 디자인 뼈대
* **Position**: Normal flow에서 제거 → 특정 위치 배치

### ✔ Position 종류

| 값          | 설명                                                         |
| ---------- | ---------------------------------------------------------- |
| `static`   | 기본값, Normal flow 배치, `top/right/bottom/left` 적용 ❌          |
| `relative` | Normal flow 유지, 자기 원래 위치 기준 이동                             |
| `absolute` | Normal flow에서 제거, 가장 가까운 `relative` 부모 기준 이동 (없으면 body 기준) |
| `fixed`    | Normal flow에서 제거, viewport 기준 고정 (스크롤에도 위치 고정)             |
| `sticky`   | relative + fixed 혼합 (스크롤 임계점 전까지 relative처럼 동작)            |
| `z-index`  | 쌓임 순서 제어 (static ❌, relative/absolute/fixed/sticky 요소만 적용) |

📌 **Position만으로 정렬/배분은 한계 → Flexbox 활용 필요!**

---

## 3️⃣ CSS Flexbox

### ✔ Display 타입

* **Outer display**: block / inline
* **Inner display**: 내부 요소 배치 방식 → Flexbox 핵심

---

### ✔ Flexbox 구성 요소

* **main axis** (주축) : 시작(main start) \~ 끝(main end)
* **cross axis** (교차축) : 시작(cross start) \~ 끝(cross end)
* **flex container** : `display: flex;`가 적용된 부모 요소
* **flex item** : 컨테이너의 1차 자식 요소

---

### ✔ Flex Container 속성

| 속성                | 설명                                                                          |
| ----------------- | --------------------------------------------------------------------------- |
| `display: flex;`  | Flex 컨테이너 지정                                                                |
| `flex-direction`  | 주축 방향 지정 (`row`, `column`, `row-reverse`, `column-reverse`)                 |
| `flex-wrap`       | 줄바꿈 여부 (`nowrap`, `wrap`)                                                   |
| `justify-content` | 주축 정렬 (`flex-start`, `center`, `flex-end`, `space-between`, `space-around`) |
| `align-items`     | 교차축 단일 행 정렬 (`flex-start`, `center`, `flex-end`, `stretch`)                 |
| `align-content`   | 교차축 여러 줄 정렬 (wrap일 때만 적용)                                                   |

---

### ✔ Flex Item 속성

| 속성           | 설명                                     |
| ------------ | -------------------------------------- |
| `align-self` | 특정 아이템 교차축 정렬 (컨테이너 `align-items` 덮어씀) |
| `flex-grow`  | 여유 공간 분배 비율                            |
| `flex-basis` | 아이템 기본 크기                              |
| `order`      | 아이템 순서 변경                              |

---

### ✔ 예시 코드

```html
<div class="container">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
</div>

<style>
  .container {
    display: flex;
    flex-direction: row;   /* 가로 정렬 */
    justify-content: center; /* 주축 중앙 */
    align-items: center;     /* 교차축 중앙 */
    height: 200px;
    border: 2px solid black;
  }
  .item {
    flex: 1;                 /* 동일한 비율로 공간 차지 */
    margin: 5px;
    background: lightblue;
    text-align: center;
  }
</style>
```

---

📌 **실제 활용 예시**

* `fixed` + `z-index` → 네비게이션 바 상단 고정
* `flexbox` → 화면 중앙 배치, 반응형 레이아웃 구성

---

# 🎨 Flexbox 시각적 정리

## 1️⃣ flex-direction (주축 방향)

```css
.container {
  display: flex;
  flex-direction: row; /* 기본값 */
}
```

| 값                | 배치 방향        |
| ---------------- | ------------ |
| `row`            | ➡ (가로, 좌→우)  |
| `row-reverse`    | ⬅ (가로, 우→좌)  |
| `column`         | ⬇ (세로, 위→아래) |
| `column-reverse` | ⬆ (세로, 아래→위) |

---

## 2️⃣ justify-content (주축 정렬)

```css
.container {
  display: flex;
  justify-content: center;
}
```

| 값               | 정렬 방식                         |
| --------------- | ----------------------------- |
| `flex-start`    | \[⬜⬜⬜      ] → 시작점 정렬         |
| `center`        | \[   ⬜⬜⬜   ] → 중앙 정렬          |
| `flex-end`      | \[      ⬜⬜⬜] → 끝점 정렬          |
| `space-between` | \[⬜   ⬜   ⬜] → 양 끝 고정 + 중간 균등 |
| `space-around`  | \[ ⬜  ⬜  ⬜ ] → 양 옆 + 중간 균등    |
| `space-evenly`  | \[ ⬜ ⬜ ⬜ ] → 모든 간격 동일         |

---

## 3️⃣ align-items (교차축 단일 행 정렬)

```css
.container {
  display: flex;
  align-items: center;
}
```

| 값            | 정렬 방식      |
| ------------ | ---------- |
| `flex-start` | 위쪽 정렬      |
| `center`     | 세로 중앙 정렬   |
| `flex-end`   | 아래쪽 정렬     |
| `stretch`    | 높이 늘려 맞춤   |
| `baseline`   | 텍스트 기준선 정렬 |

---

## 4️⃣ align-content (교차축 여러 줄 정렬)

(여러 줄이 생길 때만 적용됨: `flex-wrap: wrap;` 필수)

```css
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: space-between;
}
```

| 값               | 정렬 방식                |
| --------------- | -------------------- |
| `flex-start`    | 위쪽 줄부터 쌓임            |
| `center`        | 전체 줄을 가운데로 모음        |
| `flex-end`      | 아래쪽 줄부터 쌓임           |
| `stretch`       | 빈 공간 채워 늘어남          |
| `space-between` | 위–아래 줄 끝 고정 + 나머지 균등 |
| `space-around`  | 위–아래 포함, 전체 균등 간격    |

---

## 5️⃣ flex item 속성

```css
.item {
  flex-grow: 1;   /* 공간 분배 */
  flex-basis: 100px; /* 기본 크기 */
  order: 2;       /* 순서 변경 */
  align-self: flex-end; /* 개별 정렬 */
}
```

* `flex-grow`: 남은 공간 차지 비율
* `flex-basis`: 기본 크기
* `order`: 아이템 순서 변경
* `align-self`: 특정 아이템만 개별 정렬

---

✅ 핵심 요약

* **주축 → `flex-direction`, `justify-content`**
* **교차축 → `align-items`, `align-content`**
* **아이템 개별 제어 → `align-self`, `flex-grow`, `order`**

---
