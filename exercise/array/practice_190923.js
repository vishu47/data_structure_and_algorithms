// ! Find the Union and Intersection of the two sorted arrays
// Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the
// union between these two arrays.

// Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
// If there are repetitions, then only one occurrence of element should be printed in the union.

// const FindUnion = (a, n, b, m) => {
//   let newArr = [];
//   for (let i = 0; i <= n - 1; i++) {
//     if (newArr.indexOf(a[i]) === -1) {
//       newArr.push(a[i]);
//     }
//   }
//   for (let i = 0; i <= m - 1; i++) {
//     if (newArr.indexOf(a[i]) === -1) {
//       newArr.push(b[i]);
//     }
//   }
//   console.log(' number of elements in the union between these two arrays are ' + newArr.length);
// };

// using set methon becouse set did not store duplicate value
const FindUnion = (a, n, b, m) => {
  let newArr = [];
  let set = new Set();
  for (let i = 0; i <= n - 1; i++) {
    set.add(a[i]);
  }
  for (let i = 0; i <= m - 1; i++) {
    set.add(b[i]);
  }
  console.log(
    " number of elements in the union between these two arrays are " + set.size
  );
};

let arr1 = [1, 2, 3, 4, 5, 3];
let arr2 = [1, 2, 3];
// FindUnion(arr1, arr1.length, arr2, arr2.length);

// ! Given an array, rotate the array by one position in clock-wise direction.

const RotateArr = (arr, n) => {
  const set = new Set();
  let last;
  for (let i = n - 1; i >= 0; i--) {
    console.log(arr[i]);
    if (i === n - 1) {
      last = arr[i];
    }
    arr[i] = arr[i - 1];
    console.log(arr[i]);
  }
  arr[0] = last;
  return arr;
};

// let arr = [1, 2, 3, 4, 5];
// let n = arr.length;
// RotateArr(arr, n);

// ! Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

const MissingNumber = (arr, n) => {
  let total = 0;
  // mathmatical formula sum of all natural number based on array length
  const sum = (n * (n + 1)) / 2;

  for (let i = 0; i < arr.length; i++) {
    total += arr[i];
  }

  const mising = sum - total;
  
  return mising;
};

// let arr = [1, 2, 3, 5, 6, 7];
// let n = 7;
// const output = MissingNumber(arr, n);
// console.log(output);

// ! Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

const PairSum = (a, num) => {
  let total = 0;
  for (let i = 0; i < a.length; i++) {
    for (let j = i + 1; j < a.length; j++) {
      if (a[i] + a[j] === num) {
        total++;
      }
    }
  }
  return total;
};

let arr = [1, 1, 1, 1];
let givenSum = 2;
const output = PairSum(arr, givenSum);
console.log(output);
