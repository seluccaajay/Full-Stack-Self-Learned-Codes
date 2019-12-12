function removeProperty(obj1, key) {
  delete obj1[key];
  return obj1[key];
}
var obj1 = {
  name: 'Sam',
  age: 20
};

console.log(removeProperty(obj1, 'name'));
