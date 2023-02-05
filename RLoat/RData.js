// from keno platform use developer tool and run the below codes one by one

// First Codes..
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

// Second Codes . .
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

// Third Codes . . .
var st = btoa(JSON.stringify(arr));

var res = atob(st);
