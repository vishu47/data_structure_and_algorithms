// ! Given an array a of size N which contains elements from 0 to N-1, you need to find all the
// ! elements occurring more than once in the given array. Return the answer in ascending order. If no
// ! such element is found, return list containing [-1].

const DuplicateNumber = (a) => {
  let final = new Set();
  a.sort((a, b) => a - b);
  for (let i = 0; i < a.length; i++) {
    console.log(i);
    if (a[i + 1] === a[i]) {
      final.add(a[i]);
    }
  }
  return final.length <= 0 ? -1 : Array.from(final);
};

let arr = [2, 3, 1, 2, 3];
//   let arr = [0,3,1,2];
// const output = DuplicateNumber(arr);
// console.log(output);

// !! Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.

// this is not work for same number array meane [3,3,3] , [3,3,3] , [3,3,3] outpit shoul be 3 but return will be [3,3,3]
const CommonElements1 = (arr1, arr2, arr3, n1, n2, n3) => {
  const newArr1 = arr1.filter((item) => arr2.includes(item));
  const newArr2 = arr3.filter((item) => newArr1.includes(item));
  return newArr2;
};
const CommonElements = (arr1, arr2, arr3, n1, n2, n3) => {
  // for arr1[], arr2[] and arr3[]
  var i = 0;
  var j = 0;
  var k = 0;
  const arrr = new Set();
  while (i < n1 && j < n2 && k < n3) {
    if (arr1[i] == arr2[j] && arr2[j] == arr3[k]) {
      arrr.add(arr1[i]);
      i++;
      j++;
      k++;
    } else if (arr1[i] < arr2[j]) {
      i++;
    } else if (arr2[j] < arr3[k]) {
      j++;
    } else {
      k++;
    }
  }
  return [...arrr];
};

n1 = 6;
A = [1, 5, 10, 20, 40, 80];
n2 = 5;
B = [6, 7, 20, 80, 100];
n3 = 8;
C = [3, 4, 15, 20, 30, 70, 80, 120];
const output = CommonElements(A, B, C, n1, n2, n3);
console.log(output);
