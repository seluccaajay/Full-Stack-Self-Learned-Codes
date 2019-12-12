function getnelement(a,b) {
  len = a.length
  if(len===0){
    return undefined
  }else if (len>0) {
    return a[b]
  }
}
var a=[1,2,3,4,5,6,7,8,9,10,11];
b = prompt("Enter the number: ");
alert("The value is: "+getnelement(a,b));
console.log(getnelement(a,b));
