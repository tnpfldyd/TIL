// const names = ['아라리', '우루루', '카이야']
// names.forEach(function(nana) {
//     const name = name => `Hello! ${name}` //name 이라는 함수
//     console.log(name(nana))
// })
// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
// console.log(numbers.reduce((acc, num) => {
//     return acc + num
// }, 0))
// const me = {
//     name: 'tak',
//     first_name: 'kim',
//     getName: function() {
//         return this.first_name + this.name
//     }
// }
// console.log(me.getName())
// for (let i in me) {
//     console.log(i)
// }
// for (let i of numbers) {
//     console.log(i)
// }
// for (let i = 1; i < 50; i ++) {
//     cnt = 0
//     let k = ''
//     i = [...String(i)]
//     i.forEach(function(ni) {
//         if (ni === '3' || ni === '6' || ni === '9') {
//             cnt += 1    
//         }
//         k += ni
//     });
//     i = Number(k)
//     if (cnt === 0) {
//         console.log(i)
//     }
//     else if (cnt === 1) {
//         console.log('X')
//     }
//     else {
//         console.log('XX')
//     }
// }
// const newInput = document.createElement("input");
// newInput.setAttribute("id", "아이디");
// newInput.setAttribute("onkeyup", "printing()");
// const body = document.querySelector('body');
// const pnt = document.createElement("h1");
// pnt.setAttribute("id", "pnt")
// body.appendChild(newInput);
// body.appendChild(pnt);
// function printing() {
//     const Input = document.getElementById("아이디").value;
//     document.getElementById("pnt").innerText = Input;
// }
// const name = 'mozilla';
// console.log(name.length)
// let fruits = "사과"
// switch (fruits) {
//     case "오렌지":
//         console.log("오렌지~~~~~~~")
//         break
//     case "사과":
//         console.log("사과~~~~~~")
//         break
//     default:
//         console.log("sorry")
// }