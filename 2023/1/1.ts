import * as fs from 'fs';

const sumLines = (filePath: string) => {
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const lines = fileContent.split('\n');
    let sum = 0;

    for (const line of lines) {
        let left = '';
        let right = '';
        let foundANumber = false;

        for (const char of line) {
            if (Number.isInteger(parseInt(char))) {
                if (foundANumber === false) {
                    left = char;
                    foundANumber = true;
                }

                right = char;
            }
        }

        sum = sum + parseInt(left + right);

    }

    console.log(sum);
};

sumLines('input.txt');
