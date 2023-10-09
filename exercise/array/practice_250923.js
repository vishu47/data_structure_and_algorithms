// // ! Given an array arr[] of size n, find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

// // Note:- The position you return should be according to 1-based indexing.

// const firstRepeated = (arr, n) => {
//   for (let i = 0; i < n; i++) {
//     for (let j = i + 1; j < n; j++) {
//       if (arr[i] === arr[j]) {
//         return i + 1;
//       }
//     }
//   }
//   return -1;
// };

// // const arr = [1, 5, 3, 4, 3, 5, 6];
// // const n = arr.length;
// // const output = firstRepeated(arr, n);
// // console.log(output);

// const findMaxSum = (arr, n) => {
//   // code here not mutch efficient
//   // let ev = 0;
//   // let evAr = [];
//   // let od = 0;
//   // let odAr = [];
//   // for (let i = 0; i < n; i++) {
//   //   console.log(i % 2 === 0);
//   //   if (i % 2 === 0) {
//   //     if(arr[i])
//   //     ev += arr[i];
//   //     evAr.push(i);
//   //   } else {
//   //     od += arr[i];
//   //     odAr.push(i);
//   //   }
//   // }
//   // console.log(ev, evAr, od, odAr);
//   // if (ev > od) {
//   //   return ev;
//   // } else {
//   //   return od;
//   // }

//   console.log(new Array(n));
// };

// const arr = [9, 4, 11, 12, 6, 12];
// const n = arr.length;
// const output = findMaxSum(arr, n);
// console.log(output);

