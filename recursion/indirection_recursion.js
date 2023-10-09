let money = 250;
let apple = 0;

const BuyApple = (rs) => {
  if (rs >= 0) {
    console.log(`i have left with ${rs} rupees and have ${apple} `);
    buyMore(rs);
  } else {
    console.log("not have enough money!!!");
  }
};

const buyMore = (rs) => {
  apple++;
  BuyApple(rs - 24);
};

BuyApple(money);

// In indirect recursion, a function calls another function which then calls the first function again.
//  The recursion ends when the base case is met, at this point, the process stops. In this example,
//  the isEven function is determined using the isOdd function, and the isOdd function is determined using the isEven function.
