var obj = { name: "rajinikanth", age: 78, idustry: "tamil" };
function convertListToObject(obj) {
    var array1 = [];
    var i = 0;
    for (var a in obj) {
        array1[i] = a;
        array1[i + 1] = obj[a];
        i = i + 2;
    }
    console.log(array1);
}
convertListToObject(obj);
