// Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is a leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.

// Example 1:

// Input:
// n = 6
// A[] = {16,17,4,3,5,2}
// Output: 17 5 2
// Explanation: The first leader is 17
// as it is greater than all the elements
// to its right.  Similarly, the next
// leader is 5. The right most element
// is always a leader so it is also
// included.

//Function to find the leaders in the array.
function leaders(arr, n) {
  // my solution
  // let lead = [];
  // let flag = false;
  // for (let i = 0; i <= arr.length; i++) {
  //   if (i === arr.length - 1) {
  //     lead.push(arr[i]);
  //     break
  //   }
  //   for (let j = i + 1; j < arr.length; j++) {
  //     if (arr[i] >= arr[j]) {
  //       flag = true;
  //     } else {
  //       flag = false;
  //       break;
  //     }
  //   }
  //   if (flag) {
  //     lead.push(arr[i]);
  //   }
  // }
  // console.log(lead)
  // return lead;

  // optimal solution

  let lead = [];
  let lastEl = arr[arr.length - 1];
  lead.push(lastEl);

  for (let i = arr.length - 2; i >= 0; i--) {
    if (arr[i] >= lastEl) {
      lead.push(arr[i]);
      lastEl = arr[i];
    }
  }
  console.log(lead);
  return lead.reverse();
}

// leaders([63, 70, 80, 33, 33, 47, 20], 7);

// Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.

// Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

// Example 1:

// Input:
// n = 5
// A[] = {1,3,5,2,2}
// Output:
// 3
// Explanation:
// equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2).

function equilibriumPoint(a, n) {
  // this approch is good and brrot fource approch but got more time to execute have to optimied this code
  let f = 0;
  let b = 0;
  let out = -1;
  for (let i = 0; i < a.length; i++) {
    for (let j = i + 1; j < a.length; j++) {
      f += a[j];
    }
    for (let k = i - 1; k >= 0; k--) {
      b += a[k];
    }
    if (f === b) {
      return (out = i + 1);
    }
    b = 0;
    f = 0;
  }
  return out;
}

equilibriumPoint([4, 5, 7], 3);

console.log("run practice file");
