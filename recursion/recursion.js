const factorial = (number) => {
  if (number === 0) return 1;
  return number * factorial(number - 1);
};

let number = 8;

const FactorialData = factorial(number);
console.log(FactorialData)