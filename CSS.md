# CSS

Cascading Style Sheets

**CSS 란?**

- 스타일을 지정하기 위한 언어
- 오픈 웹의 핵심 언어 중 하나!
- 프로그래밍 언어 X 마크업 언어 X Style shet 언어!
- HTML 문서에 있는 요소들에 선택적으로 스타일을 적용할 수 있다는 말.

***CSS 는 위에서 아래로 흐른다.***

```html
h1(선택자) {
	color : blue;(선언)
    font-size(속성):15px;(값)
}
```

**CSS 정의 방법**

1. 인라인

   - <body> 에서 직접 정의

2. 내부참조 

   - <head> 에서 직접 정의

3. 외부참조

   - CSS 파일을 만들고 링크를 통해 사용

> 색, 사이즈, 여백 정도를 주로 사용 하나 알려고 하면 끝이 없는 무궁무진한 세계

4. 각각의 rule set은 반드시 {}로 감싸져야하고, 

   값 구분은 콜론(:)을 사용 다음 선언 구분은 세미콜론 (;) 사용.

5. 여러 요소 선택 가능. p,li,h1 { } 이런 식으로 여러 요소 한번에 적용 가능



**CSS 사용방법**

CSS는 "선택" 해서 스타일을 적용.

같은 레벨이라면 나중에 "선언" 된 것이 적용.

> id > class > 태그 순
>
> id는 보통 js로 개발할 때 활용! 문서에서 하나만 쓰길 권장함.

.name { color: blue } 로 미리 지정해 놓고

태그 class="name" 로 사용.



**CSS 단위**

1. %: 백분율 단위 - 가변적인 레이아웃에서 보통 사용
2. em: 상속의 영향을 받음 - 배수단위
3. rem: 상속의 영향을 받지 않음 - 최상위 요소의 사이즈를 기준 (기본은 16px)

**색상 단위**

1. rgba = (0, 0, 0, 투명도)
2. HSC색상 = 색상, 채도, 명도

### Box model

모든 요소는 '네모(박스모델)'이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다

> Normal flow

**CSS 용어**

margin = 여백

> margin: 10px 20px 30px 40px; - 상 우 하 좌
>
> margin: 10px, 0px, 5px; - 상 좌우 하
>
> margin: 10px, 0px - 상하 좌우

border = 테두리 예) border: 1px solid black;

padding = 내부 여백

기본적으로 box - sizing은 content box가 기본 값

*{box-sizing: border-box;} 를 넣어주면 박스사이즈가 변하는걸 방지함. 

> margin은 블락요소(div)에만 먹히고,
>
> 인라인 요소인 <span>에는 먹히지 않는다.



### CSS Display

display: block - 줄바꿈이 일어나는 요소

- 화면 크기 전체의 가로 폭을 차지
- 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

display: inline - 줄바꿈이 일어나지 않는 행의 일부 요소

- content 넘비 만큼 가로 폭을 차지함.

display: inline-block - block과 inline 레벨 요소의 특징 가짐

- inline 처럼 한줄에 표시 할 수 있고 block처럼 높이 길이 마진 지정 가능.

display: none

- 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

- div: 블록 레벨 요소

- span: 인라인 레벨 요소

- 블록: 너비를 가질 수 없다면 자동으로 margin

- 행은 inline 열은 block 으로 생각하면 됨.



### CSS position

- 문서 상에서 요소의 위치를 지정
- static: 기본 값
  - 요소의 배치 순서에 따름(Normal flow)
- relative
  - 자기 자신의 static 위치를 기준으로 이동 (Normal flow 유지)
- absolute
  - 절대 위치(Normal flow에서 벗어남)
  - 부모의 값이 static이 아니어야 사용 할 수 있음
- relative = 외출(본인 자리가 있음) absolute = 출가(본인 자리가 없음)

- fixed
  - 고정해서 따라다니는 자기공간 X
- sticky
  - 자기 공간 O 화면이 이동하면 따라옴

### flex

- display: flex or inline-flex < 부모에서 지정

1. flex-direction

   - row : 좌에서 우
   - row-reverse : 우에서 좌 (이렇게 하는 나라들에서 주로 씀 - 인도, 일본)
   - column : 위에서 아래
   - column-reverse : 아래에서 위

2. flex-wrap

   - wrap : 1, 2, 3

     ​       	 4, 5

   - nowrap : 카드들을 세로로길게 1, 2, 3, 4, 5

   - wrap-reverse : 3, 2, 1

     ​                           5, 4

   - nowrap-reverse : 5,4,3,2,1

3. flex-flow (direction + wrap)

   - 예) flex-flow: row wrap

4. justify-content

   - main axis(가로)를 기준으로 공간 배분

5. aligin-items

   - 모든 아이템을 cross axis(세로)를 기준으로 정렬
   - stretch, flex-start, flex-end, center, baseline(첫째꺼 글씨 크게) 등으로 사용

6. align-self

   - 해당 속성은 컨테이너 X 개별 아이템에 적용

7. flex-grow

   - 남은 영역을 아이템에 분배

8. order

   - 배치 순서

> flex에서 자식한테 주는건 self, grow, order 뿐!

1. sticky 예시

   > top {
   >
   >   position: sticky;
   >
   >   top: 0;
   >
   > }

2. fixed 예시

   > top-btn {
   >
   >   position: fixed;
   >
   >   bottom: 1rem;
   >
   >   right: 1rem;
   >
   > }
