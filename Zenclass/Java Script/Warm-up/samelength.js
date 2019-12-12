function samelength(str1,str2) {
  len1 = str1.length
  len2 = str2.length
  if(len1 === len2){
    return "Both lengths are equal";
  }else {
    return "Both lengths are not equal"
  }
}
a = prompt("Enter String 1: ");
b = prompt("Enter string 2: ");
console.log(samelength(a,b));
