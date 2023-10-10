const RotateArray = (arr, n, from, to) => {
  const tmp = arr[to]
  for (let i = to; i >= from; i--) {
    arr[i] = arr[i - 1];
  }
  arr[from] = tmp
  return arr;
};

const arr = [3, 5, 2, 5, 76, 8, 87];
const n = arr.length;
const from = 2;
const to = 5;
const output = RotateArray(arr, n, from, to);
console.log(output);
