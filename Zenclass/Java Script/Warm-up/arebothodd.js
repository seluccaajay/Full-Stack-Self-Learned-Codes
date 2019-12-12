function areBothOdd(a,b) {
  yes = "Both are odd"
  no = "Either number is not odd"
  if((a%2 !== 0) && (b%2 !== 0)){
    return yes;
  }else {
    return no;
  }
}

var c = 3;
var d = 5;
console.log(areBothOdd(c,d));
