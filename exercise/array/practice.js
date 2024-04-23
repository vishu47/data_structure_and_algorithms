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
  // let f = 0;
  // let b = 0;
  // let out = -1;
  // for (let i = 0; i < a.length; i++) {
  //   for (let j = i + 1; j < a.length; j++) {
  //     f += a[j];
  //   }
  //   for (let k = i - 1; k >= 0; k--) {
  //     b += a[k];
  //   }
  //   if (f === b) {
  //     return (out = i + 1);
  //   }
  //   b = 0;
  //   f = 0;
  // }
  // console.log(out)
  // return out;

  // optimal solutions

  let ls = 0;
  let totalSum = a.reduce((sum, current) => {
    return sum + current;
  }, 0);

  console.log(totalSum, "totalSums");

  for (let i = 0; i < a.length; i++) {
    totalSum -= a[i];

    if (totalSum === ls) {
      console.log(i, "i");
      return i;
    }

    ls += a[i];
  }

  console.log(-1, "-1");
  return -1;
}

// equilibriumPoint([4, 5, 7], 3);
// equilibriumPoint([1, 3, 5, 2, 2], 5);

// Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
// For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

// Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

function ispar(x) {
  //your code here
  // let s = 0;
  // let m = 0;
  // let b = 0;
  // for (let i = 0; i < x.length; i++) {
  //   if ("{" === x[i] || "}" === x[i]) {
  //     m += 1;
  //   } else if ("(" === x[i] || ")" === x[i]) {
  //     s += 1;
  //   } else if ("[" === x[i] || "]" === x[i]) {
  //     b += 1;
  //   }
  // }
  // console.log(
  //   s,
  //   m,
  //   b,
  //   b % 2,
  //   m % 2,
  //   s % 2,
  //   b % 2 === 0 && m % 2 === 0 && s % 2 === 0
  // );

  // if (b % 2 === 0 && m % 2 === 0 && s % 2 === 0) {
  //   console.log("balanced");
  //   return true;
  // } else {
  //   console.log("not balanced");
  //   return false;
  // }

  // optimal solution
  let a = [];
  let comp = { "(": ")", "{": "}", "[": "]" };

  for (let i = 0; i < x.length; i++) {
    if (x[i] === "[" || x[i] === "{" || x[i] === "(") {
      a.push(x[i]);
    } else {
      const pop = a.pop();
      if (!pop || comp[pop] !== x[i]) {
        return false;
      }
    }
  }
  return a.length === 0;
}

// ispar("]");

// Given an array Arr of size N, print the second largest distinct element from an array.
//  If the second largest element doesn't exist then return -1.

function print2largest(arr, n) {
  //code here
  const sort = arr.sort((a, b) => a - b);
  const fin = [...new Set(sort)];
  // console.log(fin[fin.length - 2], fin, fin.length);
  return fin[fin.length - 2] ? fin[fin.length - 2] : -1;
}

// print2largest([35, 35, 1, 10, 34, 1]);

// Given an array of N integers, and an integer K, find the number of pairs of
// elements in the array whose sum is equal to K.

function getPairsCount(arr, n, k) {
  // not optimal solution
  // let count = 0;
  // for (let i = 0; i < arr.length; i++) {
  //   for (let j = i + 1; j < arr.length; j++) {
  //     const runsum = arr[i] + arr[j];
  //     if (runsum === k) {
  //       count += 1;
  //     }
  //   }
  // }
  // console.log(count);
  // return count

  // two pointer approch

  let h = new Map();
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    let find = k - arr[i];
    if (h.has(find)) {
      count += h.get(find);
    }
    h.set(arr[i], (h.get(arr[i]) || 0) + 1);
  }
  console.log(count);
  return count;
}

// getPairsCount([1, 1, 1, 1], 4, 2);

// Given a string S, check if it is palindrome or not.

function isPalindrome(S) {
  // time complaxity
  // const rev = s.split('').reverse().join("");
  // if (rev.toLowerCase() === s.toLowerCase()) {
  //   // console.log(true);
  //   return 1;
  // } else {
  //   // console.log(false);
  //   return 0;
  // }

  // two pointer approch

  let left = 0;
  let right = S.length - 1;

  while (left < right) {
    if (S[left] !== S[right]) {
      return 0;
    }
    left++;
    right--;
  }
  return 1;
}

isPalindrome("abc");

console.log("run practice file");
