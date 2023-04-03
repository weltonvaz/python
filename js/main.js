function Fibonacci(n) {
    if (n <= 1) return 1;
  
    return Fibonacci(n - 1) + Fibonacci(n - 2);
  }
  
  for (let i = 0; i < 10; i++) {
    console.log(Fibonacci(i));
  }