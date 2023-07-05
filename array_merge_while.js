const arr2 = [1, 6, 8, 19, 20, 45, 76];
const arr1 = [5, 4, 9, 12, 24];
const arr3 = [];

const MeargeSortedArray = () => {
  let s1 = 0;
  let s2 = 0;
  let s3 = 0;
  while (s1 < arr1.length && s2 < arr2.length) {
    if (arr1[s1] < arr2[s2]) {
      arr3[s3] = arr1[s1];
      s1++;
    } else {
      arr3[s3] = arr2[s2];
      s2++;
    }
    s3++;
  }
  while (s2 < arr2.length) {
    arr3[s3] = arr2[s2];
    s2++;
    s3++;
  }
  console.log(arr3);
};

MeargeSortedArray();

// space complexity // less variables will have low space complexity
// total variables // 6
// time complexity // less lines have low time complexity
// total lines // 10 + 18lines
