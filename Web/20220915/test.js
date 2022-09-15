const title = document.createElement('h1');
title.innerText = 'JS 기초';
const body = document.querySelector('body');
body.appendChild(title);
const h2 = document.createElement('h2');
h2.innerText = '1부터 10까지 시작 '
for (let i = 1; i < 11; i++) {
  if (i != 10) {
    h2.innerText = h2.innerText.concat(i, ', ');
  }
  else {
    h2.innerText = h2.innerText.concat(i);
  }
}
const btn = document.createElement('button');
btn.innerText = '로또 번호 생성';
body.appendChild(h2);
body.appendChild(btn);
const game = document.createElement('h2');
game.innerText = '3,6,9 게임 시작 '
for (let i = 1; i < 51; i++) {
  if (i == 50) {
    game.innerText = game.innerText.concat(i);
  }
  else {
    let k = 0;
    for (let cnt = 3; cnt < 10; cnt += 3) {
      let search = String(i).indexOf(String(cnt))
      if (search != -1) {
        k += 1
      }
      while (search != -1) {
        search = String(i).indexOf(String(cnt), search + 1);
        if (search != -1) {
          k += 1
        }
      }
    }
    if (k == 0) {
      game.innerText = game.innerText.concat(i, ',');
    }
    else if (k > 1) {
      game.innerText = game.innerText.concat('XX', ',')
    }
    else {
      game.innerText = game.innerText.concat('X', ',')
    }
  }
}
body.appendChild(game);
document.addEventListener('DOMContentLoaded', () => {
    function createParagraph() {
      const lotto = [];
      while (lotto.length < 6) {
        const num = parseInt(Math.random() * 45 + 1);
        if (lotto.indexOf(num) == -1) {
          lotto.push(num);
        }
      }
      lotto.sort((a,b)=>a-b);
      const para = document.createElement('h2');
      para.textContent = lotto;
      document.body.appendChild(para);
    }
  
    const button = document.querySelector('button');
    button.addEventListener('click', createParagraph);
  });
