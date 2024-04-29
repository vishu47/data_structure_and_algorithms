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

// isPalindrome("abc");

// Given an unsorted array arr[] of size N. Rotate the array to the left
// (counter-clockwise direction) by D steps, where D is a positive integer.

function reverseArry(arr, start, end) {
  while (start < end) {
    // console.log(start, end);
    let temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start++;
    end--;
  }
}

function rotateArr(arr, d, n) {
  // code here
  // not optimal method
  // const a = [];
  // for (let i = d; i < arr.length; i++) {
  //   a.push(arr[i]);
  // }
  // for (let i = 0; i < d; i++) {
  //   a.push(arr[i]);
  // }

  // return a;

  // for optimal, solution it modify the original array
  // reverse the array from 0 to d
  // Calculate the effective rotation (d % n)
  d = d % n;

  reverseArry(arr, 0, d - 1);
  // reverse the array from d to length of array
  reverseArry(arr, d, arr.length - 1);
  // reverse the whole array
  reverseArry(arr, 0, arr.length - 1);

  return arr;
}

// console.log(
//   rotateArr(
//     [
//       25, 6, 20, 55, 69, 5, 50, 63, 61, 41, 87, 80, 2, 96, 77, 70, 12, 43, 31,
//       8, 64, 41, 68, 18, 95, 79, 52, 74, 1, 98, 3, 26, 3, 74, 32, 23, 79, 81,
//       37, 39, 21, 24, 18, 22, 71, 47, 44,
//     ],
//     77,
//     47
//   )
// );

// Given a String S, reverse the string without reversing its individual words.
//  Words are separated by dots.

function reverseWords(s) {
  // console.log(s.split(".").join("."));
  return s.split(".").reverse().join(".");
}

// console.log(reverseWords("much.very.program.this.like.i"));

// Given two strings a and b consisting of lowercase characters.
// The task is to check whether two given strings are an anagram of each other or not.
// An anagram of a string is another string that contains the same characters,
// only the order of characters can be different. For example, act and tac are an
// anagram of each other. Strings a and b can only contain lower case alphabets.

function isAnagram(a, b) {
  const aa = a.split("").sort().join("");
  const bb = b.split("").sort().join("");
  if (aa === bb) {
    return true;
  } else {
    return false;
  }
}

// console.log(isAnagram("geeksforgeeks", "forgeeksgeeks"));

// Given a sorted array containing only 0s and 1s, find the transition point, i.e.,
// the first index where 1 was observed, and before that, only 0 was observed.

function transitionPoint(arr, n) {
  if (arr.length === 1) return i;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 1) return i;
  }
  return -1;
}

// console.log(transitionPoint([0,0,0,0,0]));

// Given an array Arr of N positive integers and another number X.
// Determine whether or not there exist two elements in Arr whose sum is exactly X.
function hasArrayTwoCandidates(arr, n, x) {
  // 2 pointer approch
  // let left = 0;
  // let right = n - 1;
  // arr.sort((a, b) => a - b);
  // while (left < right) {
  //   const sum = arr[left] + arr[right];
  //   if (sum === x) {
  //     return "Yes";
  //   }
  //   if (sum > x) {
  //     right--;
  //   }
  //   if (sum < x) {
  //     left++;
  //   }
  // }
  // return "No";
  // compliment approch
  let st = new Map();
  for (let i = 0; i < arr.length; i++) {
    if (st.has(arr[i])) {
      return true;
    }
    st.set(Math.abs(arr[i] - x));
  }
  return false;
}

// console.log(
//   hasArrayTwoCandidates(
//     [
//       335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996,
//       943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727,
//       772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334,
//     ],
//     42,
//     468
//   )
// );

// Given an array of N strings, find the longest common prefix among all strings present in the array.
// N = 4
// arr[] = {geeksforgeeks, geeks, geek,
//          geezer}
// Output: gee
// Explanation: "gee" is the longest common
// prefix in all the given strings.

function longestCommonPrefix(arr, n) {
  let comp = arr[0];
  for (let i = 1; i < arr.length; i++) {
    let j = 0;
    while (arr[i][j] === comp[j] && j < comp.length && j < arr[i].length) {
      j++;
    }
    comp = comp.substring(0, j);
  }
  return comp.length > 0 ? comp : -1;
}

// console.log(longestCommonPrefix(["hello", "world"], 2));

// Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
// In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

// If there are multiple solutions, find the lexicographically smallest one.

// Note:The given array is sorted in ascending order, and you don't need to return anything to
// make changes in the original array itself.

function convertToWave(arr, n) {
  let start = 0;
  let end = 1;
  while (start < n - 1) {
    let temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start += 2;
    end += 2;
  }
  return arr;
}

// console.log(convertToWave([2, 4, 7, 8, 9, 10], 6));

// Given an array arr[] of N positive integers which can contain integers from 1 to P where
// elements can be repeated or can be absent from the array. Your task is to count the frequency
// of all numbers from 1 to N. Make in-place changes in arr[], such that arr[i] = frequency(i).
// Assume 1-based indexing.
// Note: The elements greater than N in the array can be ignored for counting and do modify
// the array in-place.

function frequencyCount(arr, N, P) {
  let mp = new Map();
  let i = 0;
  while (i < N) {
    if (arr[i] <= P && mp.has(arr[i])) {
      mp.set(arr[i], mp.get(arr[i]) + 1);
    } else {
      mp.set(arr[i], 1);
    }
    i++;
  }
  for (let i = 0; i < N; i++) {
    if (mp.has(i + 1)) {
      arr[i] = mp.get(i + 1);
    } else {
      arr[i] = 0;
    }
  }
  return arr;
}

// console.log(frequencyCount([3, 3, 3, 3], 4, 3));

// You are given an array a, of n elements. Find the minimum index based
// distance between two distinct elements
// of the array, x and y. Return -1, if either x or y does not exist in the array.

function minDist(a, n, x, y) {
  // return  d===0 ? -1 : d;
  // let minDistance = Number.MAX_SAFE_INTEGER;
  //   let lastIndexX = -1;
  //   let lastIndexY = -1;
  //   for (let i = 0; i < arr.length; i++) {
  //       if (arr[i] === x) {
  //           lastIndexX = i;
  //           if (lastIndexY !== -1) {
  //               minDistance = Math.min(minDistance, Math.abs(lastIndexX - lastIndexY));
  //           }
  //       } else if (arr[i] === y) {
  //           lastIndexY = i;
  //           if (lastIndexX !== -1) {
  //               minDistance = Math.min(minDistance, Math.abs(lastIndexX - lastIndexY));
  //           }
  //       }
  //   }
  //   return minDistance === Number.MAX_SAFE_INTEGER ? -1 : minDistance;
  // let finalDist = Number.MAX_SAFE_INTEGER;
  // let ix = -1;
  // let iy = -1;
  // for (let i = 0; i < n; i++) {
  //   if (a[i] === x) {
  //     ix = i;
  //     console.log(finalDist, Math.abs(ix - iy), "if");
  //     if (iy !== -1) {
  //       finalDist = Math.min(finalDist, Math.abs(ix - iy));
  //       console.log(finalDist, Math.abs(ix - iy), "if");
  //     }
  //   } else if (a[i] === y) {
  //     iy = i;
  //     if (ix !== -1) {
  //       console.log(finalDist, Math.abs(ix - iy), "else");
  //       finalDist = Math.min(finalDist, Math.abs(ix - iy));
  //     }
  //   }
  // }
  // return finalDist === -1 ? -1 : finalDist;
  let dist = a.length;
  let lastindex = -1;
  for (let i = 0; i < n; i++) {
    if (a[i] === x || a[i] === y) {
      if (lastindex !== -1 && a[i] !== a[lastindex]) {
        dist = Math.min(dist, i - lastindex);
      }
      lastindex = i;
    }
  }
  return dist === a.length ? -1 : dist;
}
// https://chat.openai.com/c/97a0089f-a20e-41c8-ae36-c59cf1f7d243
// console.log(minDist([1, 2, 3, 2], 4, 1, 2));

// Given a sorted array a[] of size n, delete all the duplicated elements from a[] &
// modify the array such that only distinct elements should be present there.

// Note:
// 1. Don't use set or HashMap to solve the problem.
// 2. You must return the modified array size where only distinct elements are present
// in the array, the driver code will print all the elements of the modified array.

function remove_duplicate(arr, n) {
  //code here
  let lastIndex = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] !== arr[lastIndex]) {
      lastIndex++;
      arr[lastIndex] = arr[i];
    }
  }
  console.log(arr)
  return lastIndex + 1;
}

console.log(
  remove_duplicate(
    [
      1, 3, 4, 5, 6, 12, 13, 17, 19, 22, 23, 25, 27, 28, 28, 35, 36, 37, 39, 43,
      46, 48, 54, 59, 62, 63, 65, 68, 68, 70, 70, 72, 79, 82, 83, 92, 92, 93,
      95, 96, 96,
    ],
    14
  ),
  "ll"
);

console.log("run practice file");
