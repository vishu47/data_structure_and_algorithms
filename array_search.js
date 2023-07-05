const arr = [1, 65, 78, 90, 22, 8, 23, 22, 35, 54, 98];
const item = 98;

const SearchInArray = () => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === item) {
      console.log(`at position ${i}`);
    }
  }
};

SearchInArray();
