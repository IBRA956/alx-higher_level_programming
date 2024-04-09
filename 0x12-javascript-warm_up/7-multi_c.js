if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  let printXt = parseInt(process.argv[2]);
  if (isNaN(printXt)) {
    console.log('Invalid number of occurrences');
  } else {
    while (printXt > 0) {
      console.log('C is fun');
      printXt--;
    }
  }
}

