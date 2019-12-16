// To print odd numbers in an array

function oddarray(a) {
  var arr = []
  for (var i = 1; i < a; i++) {
    if (i%2 !== 0) {
      arr.push(i);
    }
}
console.log(arr);
}
//var a = 10;
//oddarray(a);

//--------------------------------------------------------------

// To print sum of all numbers in an array

function sumarray(a) {
  var sum = 0;
  len = a.length;
  for (var i = 0; i < len; i++) {
    sum = sum + a[i];
  }
  console.log(sum);
}
//var b = [3,3,3,3,3];
//sumarray(b);

//-----------------------------------------------------------------

// To print prime numbers in an array

function primearray(a){
  var arr = [];
  for (var i = 1; i <= a; i++) {
    var count = 0;
    for (var j = 1; j <= i; j++) {
      if(i%j == 0){
        count = count + 1;
      }
      }
      if(count === 2){
        arr.push(i);
    }
  }
  console.log(arr);
}

//primearray(10);

//---------------------------------------------------------------

// Program to print odd numbers in a given array

function givenodd(a) {
  var odd = [];
  len = a.length;
  for (var i = 0; i < len; i++) {
    if(a[i]%2 !== 0){
      odd.push(a[i]);
    }
  }
  console.log(odd);
}
//var a = [1,2,3,4,5,6,7,8,9];
//givenodd(a);

//-------------------------------------------------------

// Program to print palindromes in an array

function palindromes(a){
var palin = [];
var npalin = [];
var len = a.length;
for (var i = 0; i < len; i++) {
  len2 = a[i].length;
  var mid = Math.floor(len2/2);
  for (var j = 0; j < mid; j++) {
    if (a[i][j] !== a[i][len2-1-j]) {
      npalin.push(a[i]);
      break
    }else {
      palin.push(a[i]);
      break
    }
  }
}
console.log("Palindrome: ",palin);
console.log("Not Palindrome: ",npalin);

}
var a = ["malayalam","ajay","dad","mom","rotor",]
palindromes(a);

//---------------------------------------------------------

// Program to change lower to upper case of all string in array

var array2 = ["hgdh","ndsndjsd","dsbsjd","dsjdjd","dskdhd"];
array2 = array2.map(function(x){
    return x.toUpperCase();
})

//syntax:array.map(function(currentValue, index, arr), thisValue)


//------------------------------------------------------------

// Program to
