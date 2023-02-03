// let button = document.getElementById("resultloader");
// var length = 0;
// html = {};
// let count = 0;
// let relo = setInterval(() => {
//   button.click();
//   count = count + 1;
//   print(count);
//   if (count > 3500) {
//     let data = document.getElementsByClassName("resultnum_div");
//     html = { object: data };
//     clearInterval(relo);
//   }
// }, 10);

let button = document.getElementById("resultloader");
let leng = 0;
let htmlObject = { html: "" };
let ct = 0;
// const div = document.querySelector("div");
// let bool = true;

//while (true) {
// bool = div.classList.contains("show undefined");
const stopIt = (past, present) => {
  if (past == present) {
    clearInterval(relu);
  }
};
let present = 0;
let relu = setInterval(() => {
  button.click();
  // document.getElementsByClassName("resultnum_div").length;
  console.clear();
  console.log(document.getElementsByClassName("resultnum_div").length);
}, 10);
// if (past == present) {
//   console.log("The data loading ends ..");
//   console.log("Total Data:", ct);
//   break;
// } else {
//   present += 5;
//   console.clear();
//   console.log(present);
//   console.log(past);
// }
// ct += 1;
//}
// htmlObject["html"] = document.getElementsByClassName("resultnum_div");
// leng = document.getElementsByClassName("resultnum_div").length;
// let arr = [];
// for (let i = 0; i < leng; i++) {
//   arr.push(document.getElementsByClassName("resultnum_div")[i].innerHTML);
// }

// mainElement will be an array of results
// var mainElement = document.getElementsByClassName("resultnum_div");
// let date = mainElement[1].children[0].firstElementChild.firstChild.data;
// let firstNum_Set = mainElement[1].children[1].childNodes[2].innerHTML;
// firstNum_Set = firstNum_Set.replaceAll("</li><li>", ",");
// firstNum_Set = firstNum_Set.replace("<li>", "");
// firstNum_Set = firstNum_Set.replace("</li>", "");
// firstNum_Set = firstNum_Set.split(",");
// let secNum_Set = mainElement[1].children[1].childNodes[3].innerHTML;
// secNum_Set = secNum_Set.replaceAll("</li><li>", ",");
// secNum_Set = secNum_Set.replace("<li>", "");
// secNum_Set = secNum_Set.replace("</li>", "");
// secNum_Set = secNum_Set.split(",");

// var obj = { Date: date, fSet: firstNum_Set, sSet: secNum_Set };

var bt = document.getElementById("resultloader");
var prev = document.getElementsByClassName("resultnum_div").length;
var val = 0;
var rel = setInterval(() => {
  val = document.getElementsByClassName("resultnum_div").length;
  var stop = document.getElementById("snackbar").innerHTML;
  bt.click();
  console.clear();
  console.log(val);
  console.log(stop);
  if (stop != "") {
    clearInterval(rel);
  }
}, 1000);

var arr = [];
var mainElement = document.getElementsByClassName("resultnum_div");

for (let i = 0; i < mainElement.length; i++) {
  let date = mainElement[i].children[0].firstElementChild.firstChild.data;
  let firstNum_Set = mainElement[i].children[1].childNodes[2].innerHTML;
  firstNum_Set = firstNum_Set.replaceAll("</li><li>", ",");
  firstNum_Set = firstNum_Set.replace("<li>", "");
  firstNum_Set = firstNum_Set.replace("</li>", "");
  firstNum_Set = firstNum_Set.split(",");
  let secNum_Set = mainElement[i].children[1].childNodes[3].innerHTML;
  secNum_Set = secNum_Set.replaceAll("</li><li>", ",");
  secNum_Set = secNum_Set.replace("<li>", "");
  secNum_Set = secNum_Set.replace("</li>", "");
  secNum_Set = secNum_Set.split(",");
  var obj = { Date: date, fSet: firstNum_Set, sSet: secNum_Set };
  arr.push(obj);
}

var st = btoa(JSON.stringify(arr));

var res = atob(st);

let json = atob("W29iamVjdCBPYmplY3Rd");
