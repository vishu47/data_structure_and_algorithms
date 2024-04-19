// Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
// Input:
// N = 5
//
// Output:
// 0 0 1 2 2
// Explanation:
// 0s 1s and 2s are segregated
// into ascending order.

let arr = [0, 2, 1, 2, 0];

const sor012 = (arr, n) => {
  let i = 0,
    cnt0 = 0,
    cnt1 = 0,
    cnt2 = 0;
  for (let i = 0; i < n; i++) {
    switch (arr[i]) {
      case 0:
        cnt0++;
        break;
      case 1:
        cnt1++;
        break;
      case 2:
        cnt2++;
        break;
    }
  }
  while (cnt0 > 0) {
    arr[i++] = 0;
    cnt0--;
  }

  while (cnt1 > 0) {
    arr[i++] = 1;
    cnt1--;
  }

  while (cnt2 > 0) {
    arr[i++] = 2;
    cnt2--;
  }
};

sor012(arr, arr.length);
