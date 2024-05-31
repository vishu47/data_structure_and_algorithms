// Given an array arr[] of size n and an integer x,
// return 1 if there exists a pair of elements in the
// array whose absolute difference is x, otherwise, return -1.

function findPair(n, x, arr) {
  const st = new Set();
  for (let i = 0; i < n; i++) {
    if (st.has(arr[i] - x) || st.has(arr[i] + x)) {
      return 1;
    }
    st.add(arr[i]);
  }
  return -1;
}
// console.log(findPair(10, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));

// Given a sorted array arr[] of positive integers. The task is to find the
// closest value in the array to the given number k. The array may contain duplicate values.

// Note: If the difference with k is the same for two values in the array
// sreturn the greater value.

function findClosest(n, k, arr) {
  let res = 0;
  let mp = new Map();
  let min = Number.MAX_SAFE_INTEGER;
  for (let i = 0; i < n; i++) {
    min = Math.min(min, Math.abs(arr[i] - k));
    mp.set(arr[i], Math.abs(arr[i] - k));
  }
  for (let i = 0; i < n; i++) {
    if (mp.get(arr[i]) === min) {
      res = arr[i];
    }
  }
  return res;
}

console.log(findClosest(7, 4, [1, 2, 3, 5, 6, 8, 9]));
