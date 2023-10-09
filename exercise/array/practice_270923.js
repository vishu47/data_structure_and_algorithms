// ! Given an array of integers of size N, the task is to find the first non-repeating element in this array.

const NonRepeatingElem = (arr, n) => {
  //   for (let i = 0; i < n; i++) {
  //     for (let j = 0; j < n; j++) {
  //       if (arr[i] == arr[j] && i != j) {
  //         break;
  //       }
  //       if (j == n - 1) {
  //         return arr[i];
  //       }
  //     }
  //   }

  // count frequency of items in an array
  let a = {};
  for (let i = 0; i < n; i++) {
    if (a[arr[i]] === undefined) {
      a[arr[i]] = 1;
    } else {
      a[arr[i]]++;
    }
  }
  for (let k = 0; k < n; k++) {
    if (a[arr[k]] === 1) return arr[k];
  }
};

// const arr = [
//   -1, -17, -12, 8, 16, -17, -13, -14, -3, -6, -5, -11, -10, -12, -5, 19, -17,
//   -5, -1, 12,
// ];
// const n = arr.length;
// const output = NonRepeatingElem(arr, n);
// console.log(output);

// ! Given an array arr[] of size n containing 0 and 1 only. The problem is to count the subarrays having an equal number of 0’s and 1’s.

const Pairof1_0 = (arr, n) => {
  const nm = new Map();
  let count = 0;
  let sum = 0;

  for (let i = 0; i < n; i++) {
    // replace 1 with -1 becouse we will calculate sum 0
    if (arr[i] === 0) {
      arr[i] = -1;
    }
    sum += arr[i];

    // if sum is 0 it means that equal no of 0'a and 1's are present

    if (sum === 0) {
      count += 1;
    }
    console.log(count, "l");

    // if sum key is present then value of key will be added in existing count
    if (nm.has(sum) === true) {
      count += nm.get(sum);
      console.log(count, `sumtrue${i}`);
    }
    // if sum key is not present then value of key will set 1 else
    if (nm.has(sum) === false) {
      nm.set(sum, 1);
      console.log(count, `sumfalsetrue${i}`);
    } else {
      nm.set(sum, nm.get(sum) + 1);
      console.log(count, `sumfalse${i}`);
    }
    console.log(nm);
  }
  return count;
};

const arr = [1, 0, 0, 1, 0, 1, 1];
const n = arr.length;
const output = Pairof1_0(arr, n);
console.log(output);

// hash table based question
