
// const a = 10;
// const b = 87;
// if (a - b === 7) {
//   console.log(1);
// } else if (b - a === 7) {
//   console.log(2);
// } else if (a === b) {
//   console.log(3);
// } else if (b / a === 7) {
//   console.log(4);
// } else if ((b - a) % 7 === 0) {
//   console.log(5);
// } else {
//   console.log(100);
// }

// x = "123456";
// try {
//   if (x == "") {
//     throw "empty";
//   }
//   if (isNaN(x)) {
//     throw "not a num";
//   }
//   x = Number(x);
//   if (x < 5) {
//     throw "to0 low";
//   }
//   if (x > 10) {
//     throw "to0 high";
//   }
// } catch (error) {
//   console.log("error is ", error);
// } finally {
//   console.log("execute", x);
// }

const a = new Map([
    ["mark", 2003],
    ["anita", 2001],
    ["JOHN", 2010],
    ["Mary", 2010],
    ["BOB", 2009],
    ["ben", 2007],
  ]);
  
  a.set("bob", 2008);
  a.set("BEN", 2009);
  
  console.log(a.get("Mary"), "j");
  console.log(a.has("JOHN"));
  console.log(a.delete("anita"));
  console.log(a);