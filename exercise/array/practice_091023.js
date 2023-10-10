//  ! Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

const Pairof1sand0s = (arr, n) => {
  let sum = 0;
  let count = 0;
  let nm = new Map();

  for (let i = 0; i < n; i++) {
    // replace 0 with -1
    if (arr[i] === 0) {
      arr[i] = -1;
    }
    sum += arr[i];

    // if sum = 0 then eqaul number of 0 nd 1

    if (sum === 0) {
      count += 1;
    }

    if (nm.has(sum) === true) {
      count += nm.get(sum);
    }

    if (nm.has(sum) === false) {
      nm.set(sum, 1);
    } else {
      nm.set(sum, nm.get(sum) + 1);
    }
  }
  return count;
};

// const arr = [1,0,0,1,0,1,1];
// const n = arr.length;
// const output = Pairof1sand0s(arr, n);
// console.log(output)

// ! Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
// ! Note: Array should start with a positive number and 0 (zero) should be considered a positive element.
//  ? order is preserved

const SortBasedOnCon = (arr, n) => {
  let pos = [];
  let neg = [];
  let final = [];
  for (let i = 0; i < n; i++) {
    if (arr[i] >= 0) {
      pos.push(arr[i]);
    } else {
      neg.push(arr[i]);
    }
  }
  let posi = 0;
  for (let j = 0; j < n; j++) {
    if (neg[j] !== undefined || pos[j] !== undefined) {
      final.push(pos[j]);
      if (j < neg.length) {
        final.push(neg[j]);
      }
    }
  }
  return final;

  //   solution time limit exceeded
};

// const arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8];
// const n = arr.length;
// const output = SortBasedOnCon(arr, n);
// console.log(output);

// order not considered
// without using any other space

// rotate right array

const RotateArray = (arr, from, to) => {
  const tmp = arr[to];
  for (let i = to; i >= from; i--) {
    arr[i] = arr[i - 1];
  }
  arr[from] = tmp;
};

const RearrangeArray = (arr, n) => {
  let outofplace = -1;
  for (let i = 0; i < n; i++) {
    if (outofplace >= 0) {
      if (
        (arr[i] < 0 && arr[outofplace] >= 0) ||
        (arr[i] >= 0 && arr[outofplace] < 0)
      ) {
        RotateArray(arr, outofplace, i);

        // update the pointer after rotate
        // calculate the length in between elements from where we have rotated
        if (i - outofplace >= 2) {
          outofplace += 2;
        } else {
          outofplace = -1;
        }
      }
    }

    if (outofplace == -1) {
      if ((i % 2 === 0 && arr[i] < 0) || (i % 2 !== 0 && arr[i] >= 0)) {
        outofplace = i;
      }
    }
  }
  return arr;
};

// const arr = [9, 4, -2, -1, 5, 0, -5, -3, 2];
// const n = arr.length;
// const output = RearrangeArray(arr, n);
// console.log(output);

//  ! Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number
//  ! is followed by negative and vice-versa. Order of elements in output doesn’t matter. Extra positive or negative elements should
//  ! be moved to end.

const RearrangeItems = (arr, n) => {
  const pos = 0;
  let outofplace = -1;
  for (let i = 0; i < n; i++) {
    if (outofplace >= 0) {
      if (
        (arr[i] >= 0 && arr[outofplace] < 0) ||
        (arr[i] < 0 && arr[outofplace] >= 0)
      ) {
        console.log(arr[i], arr[outofplace], "outofplacaee");
        const temp = arr[i];
        arr[i] = arr[outofplace];
        arr[outofplace] = temp;
        outofplace = -1;
      }
    }
    if (outofplace == -1) {
      if ((arr[i] >= 0 && i % 2 == 0) || (arr[i] < 0 && i % 2 != 0)) {
        outofplace = i;
        console.log(outofplace, "outofplace");
      }
    }
  }
  return arr;
};
const arr = [-2, 3, 1];
const n = arr.length;
const output = RearrangeItems(arr, n);
console.log(output);
