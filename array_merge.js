const arr1 = [1, 65, 78, 90, 8];
const arr2 = [23, 22, 35, 54, 98];
const arr3 = [];

const arr1Length = arr1.length;

const MergeArrayIntoThird = () => {
  for (let i = 0; i < arr1Length; i++) {
    arr3[i] = arr1[i];
    console.log(arr3, "withone");
  }
  for (let i = 0; i < arr2.length; i++) {
    arr3[arr1Length + i] = arr2[i];
    console.log(arr3, "withtwo");
  }
};

// const DefaultMegingMethodMethod = () => {
//   const  arr3 = [...arr1,...arr2]
//     console.log(arr3, 'withtwo')
// }

DefaultMegingMethodMethod();

// space complexity // less variables will have low space complexity
// total variables // 4
// time complexity // less lines have low time complexity
// total lines // 10+8lines
