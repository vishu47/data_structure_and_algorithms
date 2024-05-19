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
console.log(findPair(10, 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
