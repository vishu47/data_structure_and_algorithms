// ! Program to find the minimum (or maximum) element of an array

// const MinOrMax = (arr) => {
//   let max = 0
//   for (let i = 0; i < arr.length; i++) {
//     if(arr[i] > max){
//       max = arr[i]
//     }
//   }
//   console.log(max)
// }

// // Time complexity : O(n log(n))
// // Auxiliary Space : O(n)

// const MathMinOrMax = (arr) => {
//   const Max = Math.max(...arr)
//   const Min = Math.min(...arr)
//   console.log(Max,Min)
// }

// // Time Complexity: O(n)
// // Auxiliary Space: O(1), as no extra space is used

// const arr = [ -10, 43, 6, 46, 34, 23, 113, 53, 4 ]
// // MinOrMax(arr)
// MathMinOrMax(arr)

// ! K’th Smallest/Largest Element in Unsorted Array
// ? Given an array and a number K where K is smaller than the size of the array. Find the K’th smallest element in the given array. Given that all array elements are distinct.

// const KthSmallesetElementWithBubbleSort = (arr, k) => {
//   for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < arr.length; j++) {
//       if (arr[j] > arr[j + 1]) {
//         let temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//       }
//     }
//   }
//   console.log("Kth smallest element" + " " + arr[k - 1]);
// };

// const KthSmallesetElement = (arr, k) => {
//   const arrSort = arr.sort((a, b) => a - b);
//   console.log("Kth smallest element" + " " + arrSort[k - 1]);
// };

// // ? Time Complexity: O(N log N)
// // ? Auxiliary Space: O(1)

// let arr = [-10, 43, 6, 46, 34, 23, 113, 53, 4];
// KthSmallesetElement(arr, 3);

// ! Count number of occurrences (or frequency) in a sorted array
// ? Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)

// const GetNumberOccurence = (arr, number) => {
//   let occ = 0;
//   for (let i = 0; i < arr.length; i++) {
//     arr[i] === number && occ++;
//   }
//   console.log(`Number ${number} is occured ${occ} times`);
// };

// // Time Complexity: O(n)
// // Space Complexity: O(1), as no extra space is used

// const arr = [1, 1, 2, 2, 2, 2, 3];
// const number = 2;
// GetNumberOccurence(arr, number);

//! Sort an array of 0s, 1s and 2s | Dutch National Flag problem

// SortAnArrayWith0s1s2s = () => {
//   const sort = [0, 1, 2, 0, 1, 2].sort((a, b) => a - b);
//   console.log(sort)
// };

// time complexity exceeded with above approach
// const SortAnArrayWith0s1s2s = (arr) => {
//   let j;
//   let c0 = 0;
//   let c1 = 0;
//   let c2 = 0;
//   for (let i = 0; i < arr.length; i++) {
//     arr[i] === 0 && c0++;
//     arr[i] === 1 && c1++;
//     arr[i] === 2 && c2++;
//   }

//   j = 0;

//   while (c0 > 0) {
//     arr[j++] = 0;
//     c0--;
//   }
//   while (c1 > 0) {
//     arr[j++] = 1;
//     c1--;
//   }
//   while (c2 > 0) {
//     arr[j++] = 2;
//     c2--;
//   }
//   console.log(c0, c1, c2, arr);
// };
// const arr = [0, 1, 2, 0, 1, 2, 2, 1, 0, 1, 1];
// SortAnArrayWith0s1s2s(arr);

// ! Find Subarray with given sum | Set 1 (Non-negative Numbers)
// ? Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.
// ? Note: There may be more than one subarray with sum as the given sum, print first such subarray.
// Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
// Output: Sum found between indexes 1 and 4
// Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7

const SumOfSubArray = (arr, sum) => {
  for (let i = 0; i < arr.length; i++) {
    let sums = arr[i];
    let nums = [];
    for (let j = i + 1; j < arr.length; j++) {
      sums = sums + arr[j];
      nums.push(arr[j])
      if (sums === sum) {
        console.log(`sum found ${sums}`);
        return;
      }else{
        console.log(sums)
      }
    }
  }
};

const arr = [15, 2, 4, 8, 9, 5, 10, 23];
const sum = 23;
SumOfSubArray(arr, sum);
