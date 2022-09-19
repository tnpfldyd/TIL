// 인풋하면 작성하기
const body = document.querySelector('body');
const input = document.createElement('input');
input.setAttribute('id', '아이디');
const input_copy = document.createElement('p');
input_copy.setAttribute('id', 'copy');
body.appendChild(input);
body.appendChild(input_copy);
input.addEventListener('input', function() {
    const copy = input.value;
    input_copy.innerText = copy;
});
// 버튼 누르면 모달 띄우기
const btn1 = document.createElement('button');
btn1.innerText = '클릭'
body.appendChild(btn1);
const div = document.createElement('div');
const h2 = document.createElement('h2');
const modal_btn = document.createElement('button');
modal_btn.innerText = '닫기'
div.style.backgroundColor = 'rgba(0,0,0,0.7)';
div.style.position = 'fixed';
div.style.height = '100vh';
div.style.width = '100%';
div.style.top = '0';
div.style.left = '0';
div.style.display = 'none';
div.style.justifyContent = 'center';
div.style.alignItems = 'center';
h2.innerText = '모달';
h2.style.color = 'white';
body.appendChild(div);
div.appendChild(h2);
div.appendChild(modal_btn);
btn1.addEventListener('click', function() {
    div.style.display = 'flex';
});
modal_btn.addEventListener('click', function() {
    div.style.display = 'none';
});
div.addEventListener('click', function() {
    div.style.display = 'none';
});
// carousel 만들기.. 자바안에서 이펙트는 어떻게하는지 아직 미지수..
const carousel = document.createElement('div');
carousel.className = 'carousel-items';
carousel.style.position = 'relative';
carousel.style.display = 'flex';
carousel.style.width = '10rem';
carousel.style.height = '10rem';
carousel.style.overflow = 'hidden';
body.appendChild(carousel)
const carou1 = document.createElement('div');
carou1.className = 'carousel-item';
const carou2 = document.createElement('div');
carou2.className = 'carousel-item';
const carou3 = document.createElement('div');
carou3.className = 'carousel-item';
const carou4 = document.createElement('div');
carou4.className = 'carousel-item';
const carou5 = document.createElement('div');
carou5.className = 'carousel-item';
carousel.appendChild(carou1);
carousel.appendChild(carou2);
carousel.appendChild(carou3);
carousel.appendChild(carou4);
carousel.appendChild(carou5); 
const carousel_item = document.querySelectorAll('.carousel-item');
for (let i = 0; i<carousel_item.length; i++) {
    carousel_item[i].style.position = 'absolute';
    carousel_item[i].style.top = '0';
    carousel_item[i].style.width = '10rem';
    carousel_item[i].style.height = '10rem';
    carousel_item[i].style.backgroundColor = 'bisque';
    carousel_item[i].style.display = 'none';
    carousel_item[i].innerText = String(i+1)+'번';
};
carousel_item[0].style.display = 'block';
const btn_box = document.createElement('div');
const previous_btn = document.createElement('button');
const next_btn = document.createElement('button');
btn_box.style.display = 'flex';
previous_btn.innerText = 'previous';    
next_btn.innerText = 'next';
body.appendChild(btn_box);
btn_box.appendChild(previous_btn);
btn_box.appendChild(next_btn);
let cnt = 0
next_btn.addEventListener('click', function() {
    carousel_item[cnt%5].style.display = 'none';

    cnt += 1;
    carousel_item[cnt%5].style.display = 'block';
});

previous_btn.addEventListener('click', function() {
    carousel_item[cnt%5].style.display = 'none';
    cnt -= 1;
    if (cnt === -1) {
        cnt = 4
    }
    carousel_item[cnt%5].style.display = 'block';
});
// 비밀번호 확인하기
const password_box = document.createElement('div');
const p1 = document.createElement('p');
const password1 = document.createElement('input');
body.appendChild(password_box);
password_box.appendChild(p1);
password_box.appendChild(password1);
p1.innerText = '비밀번호';
password1.type = 'password';
const p2 = document.createElement('p');
const password2 = document.createElement('input');
body.appendChild(password_box);
password_box.appendChild(p2);
password_box.appendChild(password2);
p2.innerText = '비밀번호 확인';
password2.type = 'password';
const submit = document.createElement('button');
submit.innerText = '가입 신청'
body.appendChild(submit);
submit.addEventListener('click', function() {
    if (password1.value.length<8 || password2.value.length<8) {
        alert('비밀번호는 8자 이상이어야 합니다.')
    }
    else {
        if (password1.value !== password2.value) {
            alert('비밀번호가 다릅니다.')
        }
        else {
            alert('가입 성공!')
        }
    }
})