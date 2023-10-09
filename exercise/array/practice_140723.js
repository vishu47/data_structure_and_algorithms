// ! Find a peak element which is not smaller than its neighbours
// ? Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors.
// ? Note: For corner elements, we need to consider only one neighbor.

// const FindPeakElement = (arr) => {
//   const l = arr.length;
//   console.log(l - 1);
//   if (l === 0)
//     return console.log(`peak element ${arr[0]} at index ${1}`);
//   if (arr[l - 1] > arr[l - 2])
//     return console.log(`peak element ${arr[l - 1]} at index ${l - 1}`);

//   for (let i = 1; i < l - 1; i++) {
//     if (arr[i] > arr[i + 1] && arr[i] > arr[i - 1]) {
//       console.log(`peak element ${arr[i]} at index ${i}`);
//     }
//   }
// };
// // Time complexity: O(n), One traversal is needed so the time complexity is O(n)
// const arr = [5, 10, 10, 15];
// FindPeakElement(arr);

// ! Move all negative numbers to beginning and positive to end with constant extra space
// ? An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
// order will change with below approch


// const RearrangeArray = (arr) => {
//   const l = arr.length;
//   const arrm = [...arr];
//   console.log(arrm);
//   let pos = l;
//   let neg = 0;
//   for (let i = 0; i < l; i++) {
//     console.log(arr[i], pos, neg);
//     if (arr[i] <= 0) {
//       arrm[neg] = arr[i];
//       neg++;
//     } else {
//       arrm[pos - 1] = arr[i];
//       pos--;
//     }
//   }
//   console.log(arrm);
// };

// with sorting order will change
// const RearrangeArray = (arr) => {
//   const sort = arr.sort((a, b) => a - b);
//   console.log(sort)
// };

// const arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6];
// RearrangeArray(arr);
