class Jstasks{
    odd(x) {
    if(x%2!==0)
    return true;
    }
    Prime(x){
        for(let i=2;i<x;i++){
            if(x%i==0)
            {
                return false;
            }
            else{
                return true;
            }
        }
    }
    sumofarray(list){
      return  list.reduce((a,b)=>(a+b));
    }
    pallindrome(string){
        let arraylist=[]
        for(let i=0;i<string.length;i++)
        {
            arraylist.push(string[i]);
        }
        arraylist=arraylist.reverse();
        let string2=arraylist.join('');
        if(string===string2)
        return true;
        else
        return  false;
    }
    toupper(string)
    {

        return string.toUpperCase();   
    }
}


const x=new Jstasks;
if(x.odd(5))
console.log("number is odd");
if(x.Prime(7))
console.log("number is prime number");
list=[1,2,3,4,5,6,6,7,8,8,9];
y=x.sumofarray(list);
console.log(y);
list2=['ajay','mom']
list2=list2.filter(a=>x.pallindrome(a));
console.log("pallindrome",list2)
list3=['sdfsf','sdfsdfwdfsdfsdf']
function toupper(string)
{

    return string.toUpperCase();   
}
list3=list3.map(a=>x.toupper(a));
console.log("toupper",list3);