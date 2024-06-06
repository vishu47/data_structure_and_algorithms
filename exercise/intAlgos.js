// const ReversedString = (str) => {
//   let reversed = "";
//   for (let i = 0; i < str.length; i++) {
//     reversed = str[i] + reversed;
//   }
//   return reversed;
// };
// const ReversedString = (str) => {
//   let reversed = "";
//   for (char of str) {
//     reversed = char + reversed;
//   }
//   return reversed;
// };
const ReversedString = (str) => {
  return str.split("").reverse().join("");
};

// console.log(ReversedString("hi"));
// console.log(ReversedString("vishnu"));
// console.log(ReversedString("maurya"));

const maxChar = (str) => {
  // when we loop over array we use of
  // when we loop over object we use in
  let obj = {};
  let maxChar = 0;
  let chare = "";

  for (let char of str) {
    if (obj[char]) {
      obj[char] = obj[char] + 1;
    } else {
      obj[char] = 1;
    }
  }
  console.log(obj);
  for (key in obj) {
    if (obj[key] > maxChar) {
      maxChar = obj[key];
      chare = key;
    }
  }
  console.log(maxChar, chare);
};

console.log(maxChar("dwdddddddddddmm"));
console.log(maxChar("vbvvbvbvbbvbvbv"));
console.log(maxChar("iooiiiiiiiooooo"));
