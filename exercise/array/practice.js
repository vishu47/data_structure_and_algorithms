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
  //   b % 2,===,0 && m % 2 === 0 && s % 2 === 0
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
    console.log(lastIndex, "last");
    if (arr[i] !== arr[lastIndex]) {
      lastIndex++;
      arr[lastIndex] = arr[i];
      console.log(arr, lastIndex, arr[lastIndex], arr[i], "iside");
    }
    console.log(arr);
  }
  return lastIndex + 1;
}
// console.log(remove_duplicate([1, 3, 12, 5, 6, 12, 13], 14), "ll");

// Given an array A of N integers. Your task is to write a program to find the
// maximum value of ∑arr[i]*i, where i = 0, 1, 2,., n 1.
// You are allowed to rearrange the elements of the array.
// Note: Since output could be large, hence module 109+7 and then print answer.
// Input : Arr[] = {5, 3, 2, 4, 1}
// Output : 40
// Explanation:
// If we arrange the array as 1 2 3 4 5 then
// we can see that the minimum index will multiply
// with minimum number and maximum index will
// multiply with maximum number.
// So 1*0+2*1+3*2+4*3+5*4=0+2+6+12+20 = 40 mod(109+7) = 40

function Maximize(arr, n) {
  let sum = 0;
  arr.sort((a, b) => a - b);
  //  tle
  // for (let i = 0; i < n; i++) {
  //   sum = sum + arr[i] * (arr[i] - 1);
  // }

  // reduce method
  const ssum = arr.reduce((sum, current, index) => sum + current * index, 0);
  return ssum % 1000000007;
}

// console.log(Maximize([5, 3, 2, 4, 1], 5));

// Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal
// to the product of all the elements of nums except nums[i].
// Input:
// n = 5
// nums[] = {10, 3, 5, 6, 2}
// Output:
// 180 600 360 300 900
// Explanation:
// For i=0, P[i] = 3*5*6*2 = 180.
// For i=1, P[i] = 10*5*6*2 = 600.
// For i=2, P[i] = 10*3*6*2 = 360.
// For i=3, P[i] = 10*3*5*2 = 300.
// For i=4, P[i] = 10*3*5*6 = 900.

// https://www.youtube.com/watch?v=G9zKmhybKBM
function productExceptSelf(nums, n) {
  //  tle
  // let pr = [];
  // let sum = 1;
  // for (let i = 0; i < n; i++) {
  //   for (let j = 0; j < n; j++) {
  //     if (i !== j) {
  //       sum = sum * nums[j];
  //     }
  //   }
  //   pr.push(sum);
  //   sum = 1;
  // }
  // return pr;

  let pre = new Array(n).fill(1);
  let post = new Array(n).fill(1);
  let final = new Array(n).fill(1);
  for (let i = 1; i < n; i++) {
    pre[i] = nums[i - 1] * pre[i - 1];
  }
  for (let j = n - 2; j >= 0; j--) {
    post[j] = nums[j + 1] * post[j + 1];
  }
  // console.log(pre, post);
  for (let k = 0; k < n; k++) {
    final[k] = pre[k] * post[k];
  }
  return final;
}

// console.log(productExceptSelf([10, 3, 5, 6, 2], 5));

// Given an array of n integers. Find the first element that occurs atleast k number of times.
// If no such element exists in the array, then expect the answer to be -1.
// Input :
// n = 7, k = 2
// a[] = {1, 7, 4, 3, 4, 8, 7}
// Output :
// 4
// Explanation :
// Both 7 and 4 occur 2 times. But 4 is first that occurs twice.
// As at index = 4, 4 has occurred twice whereas 7 appeared twice
// at index 6.

function firstElementKTime(n, k, arr) {
  let mp = new Map();
  for (let i = 0; i < n; i++) {
    if (mp.has(arr[i])) {
      let fre = mp.get(arr[i]) + 1;
      mp.set(arr[i], fre);
      if (fre === k) return arr[i];
    } else {
      mp.set(arr[i], 1);
    }
  }
  return -1;
}

// console.log(firstElementKTime(10, 4, [3, 1, 3, 4, 5, 1, 3, 3, 5, 4]), "ans");

// Given an array arr[] of size N, check if it is sorted in non-decreasing order or not.

function arraySortedOrNot(arr, n) {
  for (let i = 1; i < n - 1; i++) {
    if (arr[i] >= arr[i - 1] && arr[i] <= arr[i + 1]) {
      continue;
    } else {
      return false;
    }
  }
  return true;
}

// console.log(
//   arraySortedOrNot([1, 2, 3, 5, 5, 7, 7, 7, 8, 12, 13, 15, 15, 15, 19], 15)
// );

// Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of
// elements in the intersection (or common elements) of the two arrays.
// For this question, the intersection of two arrays can be defined as the set
// containing distinct common elements between the two arrays.

function NumberofElementsInIntersection(a, b, n, m) {
  let st = new Set(a);
  let count = 0;
  for (let i = 0; i < m; i++) {
    if (st.has(b[i])) {
      count++;
      // for preventing the duplicasy
      st.delete(b[i]);
    }
  }
  return count;
}
// https://www.youtube.com/watch?v=zgLtdM8-6CE
// console.log(
//   NumberofElementsInIntersection([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 3], 6, 6)
// );

// Given an array arr[] of n positive integers. Push all the zeros of the given array
// to the right end of the array while maintaining
// the order of non-zero elements. Do the mentioned change in the array in-place.

function pushZerosToEnd(arr, n) {
  //code here
  // thsi solution will not persist the position of the element(2 pointer approch)
  // let lt = 0;
  // let rt = n - 1;
  // while (lt < rt) {
  //   console.log(lt, rt);
  //   if (arr[lt] === 0 && arr[rt] !== 0) {
  //     let temp = arr[lt];
  //     arr[lt] = arr[rt];
  //     arr[rt] = temp;
  //     rt--;
  //     lt++;
  //   }
  //   if (arr[lt] !== 0) {
  //     lt++;
  //   }
  //   if (arr[lt] === 0 && arr[rt] === 0) {
  //     break;
  //   }
  // }
  // return arr;

  let nz = 0; //non zero
  let z = 0; // zero
  while (nz < n) {
    console.log(arr[nz]);
    if (arr[nz] !== 0) {
      let temp = arr[nz];
      arr[nz] = arr[z];
      arr[z] = temp;
      nz++;
      z++;
    } else {
      nz++;
    }
  }
  return nz;
}

// console.log(pushZerosToEnd([0, 5, 3, 0, 4], 5));

// Given an unsorted array Arr of N positive and negative numbers. Your task is to create
// an array of alternate positive and negative numbers without changing the relative order
// of positive and negative numbers.
// Note: Array should start with a positive number and 0 (zero) should be considered a positive element.

function rearrange(arr, n) {
  let pos = [];
  let neg = [];
  let final = [];
  for (let i = 0; i < n; i++) {
    if (arr[i] < 0) {
      neg.push(arr[i]);
    } else {
      pos.push(arr[i]);
    }
  }
  let p = 0;
  let ne = 0;
  for (let j = 0; j < Math.max(neg.length, pos.length); j++) {
    if (j < pos.length) {
      final.push(pos[ne]);
      ne++;
    }
    if (j < neg.length) {
      final.push(neg[p]);
      p++;
    }
  }
  return final;
}
// console.log(rearrange([9, 4, -2, -1, 5, 0, -5, -3, 2], 9));

// Given an ascending sorted rotated array arr of distinct integers of size n.
//  The array is right-rotated k times. Find the value of k.

function findKRotation(arr, n) {
  // binary search loop
  let left = 0;
  let right = n - 1;
  // while (left < right) {
  //   const mid = Math.floor((left + right) / 2);
  //   if (array[mid] > array[right]) {
  //     left = mid + 1;
  //   } else {
  //     right = mid;
  //   }
  // }
  // return left

  while (left < right) {
    if (arr[left] > arr[right]) {
      left++;
    } else {
      right--;
    }
  }
  return left;
}

// console.log(findKRotation([1, 2, 3, 4, 5], 5));

// Given an array of size n and a range [a, b]. The task is to partition the array around the range such that the array is divided into three parts.
// 1) All elements smaller than a come first.
// 2) All elements in range a to b come next.
// 3) All elements greater than b appear in the end.
// The individual elements of three sets can appear in any order. You are required to return the modified array.

// Note: The generated output is 1 if you modify the given array successfully.

// Geeky Challenge: Solve this problem in O(n) time complexity.

function threewaypartition(array, a, b) {
  // let low = 0;
  // let mid = 0;
  // let high = array.length - 1;
  // while (mid <= high) {
  //   if (array[mid] < a) {
  //     // Swap arr[mid] with arr[low]
  //     [array[mid], array[low]] = [array[low], array[mid]];
  //     low++;
  //     mid++;
  //   } else if (array[mid] >= a && array[mid] <= b) {
  //     // Element in range [a, b], move mid pointer
  //     mid++;
  //   } else {
  //     // Swap arr[mid] with arr[high]
  //     [array[mid], array[high]] = [array[high], array[mid]];
  //     high--;
  //   }
  // }
  // // Return 1 to indicate successful modification
  // return 1;

  let l = 0;
  let r = array.length - 1;

  for (let i = 0; i <= r; i++) {
    if (array[i] < a) {
      [array[i], array[l]] = [array[l], array[i]];
      l++;
    }
    if (array[i] > b) {
      [array[i], array[r]] = [array[r], array[i]];
      r--;
      i--;
    }
  }
}

// console.log(
//   threewaypartition([10, 7, 6, 1, 4, 10, 5, 2, 7, 5, 3, 3, 8, 3, 8], 5, 5)
// );

// Given two unsorted arrays A of size N and B of size M of distinct elements,
// the task is to find all pairs from both arrays whose sum is equal to X.

// Note: All pairs should be printed in increasing order of u. For eg. for two pairs
// (u1,v1) and (u2,v2), if u1 < u2 then
// (u1,v1) should be printed first else second.

function allPairs(A, B, N, M, X) {
  const pairs = [];
  // A.sort();
  // for (let i = 0; i < N; i++) {
  //   for (let j = 0; j < M; j++) {
  //     if (A[i] + B[j] === X) {
  //       pairs.push([A[i], B[j]]);
  //     }
  //   }
  // }
  // return pairs;
  const st = new Set(B);
  A.sort((a, b) => a - b);
  for (let i = 0; i < N; i++) {
    if (st.has(X - A[i])) {
      pairs.push([A[i], X - A[i]]);
    }
  }
  return pairs;
}

// console.log(allPairs([1, 2, 4, 5, 7], [5, 6, 3, 4, 8], 5, 5, 9));

// Given an unsorted array of size N. Find the first element in array such that all of
//  its left elements are smaller and all right elements to it are greater than it.

// Note: Left and right side elements can be equal to required element.
//  And extreme elements cannot be required element.

function check(arr, n, ind) {
  i = ind - 1;
  j = ind + 1;

  while (i >= 0) {
    console.log(arr[i], "whilei");
    if (arr[i] > arr[ind]) {
      return false;
    }
    i--;
  }
  while (j < n) {
    console.log(arr[j], "whilej");
    if (arr[j] < arr[ind]) {
      return false;
    }
    j++;
  }
  return true;
}

function findElement(arr, n) {
  // for (let i = 1; i < n - 1; i++) {
  //   console.log(check(arr, n, i), "arr, n, i");
  //   if (check(arr, n, i)) {
  //     return arr[i];
  //   }
  // }
  // return -1;

  const left = [];
  const right = [];
  for (let i = 1; i < n; i++) {
    // /  let max
    left[i] = Math.max(left[i], left[i - 1]);
  }
  // /  right min
  for (let j = n - 2; j > 0; j--) {
    right[j] = Math.min(right[j + 1], right[j]);
  }

  console.log(left, right);

  for (let k = 0; k < n; k++) {
    // console.log(arr[k]);
    if (arr[k] >= left[k] && arr[k] <= right[k]) {
      console.log(arr[k]);
    }
  }
}

// console.log(findElement([4, 2, 5, 7], 4));

// Given an array of integers (A[])  and a number x, find the
//  smallest subarray with sum greater than the given value.
//  If such a subarray do not exist return 0 in that case.

function smallestSubWithSum(a, n, x) {
  // broot force
  // let sum = a[0];
  // let ln = Number.MAX_SAFE_INTEGER;
  // for (let i = 0; i < n; i++) {
  //   sum = a[i];
  //   for (let j = i + 1; j < n; j++) {
  //     sum += a[j];
  //     if (sum > x) {
  //       console.log(sum, i, j, a[j]);
  //       ln = Math.min(ln, j - i + 1);
  //       break;
  //     }
  //   }
  // }
  // return ln === Number.MAX_SAFE_INTEGER ? 0 : ln;

  // sliding window approch

  let ws = 0;
  let i = 0;
  let ln = Number.MAX_SAFE_INTEGER;
  let sum = 0;

  while (i < n) {
    sum += a[i];
    if (sum > x) {
      ln = Math.min(ln, i - ws + 1);
      while (ws < i && sum > x) {
        sum -= a[ws];
        ws++;
        if (sum > x) {
          ln = Math.min(ln, i - ws + 1);
        }
      }
    }
    i++;
  }
  return ln === Number.MAX_SAFE_INTEGER ? 0 : ln;
}

// console.log(smallestSubWithSum([1, 10, 5, 2, 7], 5, 9));

// Given an array arr of distinct elements of size n, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form:
// arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n].
// NOTE: If your transformation is correct, the output will be 1 else the output will be 0.

function zigZag(n, arr) {
  for (let i = 0; i < n - 1; i++) {
    if (i % 2 === 0 && arr[i] > arr[i + 1]) {
      let temp = arr[i];
      arr[i] = arr[i + 1];
      arr[i + 1] = temp;
    } else if (i % 2 === 0 && arr[i] < arr[i + 1]) {
      let temp = arr[i];
      arr[i] = arr[i + 1];
      arr[i + 1] = temp;
    }
  }
  return arr;
}

// console.log(zigZag(7, [4, 3, 7, 8, 6, 2, 1]));

// Given an unsorted array arr[] of size n having both negative and positive integers.
// The task is place all negative element at the end of array without changing the order
// of positive element and negative element.

function segregateElements(arr, n) {
  // const a = [];
  // const b = [];
  // for (let i = 0; i < n; i++) {
  //   if (arr[i] < 0) {
  //     a.push(arr[i]);
  //   } else {
  //     b.push(arr[i]);
  //   }
  // }
  // return [...b, ...a];

  // const b = [];
  // let k = 0;
  // for (let i = 0; i < n; i++) {
  //   if (arr[i] >= 0) {
  //     b[k] = arr[i];
  //     k++;
  //   }
  // }
  // for (let i = 0; i < n; i++) {
  //   if (arr[i] < 0) {
  //     b[k] = arr[i];
  //     k++;
  //   }
  // }
  // return b

  // let tr = n - 1;
  // for (let i = n - 1; i >= 0; i--) {
  //   if (arr[i] < 0) {
  //     const rp = arr[i];

  //     for (let j = i; j < tr; j++) {
  //       arr[j] = arr[j + 1];
  //     }
  //     arr[tr] = rp;

  //     tr--;
  //   }
  // }

  // stack solution
  const a = [];
  const b = [];
  for (let i = 0; i < n; i++) {
    if (arr[i] < 0) {
      a.push(arr[i]);
    } else {
      b.push(arr[i]);
    }
  }

  let i = n - 1;

  while (a.length > 0) {
    arr[i] = a.pop();
    i--;
  }
  while (b.length > 0) {
    arr[i] = b.pop();
    i--;
  }

  return arr;
}

// console.log(segregateElements([1, -1, 3, 2, -7, -5, 11, 6], 8));

//

// Given two sorted arrays of distinct elements. There is only 1 difference between the arrays.
// The first array has one element extra added in between. Find the index of the extra element.

function findExtra(a, b, n) {
  let on = 0;
  let tw = 0;

  while (on < n || tw < n) {
    if (a[on] !== b[tw] && (a[on] !== undefined || b[on] !== undefined)) {
      console.log(a[on]);
      return on ? on : tw;
    }
    on++;
    tw++;
  }
}

// console.log(findExtra([3, 5, 7, 9, 11, 13], [3, 5, 7, 11, 13], 6));

// Given an array Arr of size N consisting of only 0's and 1's. The array is
// sorted in such a manner that all the 1's are placed first and then they are
// followed by all the 0's. Find the count of all the 0's.

function countZeroes(arr, n) {
  // write your code here
  let sum = 0;
  for (let i = n; i >= 0; i--) {
    if (arr[i] === 0) {
      sum++;
    }
  }
  return sum;
}

// console.log(countZeroes([0, 0, 0, 0, 0], 5));

// Given an array arr of size N and an element k. The task is to find the
// count of elements in the array that appear more than n/k times.

function countOccurence(arr, n, k) {
  const c = n / k;
  const mp = new Map();
  let f = 0;
  for (let i = 0; i < n; i++) {
    if (mp.has(arr[i])) {
      mp.set(arr[i], mp.get(arr[i]) + 1);
    } else {
      mp.set(arr[i], 1);
    }
  }

  for (let [key, value] of mp) {
    if (value > c) {
      f++;
    }
  }
  return f;

  // BR approch
  // const occ = [];

  // for (let i = 0; i < n; i++) {
  //   let cn = 0;
  //   for (let j = 0; j < n; j++) {
  //     if (arr[i] === arr[j]) {
  //       cn++;
  //     }
  //     if (cn > c && !occ.includes(arr[i])) {
  //       occ.push(arr[i]);
  //     }
  //   }
  // }
  // return occ.length;
}

// console.log(countOccurence([2, 3, 3, 2], 4, 3));

// Given a string str which may contain lowercase and uppercase characters. The task
// is to remove all duplicate characters from the string and find the resultant string.
// The order of remaining characters in the output should be same as in the original string.

function removeDuplicates(str) {
  //code here
  const mp = new Set();
  let fl = "";
  for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
    mp.add(str[i]);
  }
  mp.forEach((el) => {
    fl += el;
  });
  return fl;
}

// console.log(removeDuplicates("geEksforGEeks"));

// Given two integer arrays a of size n and b of size m, the task is to find the
// numbers which are present in the first array a, but not present in the second array
// b.
//
// Note: Numbers to be returned should in order as they appear in array a.

function findMissing(a, b, n, m) {
  let fl = [];
  let flag = false;
  let st = new Set(b);
  for (let i = 0; i < n; i++) {
    if (!st.has(a[i])) {
      fl.push(a[i]);
    }
  }
  return fl;
}

// console.log(findMissing([1, 2, 3, 4, 5, 10], [2, 3, 1, 0, 5], 6, 5));

// You are given two arrays, A and B, of equal size N. The task is to find the minimum
// value of A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.
//

function minValue(arr, brr, n) {
  //code here
  const nw = brr.sort((a, b) => b - a);
  const a = arr.sort((a, b) => a - b);
  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum = sum + a[i] * nw[i];
  }

  return sum;
}

// console.log(minValue([3, 1, 1], [6, 5, 4], 3));

// Given an array arr of n positive integers. The task is to swap every ith element
// of the array with (i+2)th element.
function swapElements(n, arr) {
  for (let i = 0; i < n - 2; i++) {
    let temp = arr[i];
    arr[i] = arr[i + 2];
    arr[i + 2] = temp;
  }
  return arr;
}

// console.log(swapElements(5, [1,2,3,4,5]));

// Given an array of length n consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s on the
// left side and 1s on the right side of the array.

function segregate0and1(arr, n) {
  let left = 0;
  let right = n - 1;
  while (left < right) {
    console.log(left, right, arr);
    if (arr[left] === 1) {
      [arr[left], arr[right]] = [arr[right], arr[left]];
      right--;
    } else {
      left++;
    }
  }
  console.log(arr);
}

// console.log(segregate0and1([0, 0, 1, 1, 0, 1], 6));

// You will be given an array arr of integers of length N. You can construct
// an integer from two integers by treating the integers as strings, and
// then concatenating them. For example, 19 and 4 can be used to construct
// 194 and 419.

// The task is to find whether it’s possible to construct an integer using
// all the digits of these numbers such that it would be divisible by 3.
// If it is possible then print 1 and if not print 0.

function isPossible(N, arr) {
  let str = "";
  let count = 0;
  for (let i = 0; i < N; i++) {
    str += arr[i];
  }
  for (let i = 0; i < str.length; i++) {
    count += parseInt(str[i]);
  }
  return count % 3 === 0 ? 1 : 0;
}

// console.log(isPossible(5, [400000, 10000, 8000, 900, 30, 7]));

// Given a matrix(2D array) M of size N*N consisting of 0s and 1s only.
// The task is to find the column with maximum number of 0s. If more than
// one column exists, print the one which comes first. If the maximum
// number of 0s is 0 then return -1.

function columnWithMaxZeros(M, n) {
  let col = -1;
  let sumVal = 0;
  for (let i = 0; i < n; i++) {
    let row = 0;
    let count = 0;
    while (row < n) {
      // console.log(M[row][i]);
      if (M[row][i] === 0) {
        count++;
      }
      // console.log(count,sumVal,i);
      if (count > sumVal) {
        sumVal = count;
        col = i;
      }
      row++;
    }
  }
  return col === -1 ? -1 : col;
}

// console.log(
//   columnWithMaxZeros(
//     [
//       [1, 1],
//       [1, 1],
//     ],
//     2
//   )
// );

// Given an array of integers of size N and a number K., You must modify array arr[]
// exactly K number of times. Here modify array means in each operation you can replace
//  any array element either arr[i] by -arr[i] or -arr[i] by arr[i]. You need to
//  perform this operation in such a way that after K operations, the sum of the
//  array must be maximum.

function maximizeSum(arr, n, k) {
  let sum = 0;
  let kn = k;
  let min = Number.MAX_SAFE_INTEGER;
  arr.sort((a, b) => a - b);
  console.log(arr, "lldddd");
  for (let i = 0; i < n; i++) {
    if (arr[i] < 0 && kn > 0) {
      arr.splice(i, 1, -arr[i]);
      kn -= 1;
    }
    sum += arr[i];
    min = Math.min(min, arr[i]);
  }
  // console.log(arr, kn, sum - min, min);
  console.log(arr, "ll");
  if (kn % 2 !== 0 && kn !== 0) {
    min = -min;
    sum = sum + min * 2;
  }
  return sum;
}

// console.log(maximizeSum([5, -2, 5, -4, 5, -12, 5, 5, 5, 20], 10, 5));

// Given an array of distinct elements which was initially sorted.
// This array may be rotated at some unknown point. The task is to find the
// minimum element in the given sorted and rotated array.
function minNumber(arr, low, high) {
  let n = arr.length - 1;
  let min = Number.MAX_SAFE_INTEGER;
  for (let i = n; i >= 0; i--) {
    console.log(arr[i], min);
    min = Math.min(min, arr[i]);
  }
  return min;
}

// console.log(minNumber([2, 3, 4, 5, 6, 7, 8, 9, 10, 1], 1, 1));

// Given a sorted array with possibly duplicate elements. The task is to find indexes
// of first and last occurrences of an element X in the given array.

// Note: If the element is not present in the array return {-1,-1} as pair.

function indexes(v, x) {
  // const index = [-1, -1];
  // for (let i = 0; i < v.length; i++) {
  //   if (v[i] === x) {
  //     index[0] = i;
  //     break;
  //   }
  // }
  // for (let i = v.length - 1; i >= 0; i--) {
  //   console.log(v[i], v[i] === x, i);
  //   if (v[i] === x) {
  //     index[1] = i;
  //     break;
  //   }
  // }
  // return index;

  // 2 pointers

  let left = 0;
  let right = v.length - 1;
  let res = [-1, -1];
  while (left <= right) {
    if (v[left] === x) {
      res[0] = Math.max(res[0], left);
    }
    if (v[right] === x) {
      res[1] = Math.max(res[1], right);
    }
    if (res[0] < left) {
      left++;
    } else {
      right--;
    }
  }
  return res;
}

// console.log(indexes([1, 3, 5, 5, 5, 5, 67, 123, 125], 5));

// Given a non-negative number represented as a list of digits, add 1 to the number
// (increment the number represented by the digits). The digits are stored such that
// the most significant digit is first element of array.

function increment(arr, n) {
  // MSD : most significant digit will be 1st element and
  // LSD : Least Significant digit will be the last digit of list

  for (let i = n - 1; i >= 0; i--) {
    arr[i] = arr[i] + 1;
    if (arr[i] <= 9) {
      return arr;
    }
    arr[i] = 0;
  }

  arr.unshift(1);
  return arr;
}

// console.log(increment([1, 2, 4], 3));

// You are given an array arr[] of length n, you have to re-construct the same array
// arr[] in-place. The arr[i] after reconstruction will become arr[i] OR arr[i+1],
// where OR is bitwise or. If for some i, i+1 does not exists, then do not change
// arr[i].

function game_with_number(arr, n) {
  //code here
  for (let i = 0; i < n; i++) {
    if (arr[i + 1]) {
      arr[i] = arr[i] | arr[i + 1];
    }
  }
  return arr;
}

// console.log(game_with_number([10, 11, 1, 2, 3], 5));
// console.log(game_with_number([5, 9, 2, 6], 4));

// Given two sorted arrays arr and brr and a number x, find the pair whose sum is
// closest to x and the pair has an element from each array. In the case of multiple
// closest pairs return any one of them.
// Note: Can return the two numbers in any manner. The driver code takes care of the
// printing of the closest difference.

function printClosest(arr, brr, n, m, x) {
  let a = 0;
  let b = brr.length - 1;
  let sum = 0;
  let pair = [];
  let lastDiff = Number.MAX_SAFE_INTEGER;
  while (a < n && b >= 0) {
    sum = arr[a] + brr[b];
    console.log(sum);
    let diff = Math.abs(sum - x);
    if (diff < lastDiff) {
      lastDiff = Math.min(lastDiff, diff);
      pair[0] = arr[a];
      pair[1] = brr[b];
    }
    if (sum > x) {
      b--;
    } else {
      a++;
    }
  }
  return pair;
}

// console.log(printClosest([1, 1, 1, 4, 4, 5, 9, 10], [6, 7, 8, 10], 8, 4, 6));

// Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap.

function isMaxHeap(n, arr) {
  //code here
  let d = arr.length;

  // Check for every internal node if it is greater than its children
  for (let i = 0; i <= Math.floor((d - 2) / 2); i++) {
    // Left child index
    let left = 2 * i + 1;
    // Right child index
    let right = 2 * i + 2;

    // If left child is greater than parent
    if (left < d && arr[i] < arr[left]) {
      return false;
    }

    // If right child is greater than parent
    if (right < d && arr[i] < arr[right]) {
      return false;
    }
  }

  return true;
}

// console.log(isMaxHeap(6, [90, 15, 10, 7, 12, 2]));

// Given two arrays a and b both of size n. Given q queries in an array query each
// having a positive integer x denoting an index of the array a. For each query,
// your task is to find all the elements less than or equal to a[x] in the array b.

function countElements(n, a, b, q, queries) {
  // code here let\
  // b.sort((a, b) => a - b);
  // let final = [];
  // for (let i = 0; i < q; i++) {
  //   let elem = a[queries[i]];
  //   let j = 0;
  //   let count = 0;
  //   while (j < n) {
  //     if (elem >= b[j]) {
  //       // console.log(elem, b[j], elem >= b[j]);
  //       count++;
  //     } else {
  //       break;
  //     }
  //     j++;
  //   }
  //   final.push(count);
  // }
  // return final;

  b.sort((x, y) => x - y);

  // Helper function to perform binary search
  function binarySearch(arr, target) {
    let low = 0;
    let high = arr.length;

    while (low < high) {
      let mid = Math.floor((low + high) / 2);
      if (arr[mid] <= target) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }

    return low;
  }

  let final = [];

  for (let i = 0; i < queries.length; i++) {
    let elem = a[queries[i]];
    // Perform binary search to find the count of elements <= elem
    let count = binarySearch(b, elem);
    final.push(count);
  }

  return final;
}

// console.log(countElements(4, [1, 1, 5, 5], [0, 1, 2, 3], 4, [0, 1, 2, 3]));

// Given an array arr[] of size N of distinct elements and a number X, find if there is a pair in arr[] with product equal to X.
function isProduct(arr, n, x) {
  //code here
  // failed some cases
  // arr.sort((a,b) => a - b)
  // let left = 0;
  // let right = n - 1;
  // while (left < right) {
  //   let pr = arr[left] * arr[right];
  //   if (x === pr) {
  //     return true;
  //   }
  //   if (pr > x) {
  //     right--;
  //   }else{
  //     left++;
  //   }
  // }
  // return false;
  // optimised solutions
}

// console.log(isProduct([10, 20, 9, 40], 4, 400));

// The hiring team aims to find 3 candidates who are great collectively.
//  Each candidate has his or her ability expressed as an integer.
// 3 candidates are great collectively if product of their abilities is maximum.
//  Given abilities of N candidates in an array arr[], find the maximum collective
// ability from the given pool of candidates.

function maxProduct(arr, n) {
  //code here
  let prod = 1;
  arr.sort((a, b) => a - b);
  for (let i = n - 1; i > n - 4; i--) {
    prod *= arr[i];
  }
  return prod;
}

console.log(maxProduct([10, 3, 5, 6, 20], 5));

console.log("run practice file");
