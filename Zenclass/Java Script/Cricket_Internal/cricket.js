let score = 0;
let counter = 0;
let counter2 = 0;
let over1=[];
let over2=[];
let over3=[];
let over4=[];
let over5=[];
let over6=[];
function  startmatch(){
   if(counter<18){
   counter=counter+1;     

   let run = Math.ceil(Math.random()*6);
   score = score + run;
   document.getElementById("scoreone").innerHTML=run;
   document.getElementById("totalone").innerHTML=score;
   if(counter<=6){
     over1.push(run);
   }
   if(counter>6 && counter<=12){
     over2.push(run);
   }
   if(counter>12 && counter<=18){
     over3.push(run);
   }
   
   
localStorage.firstover=over1;
localStorage.secondover=over2;
localStorage.thirdover=over3;
 }
 else{
   alert("Your 3 overs has been completed");
 }
}
let score2 = 0;
function  match(){
   if(counter2<19){
   let run2= Math.ceil(Math.random()*6);
   score2 = score2 + run2;
    document.getElementById("scoretwo").innerHTML=run2;
    document.getElementById("totaltwo").innerHTML=score2;
    if(counter2<6){
      over4.push(run2);
    }
    if(counter2>6 && counter2<=12){
      over5.push(run2);
    }
    if(counter2>12 && counter2<=18){
      over6.push(run2);
    }
    counter2 = counter2+1;
  }
  else{
    alert("Your 3 overs has been completed");
  }
localStorage.fourthover=over4;
localStorage.fifthover=over5;
localStorage.sixthover=over6;
}

function winner(){
  let o1 = localStorage.getItem("firstover");
  let o2 = localStorage.getItem("secondover");
  let o3 = localStorage.getItem("thirdover");
  document.getElementById("over1").innerHTML=o1;
  document.getElementById("over2").innerHTML=o2;
  document.getElementById("over3").innerHTML=o3;
}
function winner2(){
  let o4 = localStorage.getItem("fourthover");
  let o5 = localStorage.getItem("fifthover");
  let o6 = localStorage.getItem("sixthover");
  document.getElementById("over4").innerHTML=o4;
  document.getElementById("over5").innerHTML=o5;
  document.getElementById("over6").innerHTML=o6;
}
function result(){
  
}
console.log(over1);
console.log(over2);
console.log(over3);
console.log(over4);
console.log(over5);
console.log(over6);
