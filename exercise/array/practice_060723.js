const a = [4, 34, 56, 12, 54, 13, -23, 90, 54, -45];
const b = [2, -34, 56, 12, -12, 13, 23, -90, 54, 45];

const MergeThenSort = () => {
  // merge array
  for (let i = 0; i < b.length; i++) {
    a.push(b[i]);
  }

  // bubble sort
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a.length; j++) {
      if (a[j] > a[j + 1]) {
        const temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
      }
    }
  }
  console.log(a);
};

MergeThenSort();
