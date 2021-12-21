#!/usr/bin/node
if (Process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
    console.log(args[args.length - 2]);
}
