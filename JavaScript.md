# 자바스크립트 (JavaScript)

- 브라우저를 조작하기 위한 유일한 언어
- 브라우저 화면을 '동적'으로 만들기 위함
- 실행 순서
  - 위에서 아래로 실행함.
- 인터프리터와 컴파일러
  - 인터프리터 - 별도의 변환 없이 그대로 컴퓨터가 처리
  - 컴파일러 - 기계언어로 변환하여 그 결과를 컴퓨터가 실행.
  - 자바스크립트는 인터프리터를 사용하는 언어

- 내부 스크립트는 그대로 작성하면되고, 외부 스크립트는 .js 파일을 만들고, 내부 스크립트 안에 <script src="~~.js" defer></script> 작성
-  async 와 defer
  - async - 다수의 백그라운드 스크립트를 최대한 빠르게 불러와야 할 때 사용 실행 순서 보장 X
  - defer - 페이지에 나타난 순서 그대로 불러옴. 페이지 콘텐츠와 위쪽 스크립트 로딩이 끝나면 실행. 실행 순서 보장 O.

- 주석
  - 1줄 짜리 주석은 // 로 작성
  - 여러 줄 주석은 /* 여기에 작성 */


## DOM 조작

- 문서(HTML) 조작

  ```html
  console.log(~) - 콘솔 창에 들어감
  alert(~) - 팝업 창
  <body>
    <script>
      조작하는 영역
      const title = document.createElement('h1') - title 이라는 변수에 h1태그 추가
      title.innerText = 'JS 기초' - 텍스트 추가 h1태그에 JS 기초 라는 text 추가
      const body = document.querySelector('body') - body 라는 변수에 body 태그 정보를 저장
      body.appendChild(title) body 라는 변수 (body 태그 정보) 에 자식요소로 title을 넣어줌
    </script>
  </body>
  ```

- const, let 차이

  ```html
  const a = 1
  a = 2 - 실행 불가. 할당시 변경 불가능 (재할당이 가능한 경우는 할당한 것의 속성을 바꿀때 재할당 가능)
  let b = 1
  b = 2 - 가능
  ```

- getElement, getElements 는 보통 1개만 있는 id 같은 것들을 불러올때는 t 여러개 존재 가능한 것들은 ts

- innerHTML 은 보안에 취약하기 때문에 사용하지 않는 것이 좋음.

  ```html
  remove - 삭제
  body.removeChild(a) - body의 자식중에 a를 지운다.
  a.setAttribute('href', 'https://~~~~') - 속성을 지정할 수 있음. -재할당 가능
  a.getAttribute('href') - 'https://~~~~'
  h1.classList = h1 클래스에 있는걸 리스트로 받아옴
  Toggle = 스위치 같은 기능
  addEventListener('click', function() {
  	클릭하면 일어나는 행동을 지정
  	h1.classList.toggle('blue')
  	})
  ```

- 실행 순서
  - 위에서 아래로 실행함.



## 조건문



#### if 문

- if, else if (파이썬에 elif 와 같은 역할), else 로 3가지로 쓸 수 있음.

  > if (i > 0) {
  >
  >  내용
  >
  > }
  >
  > else {
  >
  >  내용
  >
  > }

#### for 문

- for (let i = 0; i < 50; i++) {} = for i in range(50) 과 같음 특정 숫자 만큼 증가하고 싶을 땐,

  > for (let i = 0; i < 50; i += 3) {} 과 같이 사용 하면 됨.

#### while 문

- 파이썬 while문과 비슷하게 사용가능. while (조건)

  > while (i != 0) {
  >
  >   i -= 1
  >
  > }



## 함수

- 함수 선언은 function 임시함수명 () { 내용 }

- sort

  - numbers.sort((a, b) => a - b); // 오름차순

  - numbers.sort((a, b) => b - a); // 내림차순

    > 여기서 => 는 임시 함수 마치 lambda 같은 기능인 듯?

- String(숫자) - 숫자를 문자열로 바꿔줌. 문자열.indexOf('찾을문자')
  - 있으면 인덱스를 반환
  - 없으면 -1을 반환
- concat('더할문자' or 숫자) 문자열에 다른걸 붙일때 사용

