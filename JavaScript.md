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

- for in 배열은 인덱스 출력, 객체(딕셔너리)는 키 값을 보여줌

- for of 배열은 하나 하나 출력, 객체(딕셔너리)는 오류남

  > 리스트의 인덱스를 뽑아야 할 땐 for in을 쓰고 배열을 하나 씩 뽑아야 할땐 for of 를 쓰고, 딕셔너리를 사용 할 땐 for in !

  ```javascript
  const num = [1, 2, 3, 4, 5]
  for (let i of num) {
      console.log(i)
  }
  1
  2
  3
  4
  5
  - 요소
  for (let i in num) {
      console.log(i)
  }
  0
  1
  2
  3
  4
  - 인덱스
  ```

  

#### while 문

- 파이썬 while문과 비슷하게 사용가능. while (조건)

  > while (i != 0) {
  >
  >   i -= 1
  >
  > }

#### 3항 연산자

- true ? 1 : 2 = 1

- false ? 1 : 2 = 2

  > true 일땐 앞에 조건 출력 false 일땐 뒤의 조건 출력

#### switch 문

- switch (변수) {

case '비교값' : {

실행할 행동
break
}

default: {

실행할 행동
}
}

- switch 문에서는 break를 만나거나 default 까지 갈 때가지 멈추지 않음

#### do while 문

- 테스트 조건이 거짓으로 평가 될 때 까지 지정된 구문을 실행함.
- 구문이 실행 한 뒤에 테스트 조건을 평가함으로 while (i < 5) 조건일 때 실행 된 뒤에 5가 거짓으로 판명나면 멈추니 "12345" 라는 숫자가 들어가는 것.

```javascript
let result = '';
let i = 0;
do {
    i = i + 1;
    result = result + i;
} while (i < 5);
console.log(result);
// "12345"
```







## 함수

- 함수 선언은 function 임시함수명 () { 내용 }

- sort

  - numbers.sort((a, b) => a - b); // 오름차순

  - numbers.sort((a, b) => b - a); // 내림차순

    > 여기서 => 는 임시 함수 마치 lambda 같은 기능인 듯?

- String(숫자) - 숫자를 문자열로 바꿔줌.
  - [...String(10)] = ['1', '0'] 

- 문자열.indexOf('찾을문자')

  - 있으면 인덱스를 반환
  - 없으면 -1을 반환

- Number(문자열숫자) - 문자열인 숫자를 인트형으로 바꿔줌

- concat('더할문자' or 숫자) 문자열에 다른걸 붙일때 사용

- length = 길이 

  > 예) const name = "rarara"
  >
  > console.log(name.length) = 6

- const name = function (변수) {} 로도 가능

  > 자바에서는 ()에서 갯수 보다 더 많이, 적게 넣어도 가능
  >
  > (1,2, ...변수) 이렇게 선언 뒤에 값을 1, 2, 3, 4, 5 를 넣으면 [1, 2, [3, 4, 5]] 로 넣어줌
  >
  > num = [1, 2, 3];
  >
  > 하면 function(...num) 알아서 들어감

- 함수 표현식, 선언식

  - 표현식은 식 위에선 호이스팅 X
  - 선언식은 호이스팅 O

- 화살표 함수

  - const name = name => 'hello, ${name}'


```javascript
const fruits = ['딸기', '바나나', '멜론']
fruits.forEach(function(fruit) {
    console.log(fruit)
})
fruits.forEach(fruit => console.log(fruit))
forEach(function(요소, 인덱스, 배열))
```

- filter = 해당하는 것만 출력
- 함수 종류

```javascript
숫자배열.reduce((acc, num) => {
    return acc + num
}, 0) - 합계 구하는 함수
const me = {
    name: 'tak',
    getName: funtion() {
    return this.name
}
}
```





## 변수 선언

- 변수 선언은 var, const, let 3가지 방법으로 가능.

  - var
    - 재선언, 재할당 둘 다 가능
    - var는 호이스팅이 가능하기 때문에(?) 예상치 못한 오류가 발생 될 수 있다.
    - 특별한 경우를 제외하고는 const, let 둘 중 하나를 사용하도록
  - const
    - 재선언 불가능
    - 재할당 불가능
  - let
    - 재선언 불가능
    - 재할당 가능

- var 혹은 let을 사용하여 선언된 변수는 undefined 의 값을 가진다.

  - undefined 는 불리언 맥락에서 사용 될 때 false로 동작함.

    > var myArray = [];
    >
    > if (!myArray[0]) myFunction();
    >
    > myArray[0] 이 false 이므로 myFunction 함수 작동

  - undifined 값은 수치 맥락에서 사용될 때 NaN 으로 변경

    > var a;
    >
    > a = a + 2;
    >
    > console.log(a) = NaN

  - null 값을 평가할 때, 수치 맥락에서는 0으로, 불리언 맥락에서는 false로 작동함.

    > var n = null;
    >
    > console.log(n + 5); == 5
    >
    > console.log(n * 32); == 0



## Array

```javascript
let fruits = ['사과', '바나나']
console.log(fruits.length) - 2

let first = fruits[0] - 사과
let last = fruits[fruits.length - 1] - 바나나

fruits.forEach(function (item, index, array) {
    console.log(item, index)
})
사과 0
바나나 1

fruits.push('오렌지') - ["사과", "바나나", "오렌지"]
fruits.pop() - ["사과", "바나나"]
fruits.shift() - ["바나나"]
fruits.unshift('딸기') - ["딸기", "바나나"]
fruits.push('망고') - ["딸기", "바나나", "망고"]
let pos = fruits.indexOf("바나나") - 1
fruits.splice(pos, 1) - ["딸기", "망고"] pos 는 시작 인덱스 1은 시작 인덱스부터 몇 개를 지울 건지를 뜻함.

```



## 이 외

> '${변수} 문자열 ${변수}' 로 사용 가능.

- null 은 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

- 자바는 === 로 비교

  - == 는 동등 비교

    > 5 == '5' 같을 때는 오류가 날 수도 ..?

  - === 는 완전 일치

- && = and , || = or, ! = not
- 배열.join() - join은 배열의 메서드
