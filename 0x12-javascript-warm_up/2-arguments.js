#!/usr/bin/node

const count = process.argv.length;
// console.log(count == 2? 'Arguments found');
if (count == '') {
    console.log('No argument');
} else if (count == 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
