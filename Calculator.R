#Add two numbers
num1 = as.numeric(readline(prompt="Enter first number: "))
num2 = as.numeric(readline(prompt="Enter second number: "))

add <- function(num1, num2) {
  return(num1 + num2)
}
print(paste("The sume of :", num1, " + ", num2, "=", add(num1,num2)))

## Substract two numbers
subtract <- function(num1, num2) {
  return(num1 - num2)
}
print(paste("The substraction of :", num1, " - ", num2, "=", subtract(num1,num2)))

## Multiply two numbers
multiply <- function(num1, num2) {
  return (num1 * num2)
}
print(paste("The multiplication of :", num1, " * ", num2, "=", multiply(num1,num2)))

## Division of two numbers
divide <- function(num1, num2) {
  return (num1 / num2)
}
print(paste("The division of :", num1, " / ", num2, "=", divide(num1,num2)))

## Modulus of two numbers
modulus <- function(num1, num2) {
  return (num1 %% num2)
}
print(paste("The modulu of :", num1, " % ", num2, "=", modulus(num1,num2)))

## Exponential of two numbers
Exponential <- function(num1, num2) {
  return(num1 ** num2)
}
print(paste("The exponetial of :", num1, " ** ", num2, "=", Exponential(num1,num2)))
      
## Factorial of number
num = as.integer(readline(prompt="Enter number to get its factorial value: "))
factorial <- function(num) {
  if (num == 0) {
    return(1)
  } else {
    return(num * factorial(num - 1))
  }
}
print(paste("The factorial value of :", num, "=", factorial(num)))

## Square root of a number
num = as.integer(readline(prompt="Enter number to get its square root value: "))
squareRoot <- function(num) {
  if (num >= 0) {
    return (sqrt(num))
  } else{
    return (sqrt(-num)) 
  }
}
print(paste("The square root value of :", num, "=", squareRoot(num)))

## Cube root of a number
num = as.integer(readline(prompt="Enter number to get its cube root value: "))
cubeRoot <- function(num) {
  return (sign(num) * abs(num)^(1/3))
}
print(paste("The cube root value of :", num, "=", cubeRoot(num)))
      
## Sine value of a number
radians = as.numeric(readline(prompt="Enter radians: "))
sine <- function(radians){
  return (radians )
}
result <- sin(radians * (pi/180))
print(paste("The sine value of :", radians, "=", result))

