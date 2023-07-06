let money = 250;
let apple = 0;

const BuyApple = (x) => {
  if (x > 0) {
    console.log("i have left with", x, "rs", "have", apple , 'apples');
    BuyMore(x);
  } else {
    console.log("Not have much money!");
  }
};

const BuyMore = (x) => {
  apple++;
  BuyApple(x - 20);
};

BuyApple(money);

// In indirect recursion, a function calls another function which then calls the first function again.
//  The recursion ends when the base case is met, at this point, the process stops. In this example,
//  the isEven function is determined using the isOdd function, and the isOdd function is determined using the isEven function.
