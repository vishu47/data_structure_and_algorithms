// no. of loops lengtharr*lengtharr

// const arr1 = [1, 65, 78, 90, 8, 23, 22, 35, 54, 54];
// const arr1 = [23, 22, 35, 54, 98];
const arr1 = [-10, 22, 98, -23, -90, 22, 35, 54, 98];

const BubbleSortArray = () => {
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr1.length; j++) {
      if (arr1[j] > arr1[j + 1]) {
        const temp = arr1[j];
        arr1[j] = arr1[j + 1];
        arr1[j + 1] = temp;
      }
    }
  }
  console.log(arr1);
};

BubbleSortArray();

// traverse from left and compare adjacent elements and the higher one is placed at right side.
// In this way, the largest element is moved to the rightmost end at first.
// This process is then continued to find the second largest and place it and so on until the data is sorted.
