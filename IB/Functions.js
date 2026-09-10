function sayGoodbye(name) {
  console.log(`Goodbye, ${name}!`);
}

function excitedGreet(name) {
  name = name.toUpperCase();
  console.log(`HELLO ${name}!!!`);
}

function takeTwoNames(name1, name2) {
  console.log(`Hello ${name1} and ${name2}!`);
}

sayGoodbye(prompt("Enter a name: "));
excitedGreet(prompt("Enter a name: "));
takeTwoNames(prompt("Enter the first name: "), prompt("Enter the second name: "));