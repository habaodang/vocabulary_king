function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function getData() {
  return fetch("/getwordenglish")
    .then((response) => response.json())
    .then((data) => {
      cauHoi = data.ques;
      dapAn = data.answer;
      return { cauHoi, dapAn };
    });
}

function showQues(ques) {
  document.querySelector(".question").textContent = ques;
}

function showAnswer() {
  getData().then(async ({ cauHoi, dapAn }) => {
    showQues(cauHoi);
    document
      .querySelector(".button_show")
      .addEventListener("click", function () {
        document.querySelector(".result").textContent = dapAn;
        document.querySelector(".result").style.display = "block";
      });
  });
}

function nextGame() {
  document.querySelector(".result").style.display = "none";
  showAnswer();
}
showAnswer();
